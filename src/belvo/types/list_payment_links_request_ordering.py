# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ListPaymentLinksRequestOrdering(str, enum.Enum):
    ASCENDING = "created_at"
    DESCENDING = "-created_at"

    def visit(self, ascending: typing.Callable[[], T_Result], descending: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListPaymentLinksRequestOrdering.ASCENDING:
            return ascending()
        if self is ListPaymentLinksRequestOrdering.DESCENDING:
            return descending()
