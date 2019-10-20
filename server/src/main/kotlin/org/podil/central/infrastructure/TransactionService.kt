package org.podil.central.infrastructure

import org.podil.central.model.WithdrawRequest
import org.podil.central.model.WithdrawResponse
import org.podil.central.repository.CardRepository
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.stereotype.Service
import javax.validation.ConstraintViolationException

@Service
class TransactionService @Autowired constructor(
    private val cardRepository: CardRepository
) {

    fun withdraw(request: WithdrawRequest): WithdrawResponse =
        cardRepository
            .findCardById(request.cardId)
            .let {
                try {
                    cardRepository.updateCardById(it.id, it.balance - request.amount)
                    WithdrawResponse(true, it.balance - request.amount, request.amount)
                } catch (e: ConstraintViolationException){
                    WithdrawResponse(false, it.balance, request.amount)
                }
            }
}