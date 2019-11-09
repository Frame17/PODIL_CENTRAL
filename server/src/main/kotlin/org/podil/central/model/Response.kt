package org.podil.central.model

const val CARD_NOT_FOUND = "Card Not Found"
const val LOW_BALANCE = "Low Balance"
const val WRONG_PIN = "Wrong Pin"
const val USER_NOT_FOUND = "User Not Found"
const val USER_ALREADY_REGISTERED = "User Already Registered"

data class AuthorizationResponse(
    val success: Boolean,
    val reason: String? = null
)

data class WithdrawResponse(
    val successful: Boolean,
    val balance: Long?,
    val amount: Long,
    val reason: String? = null
)

data class DepositResponse(
    val successful: Boolean,
    val balance: Long?,
    val amount: Long,
    val reason: String? = null
)

data class TransferResponse(
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

data class RegistrationResponse(
    val successful: Boolean,
    val reason: String? = null
)