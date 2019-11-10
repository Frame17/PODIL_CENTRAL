package org.podil.central

import org.junit.After
import org.junit.Assert.*
import org.junit.Test
import org.junit.runner.RunWith
import org.podil.central.model.RegistrationResponse
import org.podil.central.model.USER_ALREADY_REGISTERED
import org.podil.central.repository.UserRepository
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.test.context.SpringBootTest
import org.springframework.boot.test.web.client.TestRestTemplate
import org.springframework.boot.web.server.LocalServerPort
import org.springframework.test.context.junit4.SpringRunner


@RunWith(SpringRunner::class)
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
class RegistrationIntegrationTest {

    @LocalServerPort
    var port: Int = 0

    @Autowired
    lateinit var restTemplate: TestRestTemplate

    @Autowired
    lateinit var userRepository: UserRepository

    @After
    fun tearDown() {
        userRepository.deleteById(6)
    }

    @Test
    fun register() {
        restTemplate.getForObject(
            "http://localhost:$port/register?id=6",
            RegistrationResponse::class.java
        ).run {
            assertTrue(successful)
        }
    }

    @Test
    fun registerAlreadyExisted() {
        register()
        restTemplate.getForObject(
            "http://localhost:$port/register?id=6",
            RegistrationResponse::class.java
        ).run {
            assertFalse(successful)
            assertEquals(USER_ALREADY_REGISTERED, reason)
        }
    }
}