package org.podil.central.infrastructure

import org.podil.central.model.RegistrationResponse
import org.podil.central.model.USER_ALREADY_REGISTERED
import org.podil.central.repository.UserRepository
import org.podil.central.repository.entity.UserEntity
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.stereotype.Service

@Service
class RegistrationService @Autowired constructor(
    private val userRepository: UserRepository
) {

    fun register(id: Int) =
        userRepository.run {
            takeUnless { existsById(id) }
                ?.let {
                    save(UserEntity(id))
                    RegistrationResponse(true)
                } ?: RegistrationResponse(false, USER_ALREADY_REGISTERED)
        }
}