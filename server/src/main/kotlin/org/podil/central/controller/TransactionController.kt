package org.podil.central.controller

import org.podil.central.infrastructure.TransactionService
import org.podil.central.model.DepositRequest
import org.podil.central.model.TransferRequest
import org.podil.central.model.WithdrawRequest
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestBody
import org.springframework.web.bind.annotation.RestController
import javax.validation.Valid

@RestController
class TransactionController @Autowired constructor(
    val transactionService: TransactionService
) {

    @PostMapping("withdraw")
    fun withdraw(@Valid @RequestBody request: WithdrawRequest) =
        request.run {
            transactionService.withdraw(cardId, amount)
        }

    @PostMapping("deposit")
    fun deposit(@Valid @RequestBody request: DepositRequest) =
        request.run {
            transactionService.deposit(cardId, amount)
        }

    @PostMapping("transfer")
    fun transfer(@Valid @RequestBody request: TransferRequest) =
        request.run {
            transactionService.transfer(fromId, toId, amount)
        }
}