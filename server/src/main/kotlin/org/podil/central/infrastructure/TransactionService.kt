package org.podil.central.infrastructure

import org.podil.central.model.WithdrawRequest
import org.podil.central.model.WithdrawResponse
import org.podil.central.repository.CardRepository
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.stereotype.Service

@Service
class TransactionService @Autowired constructor(
    private val cardRepository: CardRepository
) {

    fun withdraw(request: WithdrawRequest): WithdrawResponse =
        cardRepository
            .findById(request.cardId)
            .map { card ->
                runCatching {
                    cardRepository.updateCardById(card.id, card.balance - request.amount)
                }.fold(
                    { WithdrawResponse(true, card.balance - request.amount, request.amount) },
                    { WithdrawResponse(false, card.balance, request.amount, "Low Balance") }
                )
            }.orElse(WithdrawResponse(false, null, request.amount, "Card Not Found"))
}