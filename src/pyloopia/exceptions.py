
class ApiException(Exception) :
    pass


class AuthException(ApiException) :

    def __str__(self) :
        return "Invalid username and/or password."


class DomainOccupiedException(ApiException) :

    def __str__(self) :
        return "The domain is not available for registration."


class RateLimitException(ApiException) :

    def __str__(self) :
        return "Rate limit exceeded."


class BadIndataException(ApiException) :

    def __str__(self) :
        return "Invalid input data."


class UnknownException(ApiException) :

    def __str__(self) :
        return "Unknown API Error."


class InsufficientFundsException(ApiException) :

    def __str__(self) :
        return "Insufficient funds."
