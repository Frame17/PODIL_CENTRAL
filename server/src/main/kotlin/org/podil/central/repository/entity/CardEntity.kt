package org.podil.central.repository.entity

import javax.persistence.Entity
import javax.persistence.Id
import javax.persistence.Table

@Entity
@Table(name = "cards")
data class CardEntity(
    @Id val id: String,
    val balance: Long
)