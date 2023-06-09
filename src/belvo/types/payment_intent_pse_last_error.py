# This file was auto-generated by Fern from our API Definition.

import typing

from .last_error_invalid_credentials import LastErrorInvalidCredentials
from .last_error_invalid_token import LastErrorInvalidToken
from .last_error_login_error import LastErrorLoginError
from .last_error_payment_error import LastErrorPaymentError
from .last_error_session_expired import LastErrorSessionExpired
from .last_error_two_factor import LastErrorTwoFactor

PaymentIntentPseLastError = typing.Union[
    LastErrorInvalidCredentials,
    LastErrorInvalidToken,
    LastErrorLoginError,
    LastErrorTwoFactor,
    LastErrorPaymentError,
    LastErrorSessionExpired,
]
