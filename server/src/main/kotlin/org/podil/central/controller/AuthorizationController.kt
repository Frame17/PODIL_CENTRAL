package org.podil.central.controller

import org.podil.central.infrastructure.AuthorizationService
import org.podil.central.model.AuthorizationRequest
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestBody
import org.springframework.web.bind.annotation.RestController

@RestController
class AuthorizationController(
    private val authorizationService: AuthorizationService
) {

    @PostMapping("auth")
    fun auth(@RequestBody authRequest: AuthorizationRequest) =
        authorizationService.auth(authRequest)
}