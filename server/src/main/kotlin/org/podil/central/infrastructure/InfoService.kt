package org.podil.central.infrastructure

import org.podil.central.model.BalanceResponse
import org.podil.central.model.CardsResponse
import org.podil.central.repository.CardRepository
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.stereotype.Service

@Service
class InfoService @Autowired constructor(
    private val cardRepository: CardRepository
) {

    fun balance(cardId: Long): BalanceResponse =
        cardRepository
            .findById(cardId)
            .map {
                BalanceResponse(it.balance)
            }
            .orElse(BalanceResponse(null, "Card Not Found"))

    fun cards(userId: Long): CardsResponse =
        cardRepository
            .findAllByUserId(userId)
            .map {
                it.map { cardEntity ->
                    cardEntity.id
                }.let { cards ->
                    CardsResponse(cards)
                }
            }
            .orElse(CardsResponse(null, "User Not Found"))
}