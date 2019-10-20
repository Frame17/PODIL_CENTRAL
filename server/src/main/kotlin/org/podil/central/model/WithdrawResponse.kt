package org.podil.central.model

data class WithdrawResponse(
    val successful: Boolean,
    val balance: Long,
    val amount: Long
)