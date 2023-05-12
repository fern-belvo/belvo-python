# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class NextStepNeedsRedirectType(str, enum.Enum):
    OPEN_FINANCE_DISPLAY_PAYMENT_METHOD_INFORMATION = "open_finance_display_payment_method_information"
    OPEN_FINANCE_DISPLAY_CONFIRMATION_REQUIRED = "open_finance_display_confirmation_required"
    OPEN_FINANCE_DISPLAY_NEEDS_REDIRECT = "open_finance_display_needs_redirect"
    OPEN_FINANCE_DISPLAY_PAYMENT_PROCESSING = "open_finance_display_payment_processing"
    OPEN_FINANCE_DISPLAY_PAYMENT_SUCCEEDED = "open_finance_display_payment_succeeded"
    OPEN_FINANCE_DISPLAY_PAYMENT_FAILED = "open_finance_display_payment_failed"

    def visit(
        self,
        open_finance_display_payment_method_information: typing.Callable[[], T_Result],
        open_finance_display_confirmation_required: typing.Callable[[], T_Result],
        open_finance_display_needs_redirect: typing.Callable[[], T_Result],
        open_finance_display_payment_processing: typing.Callable[[], T_Result],
        open_finance_display_payment_succeeded: typing.Callable[[], T_Result],
        open_finance_display_payment_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NextStepNeedsRedirectType.OPEN_FINANCE_DISPLAY_PAYMENT_METHOD_INFORMATION:
            return open_finance_display_payment_method_information()
        if self is NextStepNeedsRedirectType.OPEN_FINANCE_DISPLAY_CONFIRMATION_REQUIRED:
            return open_finance_display_confirmation_required()
        if self is NextStepNeedsRedirectType.OPEN_FINANCE_DISPLAY_NEEDS_REDIRECT:
            return open_finance_display_needs_redirect()
        if self is NextStepNeedsRedirectType.OPEN_FINANCE_DISPLAY_PAYMENT_PROCESSING:
            return open_finance_display_payment_processing()
        if self is NextStepNeedsRedirectType.OPEN_FINANCE_DISPLAY_PAYMENT_SUCCEEDED:
            return open_finance_display_payment_succeeded()
        if self is NextStepNeedsRedirectType.OPEN_FINANCE_DISPLAY_PAYMENT_FAILED:
            return open_finance_display_payment_failed()
