# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EnumPaymentLinkAllowedPaymentMethod(str, enum.Enum):
    """
    Selected payment method type.

      - For 🇧🇷 Brazil's OFPI, the value must be `open_finance`.
      - For 🇨🇴 Colombia's PSE, the value must be `pse`.
    """

    OPEN_FINANCE = "open_finance"
    PSE = "pse"

    def visit(self, open_finance: typing.Callable[[], T_Result], pse: typing.Callable[[], T_Result]) -> T_Result:
        if self is EnumPaymentLinkAllowedPaymentMethod.OPEN_FINANCE:
            return open_finance()
        if self is EnumPaymentLinkAllowedPaymentMethod.PSE:
            return pse()
