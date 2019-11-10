package org.podil.central

import org.junit.After
import org.junit.Assert.*
import org.junit.Before
import org.junit.Test
import org.junit.runner.RunWith
import org.podil.central.model.*
import org.podil.central.repository.CardRepository
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.test.context.SpringBootTest
import org.springframework.boot.test.web.client.TestRestTemplate
import org.springframework.boot.web.server.LocalServerPort
import org.springframework.http.HttpEntity
import org.springframework.test.context.junit4.SpringRunner


@RunWith(SpringRunner::class)
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
class TransactionIntegrationTest {

    @LocalServerPort
    var port: Int = 0

    @Autowired
    lateinit var restTemplate: TestRestTemplate

    @Autowired
    lateinit var cardRepository: CardRepository

    @Before
    fun setUp() {
        cardRepository.updateCardById(17, 1000)
        cardRepository.updateCardById(18, 1000)
    }

    @After
    fun tearDown() {
        cardRepository.updateCardById(17, 0)
        cardRepository.updateCardById(18, 0)
    }

    @Test
    fun withdraw() {
        restTemplate.postForObject(
            "http://localhost:$port/withdraw",
            HttpEntity(WithdrawRequest(17, 200)),
            WithdrawResponse::class.java
        ).run {
            assertTrue(successful)
            assertEquals(800L, balance)
            assertEquals(200L, amount)
        }
    }

    @Test
    fun withdrawLowBalance() {
        restTemplate.postForObject(
            "http://localhost:$port/withdraw",
            HttpEntity(WithdrawRequest(17, 2000)),
            WithdrawResponse::class.java
        ).run {
            assertFalse(successful)
            assertEquals(1000L, balance)
            assertEquals(2000L, amount)
            assertEquals(LOW_BALANCE, reason)
        }
    }

    @Test
    fun withdrawWrongCard() {
        restTemplate.postForObject(
            "http://localhost:$port/withdraw",
            HttpEntity(WithdrawRequest(19, 200)),
            WithdrawResponse::class.java
        ).run {
            assertFalse(successful)
            assertEquals(null, balance)
            assertEquals(200L, amount)
            assertEquals(CARD_NOT_FOUND, reason)
        }
    }

    @Test
    fun deposit() {
        restTemplate.postForObject(
            "http://localhost:$port/deposit",
            HttpEntity(DepositRequest(17, 200)),
            DepositResponse::class.java
        ).run {
            assertTrue(successful)
            assertEquals(1200L, balance)
            assertEquals(200L, amount)
        }
    }

    @Test
    fun depositWrongCard() {
        restTemplate.postForObject(
            "http://localhost:$port/deposit",
            HttpEntity(DepositRequest(19, 200)),
            DepositResponse::class.java
        ).run {
            assertFalse(successful)
            assertEquals(null, balance)
            assertEquals(200L, amount)
            assertEquals(CARD_NOT_FOUND, reason)
        }
    }

    @Test
    fun transfer() {
        restTemplate.postForObject(
            "http://localhost:$port/transfer",
            HttpEntity(TransferRequest(17, 18, 1000)),
            TransferResponse::class.java
        ).run {
            assertTrue(successful)
            assertEquals(0L, balance)
            assertEquals(1000L, amount)
            assertEquals(2000L, cardRepository.findById(18).get().balance)
        }
    }

    @Test
    fun transferWrongFromId() {
        restTemplate.postForObject(
            "http://localhost:$port/transfer",
            HttpEntity(TransferRequest(16, 18, 1000)),
            TransferResponse::class.java
        ).run {
            assertFalse(successful)
            assertEquals(null, balance)
            assertEquals(1000L, amount)
            assertEquals("Card id 16 - $CARD_NOT_FOUND", reason)
        }
    }

    @Test
    fun transferWrongToId() {
        restTemplate.postForObject(
            "http://localhost:$port/transfer",
            HttpEntity(TransferRequest(17, 19, 1000)),
            TransferResponse::class.java
        ).run {
            assertFalse(successful)
            assertEquals(null, balance)
            assertEquals(1000L, amount)
            assertEquals("Card id 19 - $CARD_NOT_FOUND", reason)
        }
    }

    @Test
    fun transferLowBalance() {
        restTemplate.postForObject(
            "http://localhost:$port/transfer",
            HttpEntity(TransferRequest(17, 18, 2000)),
            TransferResponse::class.java
        ).run {
            assertFalse(successful)
            assertEquals(null, balance)
            assertEquals(2000L, amount)
            assertEquals("Card id 17 - $LOW_BALANCE", reason)
        }
    }
}