package org.podil.central.infrastructure

import org.podil.central.model.AuthorizationRequest
import org.podil.central.model.AuthorizationResponse
import org.podil.central.repository.CardRepository
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.stereotype.Service

@Service
class AuthorizationService @Autowired constructor(
    private val cardRepository: CardRepository
) {

    fun auth(authRequest: AuthorizationRequest): AuthorizationResponse =
        cardRepository
            .findById(authRequest.cardId)
            .map {
                it.takeIf { it.pin == authRequest.pin }
                    ?.let { AuthorizationResponse(true) }
                    ?: AuthorizationResponse(false, "Wrong Pin")
            }
            .orElse(AuthorizationResponse(false, "Card Not Found"))
}