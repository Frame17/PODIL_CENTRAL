package org.podil.central.model

class AuthorizationResponse(
    val success: Boolean,
    val reason: String? = null
)

data class WithdrawResponse(
    val successful: Boolean,
    val balance: Long?,
    val amount: Long,
    val reason: String? = null
)

data class BalanceResponse(
    val balance: Long?,
    val reason: String? = null
)

data class CardsResponse(
    val cards: List<Long>?,
    val reason: String? = null
)