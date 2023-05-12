# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EnumBankAccountHolderTypePse(str, enum.Enum):
    """
    The type of bank account to create in Belvo. For business bank accounts, this field must the set to `BUSINESS`.
    """

    BUSINESS = "BUSINESS"

    def visit(self, business: typing.Callable[[], T_Result]) -> T_Result:
        if self is EnumBankAccountHolderTypePse.BUSINESS:
            return business()
