package org.podil.central.model

const val CARD_NOT_FOUND = "Card Not Found"
const val LOW_BALANCE = "Low Balance"
const val WRONG_PIN = "Wrong Pin"
const val USER_NOT_FOUND = "User Not Found"
const val NO_CARDS_4_THIS_USER = "This user has no cards"
const val USER_ALREADY_REGISTERED = "User Already Registered"
const val CARD_LIMIT_REACHED = "Reached card limit"

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
    val sentTo: Int?,
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

data class CardGenResponse(
    val successful: Boolean,
    val id: Long?,
    val pin: Int?,
    val reason: String? = null
)