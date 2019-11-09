package org.podil.central.repository

import org.podil.central.repository.entity.CardEntity
import org.springframework.data.jpa.repository.Modifying
import org.springframework.data.jpa.repository.Query
import org.springframework.data.repository.CrudRepository
import org.springframework.stereotype.Repository
import org.springframework.transaction.annotation.Transactional
import org.springframework.validation.annotation.Validated
import java.util.*
import javax.validation.constraints.Min

@Repository
@Validated
interface CardRepository : CrudRepository<CardEntity, Long> {

    @Transactional
    @Modifying(flushAutomatically = true, clearAutomatically = true)
    @Query("update CardEntity c set c.balance = ?2 where c.id = ?1")
    fun updateCardById(id: Long, @Min(0L) balance: Long)

    fun findAllByUserId(id: Int): Optional<List<CardEntity>>
}