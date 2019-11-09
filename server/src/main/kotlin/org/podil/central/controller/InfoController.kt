package org.podil.central.controller

import org.podil.central.infrastructure.InfoService
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.RequestParam
import org.springframework.web.bind.annotation.RestController

@RestController
class InfoController @Autowired constructor(
    private val infoService: InfoService
) {

    @GetMapping("balance")
    fun balance(@RequestParam("id") cardId: Long) = infoService.balance(cardId)

    @GetMapping("cards")
    fun cards(@RequestParam("id") userId: Int) = infoService.cards(userId)
}