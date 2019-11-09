package org.podil.central.model

import javax.validation.constraints.Min

data class WithdrawRequest(
    val cardId: Long,
    @get:Min(0) val amount: Long
)

data class DepositRequest(
    val cardId: Long,
    @get:Min(0) val amount: Long
)

data class TransferRequest(
    val fromId: Long,
    val toId: Long,
    @get:Min(0) val amount: Long
)

data class AuthorizationRequest(
    val cardId: Long,
    val pin: Int
)