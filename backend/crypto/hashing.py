from flask import current_app as app
import argon2

import abc


class HashingBackend(abc.ABC):
    @abc.abstractmethod
    def needs_rehash(self, hash: str):
        '''
        Check whether given hash digest needs to be
        hashed again using current parameters.
        '''

        pass

    @abc.abstractmethod
    def hash(self, password: str):
        '''
        Calculate the message digest for the password.
        '''

        pass

    @abc.abstractmethod
    def verify(self, hash: str, password: str):
        '''
        Verify whether password matches the message digest.
        '''

        pass


class ArgonBackend(HashingBackend):
    def __init__(self):
        self._hasher = argon2.PasswordHasher()

    def needs_rehash(self, hash: str):
        return self._hasher.check_needs_rehash(hash)

    def hash(self, password: str):
        return self._hasher.hash(password)

    def verify(self, hash: str, password: str):
        try:
            self._hasher.verify(hash, password)
            return True

        # handle verify mismatch, when password is invalid
        except argon2.exceptions.VerifyMismatchError:
            return False
        
        # handle other exceptions, logging it into application
        except (argon2.exceptions.InvalidHash,
                argon2.exceptions.Argon2Error,) as exc:
            app.log_exception(exc)
            return False



default_backend = ArgonBackend()
