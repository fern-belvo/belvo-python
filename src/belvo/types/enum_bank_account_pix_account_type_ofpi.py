# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EnumBankAccountPixAccountTypeOfpi(str, enum.Enum):
    """
    The type of bank account. Can be either:

      - `CHECKINGS`
      - `SAVINGS`
      - `SALARY`
    """

    CHECKINGS = "CHECKINGS"
    SAVINGS = "SAVINGS"
    SALARY = "SALARY"

    def visit(
        self,
        checkings: typing.Callable[[], T_Result],
        savings: typing.Callable[[], T_Result],
        salary: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EnumBankAccountPixAccountTypeOfpi.CHECKINGS:
            return checkings()
        if self is EnumBankAccountPixAccountTypeOfpi.SAVINGS:
            return savings()
        if self is EnumBankAccountPixAccountTypeOfpi.SALARY:
            return salary()