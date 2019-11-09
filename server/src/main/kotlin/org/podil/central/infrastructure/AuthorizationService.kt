package org.podil.central.infrastructure

import org.podil.central.model.AuthorizationResponse
import org.podil.central.model.CARD_NOT_FOUND
import org.podil.central.model.WRONG_PIN
import org.podil.central.repository.CardRepository
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.stereotype.Service

@Service
class AuthorizationService @Autowired constructor(
    private val cardRepository: CardRepository
) {

    fun auth(cardId: Long, pin: Int): AuthorizationResponse =
        cardRepository
            .findById(cardId)
            .map {
                it.takeIf { it.pin == pin }
                    ?.let { AuthorizationResponse(true) }
                    ?: AuthorizationResponse(false, WRONG_PIN)
            }
            .orElse(AuthorizationResponse(false, CARD_NOT_FOUND))
}