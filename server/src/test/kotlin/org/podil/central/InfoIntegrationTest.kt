package org.podil.central

import org.junit.After
import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Before
import org.junit.Test
import org.junit.runner.RunWith
import org.podil.central.model.*
import org.podil.central.repository.CardRepository
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.test.context.SpringBootTest
import org.springframework.boot.test.web.client.TestRestTemplate
import org.springframework.boot.web.server.LocalServerPort
import org.springframework.test.context.junit4.SpringRunner


@RunWith(SpringRunner::class)
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
class InfoIntegrationTest {

    @LocalServerPort
    var port: Int = 0

    @Autowired
    lateinit var restTemplate: TestRestTemplate

    @Autowired
    lateinit var cardRepository: CardRepository

    @Before
    fun setUp() {
        cardRepository.updateCardById(17, 1000)
    }

    @After
    fun tearDown() {
        cardRepository.updateCardById(17, 0)
    }

    @Test
    fun balance() {
        restTemplate.getForObject(
            "http://localhost:$port/balance?id=17",
            BalanceResponse::class.java
        ).run {
            assertEquals(1000L, balance)
        }
    }

    @Test
    fun balanceWrongCard() {
        restTemplate.getForObject(
            "http://localhost:$port/balance?id=71",
            BalanceResponse::class.java
        ).run {
            assertEquals(null, balance)
            assertEquals(CARD_NOT_FOUND, reason)
        }
    }

    @Test
    fun cards() {
        restTemplate.getForObject(
            "http://localhost:$port/cards?id=5",
            CardsResponse::class.java
        ).run {
            assertTrue(cards!!.contains(17) and cards!!.contains(18))
        }
    }

    @Test
    fun cardsWrongUser() {
        restTemplate.getForObject(
            "http://localhost:$port/cards?id=6",
            CardsResponse::class.java
        ).run {
            assertEquals(null, cards)
            assertEquals(NO_CARDS_4_THIS_USER, reason)
        }
    }
}