package org.podil.central.model

import javax.validation.constraints.Min

data class WithdrawRequest(
    val cardId: Long,
    @get:Min(0) val amount: Long
)

class AuthorizationRequest(
    val cardId: Long,
    val pin: Int
)