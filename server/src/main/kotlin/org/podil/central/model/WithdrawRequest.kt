package org.podil.central.model

import javax.validation.constraints.Min

data class WithdrawRequest(
    val userId: String,
    val cardId: String,
    @get:Min(0) val amount: Long
)