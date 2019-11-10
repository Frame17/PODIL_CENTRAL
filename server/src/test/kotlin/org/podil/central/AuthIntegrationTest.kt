package org.podil.central

import org.junit.Assert.*
import org.junit.Test
import org.junit.runner.RunWith
import org.podil.central.model.AuthorizationRequest
import org.podil.central.model.AuthorizationResponse
import org.podil.central.model.WRONG_PIN
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.test.context.SpringBootTest
import org.springframework.boot.test.web.client.TestRestTemplate
import org.springframework.boot.web.server.LocalServerPort
import org.springframework.http.HttpEntity
import org.springframework.test.context.junit4.SpringRunner


@RunWith(SpringRunner::class)
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
class AuthIntegrationTest {

    @LocalServerPort
    var port: Int = 0

    @Autowired
    lateinit var restTemplate: TestRestTemplate

    @Test
    fun auth() {
        restTemplate.postForObject(
            "http://localhost:$port/auth",
            HttpEntity(AuthorizationRequest(17, 1234)),
            AuthorizationResponse::class.java
        ).run {
            assertTrue(success)
        }
    }

    @Test
    fun authWrongPin() {
        restTemplate.postForObject(
            "http://localhost:$port/auth",
            HttpEntity(AuthorizationRequest(17, 4321)),
            AuthorizationResponse::class.java
        ).run {
            assertFalse(success)
            assertEquals(WRONG_PIN ,reason)
        }
    }
}