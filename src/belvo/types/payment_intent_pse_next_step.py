# This file was auto-generated by Fern from our API Definition.

import typing

from .next_step_display_confirmation_required_pse import NextStepDisplayConfirmationRequiredPse
from .next_step_display_credentials_required_pse import NextStepDisplayCredentialsRequiredPse
from .next_step_display_customer_bank_accounts_pse import NextStepDisplayCustomerBankAccountsPse
from .next_step_display_needs_redirect_pse import NextStepDisplayNeedsRedirectPse
from .next_step_display_payment_method_information_pse import NextStepDisplayPaymentMethodInformationPse
from .next_step_display_token_required_pse import NextStepDisplayTokenRequiredPse

PaymentIntentPseNextStep = typing.Union[
    NextStepDisplayPaymentMethodInformationPse,
    NextStepDisplayCredentialsRequiredPse,
    NextStepDisplayNeedsRedirectPse,
    NextStepDisplayTokenRequiredPse,
    NextStepDisplayCustomerBankAccountsPse,
    NextStepDisplayConfirmationRequiredPse,
]
