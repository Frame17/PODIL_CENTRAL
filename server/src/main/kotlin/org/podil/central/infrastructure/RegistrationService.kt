package org.podil.central.infrastructure

import org.podil.central.model.CardGenResponse
import org.podil.central.model.RegistrationResponse
import org.podil.central.model.USER_ALREADY_REGISTERED
import org.podil.central.repository.CardRepository
import org.podil.central.repository.CardRepository.Companion.DEFAULT_PIN
import org.podil.central.repository.CardRepository.Companion.FIRST_CARD
import org.podil.central.repository.CardRepository.Companion.PIN_RANGE
import org.podil.central.repository.UserRepository
import org.podil.central.repository.entity.CardEntity
import org.podil.central.repository.entity.UserEntity
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.stereotype.Service
import kotlin.random.Random.Default.nextInt

@Service
class RegistrationService @Autowired constructor(
    private val userRepository: UserRepository,
    private val cardRepository: CardRepository
) {

    fun register(id: Int) =
        userRepository.run {
            takeUnless { existsById(id) }
                ?.let {
                    save(UserEntity(id))
                    RegistrationResponse(true)
                } ?: RegistrationResponse(false, USER_ALREADY_REGISTERED)
        }

    fun generateCard(id: Int) =
        cardRepository
            .findMostRecentCardId()
            .let {
                CardEntity(it?.inc() ?: FIRST_CARD, id, DEFAULT_PIN + nextInt(PIN_RANGE), 0)
                    .let { card -> cardRepository.save(card) }
            }.run {
                CardGenResponse(this.id, pin)
            }
}