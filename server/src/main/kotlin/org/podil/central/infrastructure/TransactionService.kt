package org.podil.central.infrastructure

import org.podil.central.model.*
import org.podil.central.repository.CardRepository
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.stereotype.Service

@Service
class TransactionService @Autowired constructor(
    private val cardRepository: CardRepository
) {

    fun withdraw(cardId: Long, amount: Long): WithdrawResponse =
        cardRepository
            .findById(cardId)
            .map { card ->
                runCatching {
                    cardRepository.updateCardById(card.id, card.balance - amount)
                }.fold(
                    { WithdrawResponse(true, card.balance - amount, amount) },
                    { WithdrawResponse(false, card.balance, amount, LOW_BALANCE) }
                )
            }.orElse(WithdrawResponse(false, null, amount, CARD_NOT_FOUND))

    fun deposit(cardId: Long, amount: Long): DepositResponse =
        cardRepository
            .findById(cardId)
            .map {
                cardRepository.updateCardById(it.id, it.balance + amount)
                DepositResponse(true, it.balance + amount, amount)
            }.orElse(DepositResponse(false, null, amount, CARD_NOT_FOUND))

    fun transfer(fromId: Long, toId: Long, amount: Long): TransferResponse =
        withdraw(fromId, amount)
            .run {
                takeIf {
                    it.successful
                }?.let {
                    cardRepository
                        .findById(toId)
                        .map {
                            TransferResponse(true, it.balance, amount, it.userId)
                        }
                        .orElseGet {
                            deposit(fromId, amount)
                            TransferResponse(false, null, amount, null, "Card id $toId - $CARD_NOT_FOUND")
                        }
                } ?: TransferResponse(false, null, amount, null, "Card id $fromId - $reason")
            }
}