# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EnumTaxRetentionPaymentStatus(str, enum.Enum):
    PAID = "PAID"
    PROVISIONED = "PROVISIONED"

    def visit(self, paid: typing.Callable[[], T_Result], provisioned: typing.Callable[[], T_Result]) -> T_Result:
        if self is EnumTaxRetentionPaymentStatus.PAID:
            return paid()
        if self is EnumTaxRetentionPaymentStatus.PROVISIONED:
            return provisioned()
