# This file was auto-generated by Fern from our API Definition.

import typing

from .next_step_display_confirmation_required_ofpi import NextStepDisplayConfirmationRequiredOfpi
from .next_step_display_payment_failed import NextStepDisplayPaymentFailed
from .next_step_display_payment_method_information import NextStepDisplayPaymentMethodInformation
from .next_step_display_payment_processing import NextStepDisplayPaymentProcessing
from .next_step_display_payment_succeeded import NextStepDisplayPaymentSucceeded
from .next_step_needs_redirect import NextStepNeedsRedirect

PaymentIntentOfpiNextStep = typing.Union[
    NextStepDisplayPaymentMethodInformation,
    NextStepNeedsRedirect,
    NextStepDisplayConfirmationRequiredOfpi,
    NextStepDisplayPaymentProcessing,
    NextStepDisplayPaymentSucceeded,
    NextStepDisplayPaymentFailed,
]
