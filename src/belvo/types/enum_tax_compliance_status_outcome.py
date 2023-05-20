# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EnumTaxComplianceStatusOutcome(str, enum.Enum):
    """
    Indicates whether the taxpayer is complying to all their tax obligations (`POSITIVE`), if they are not (`NEGATIVE`), or have none to comply to (`NO_OBLIGATIONS`).
    """

    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"
    NO_OBLIGATIONS = "NO_OBLIGATIONS"

    def visit(
        self,
        positive: typing.Callable[[], T_Result],
        negative: typing.Callable[[], T_Result],
        no_obligations: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EnumTaxComplianceStatusOutcome.POSITIVE:
            return positive()
        if self is EnumTaxComplianceStatusOutcome.NEGATIVE:
            return negative()
        if self is EnumTaxComplianceStatusOutcome.NO_OBLIGATIONS:
            return no_obligations()
