package org.podil.central.controller

import org.podil.central.infrastructure.TransactionService
import org.podil.central.model.WithdrawRequest
import org.podil.central.model.WithdrawResponse
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
    fun withdraw(@Valid @RequestBody request: WithdrawRequest): WithdrawResponse =
        transactionService.withdraw(request)
}