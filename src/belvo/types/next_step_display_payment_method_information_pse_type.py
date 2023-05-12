# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class NextStepDisplayPaymentMethodInformationPseType(str, enum.Enum):
    PSE_DISPLAY_PAYMENT_METHOD_INFORMATION = "pse_display_payment_method_information"
    PSE_DISPLAY_CREDENTIALS_REQUIRED = "pse_display_credentials_required"
    PSE_DISPLAY_NEEDS_REDIRECT = "pse_display_needs_redirect"
    PSE_DISPLAY_TOKEN_REQUIRED = "pse_display_token_required"
    PSE_DISPLAY_CUSTOMER_BANK_ACCOUNTS = "pse_display_customer_bank_accounts"
    PSE_DISPLAY_CONFIRMATION_REQUIRED = "pse_display_confirmation_required"
    PSE_DISPLAY_PAYMENT_PROCESSING = "pse_display_payment_processing"
    PSE_DISPLAY_PAYMENT_FAILED = "pse_display_payment_failed"
    PSE_DISPLAY_PAYMENT_SUCCEEDED = "pse_display_payment_succeeded"

    def visit(
        self,
        pse_display_payment_method_information: typing.Callable[[], T_Result],
        pse_display_credentials_required: typing.Callable[[], T_Result],
        pse_display_needs_redirect: typing.Callable[[], T_Result],
        pse_display_token_required: typing.Callable[[], T_Result],
        pse_display_customer_bank_accounts: typing.Callable[[], T_Result],
        pse_display_confirmation_required: typing.Callable[[], T_Result],
        pse_display_payment_processing: typing.Callable[[], T_Result],
        pse_display_payment_failed: typing.Callable[[], T_Result],
        pse_display_payment_succeeded: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NextStepDisplayPaymentMethodInformationPseType.PSE_DISPLAY_PAYMENT_METHOD_INFORMATION:
            return pse_display_payment_method_information()
        if self is NextStepDisplayPaymentMethodInformationPseType.PSE_DISPLAY_CREDENTIALS_REQUIRED:
            return pse_display_credentials_required()
        if self is NextStepDisplayPaymentMethodInformationPseType.PSE_DISPLAY_NEEDS_REDIRECT:
            return pse_display_needs_redirect()
        if self is NextStepDisplayPaymentMethodInformationPseType.PSE_DISPLAY_TOKEN_REQUIRED:
            return pse_display_token_required()
        if self is NextStepDisplayPaymentMethodInformationPseType.PSE_DISPLAY_CUSTOMER_BANK_ACCOUNTS:
            return pse_display_customer_bank_accounts()
        if self is NextStepDisplayPaymentMethodInformationPseType.PSE_DISPLAY_CONFIRMATION_REQUIRED:
            return pse_display_confirmation_required()
        if self is NextStepDisplayPaymentMethodInformationPseType.PSE_DISPLAY_PAYMENT_PROCESSING:
            return pse_display_payment_processing()
        if self is NextStepDisplayPaymentMethodInformationPseType.PSE_DISPLAY_PAYMENT_FAILED:
            return pse_display_payment_failed()
        if self is NextStepDisplayPaymentMethodInformationPseType.PSE_DISPLAY_PAYMENT_SUCCEEDED:
            return pse_display_payment_succeeded()
