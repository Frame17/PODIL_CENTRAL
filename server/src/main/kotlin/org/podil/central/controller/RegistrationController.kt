package org.podil.central.controller

import org.podil.central.infrastructure.RegistrationService
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.RequestParam
import org.springframework.web.bind.annotation.RestController

@RestController
class RegistrationController @Autowired constructor(
    private val registrationService: RegistrationService
) {

    @GetMapping("register")
    fun register(@RequestParam id: Int) =
        registrationService.register(id)

    @GetMapping("generate-card")
    fun cardGen(@RequestParam id: Int) =
        registrationService.generateCard(id)
}