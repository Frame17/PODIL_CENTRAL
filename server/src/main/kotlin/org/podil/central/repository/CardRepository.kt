package org.podil.central.repository

import org.podil.central.repository.entity.CardEntity
import org.springframework.data.jpa.repository.Modifying
import org.springframework.data.jpa.repository.Query
import org.springframework.data.repository.CrudRepository
import org.springframework.stereotype.Repository
import org.springframework.validation.annotation.Validated
import java.util.*
import javax.validation.constraints.Min

@Repository
@Validated
interface CardRepository : CrudRepository<CardEntity, Long> {

    companion object {
        const val FIRST_CARD = 100000000000
        const val DEFAULT_PIN = 1000
        const val PIN_RANGE = 9000
    }

    @Modifying(flushAutomatically = true, clearAutomatically = true)
    @Query("update CardEntity c set c.balance = ?2 where c.id = ?1")
    fun updateCardById(id: Long, @Min(0L) balance: Long)

    fun findAllByUserId(id: Int): Optional<List<CardEntity>>

    @Query("select MAX(id) from cards", nativeQuery = true)
    fun findMostRecentCardId(): Long?
}