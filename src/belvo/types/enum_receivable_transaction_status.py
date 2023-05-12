# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EnumReceivableTransactionStatus(str, enum.Enum):
    APPROVED = "APPROVED"
    CANCELLED = "CANCELLED"
    REVERTED = "REVERTED"
    UNCATEGORIZED = "UNCATEGORIZED"

    def visit(
        self,
        approved: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        reverted: typing.Callable[[], T_Result],
        uncategorized: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EnumReceivableTransactionStatus.APPROVED:
            return approved()
        if self is EnumReceivableTransactionStatus.CANCELLED:
            return cancelled()
        if self is EnumReceivableTransactionStatus.REVERTED:
            return reverted()
        if self is EnumReceivableTransactionStatus.UNCATEGORIZED:
            return uncategorized()
