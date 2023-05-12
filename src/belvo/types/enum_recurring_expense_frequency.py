# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EnumRecurringExpenseFrequency(str, enum.Enum):
    """
    The frequency at which this recurring expense occurs.


    ℹ️ **Note:** Belvo only identifies `MONTHLY` frequencies.
    """

    MONTHLY = "MONTHLY"

    def visit(self, monthly: typing.Callable[[], T_Result]) -> T_Result:
        if self is EnumRecurringExpenseFrequency.MONTHLY:
            return monthly()