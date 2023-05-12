# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .account import Account
from .enum_recurring_expense_category import EnumRecurringExpenseCategory
from .enum_recurring_expense_frequency import EnumRecurringExpenseFrequency
from .enum_recurring_expense_payment_type import EnumRecurringExpensePaymentType
from .recurring_expense_source_transaction import RecurringExpenseSourceTransaction


class RecurringExpenses(pydantic.BaseModel):
    """
    Recurring expense insights.


    ℹ️ If no recurring expense insights are found, we return an empty array.
    """

    id: typing.Optional[str] = pydantic.Field(
        description=("Belvo's unique identifier used to reference the current recurring expense.\n")
    )
    account: Account
    name: typing.Optional[str] = pydantic.Field(
        description=(
            "The name for the recurring expense.\n"
            "\n"
            'ℹ️ **Note**: This information is taken from the description section of a transaction and then normalized to provide you with an easy-to-read name. As such, sometimes the name will reflect the merchant the payment is made to (for example, Netflix.com), while for other recurring expenses, this could be something like "Monthly payment to John".\n'
        )
    )
    transactions: typing.List[RecurringExpenseSourceTransaction] = pydantic.Field(
        description=(
            "An array of minified transaction objects used to evaluate the recurring expense. If no transactions were found, we return an empty array.\n"
        )
    )
    frequency: EnumRecurringExpenseFrequency
    average_transaction_amount: float = pydantic.Field(
        description=("The average transaction amount of the recurring expense.\n")
    )
    median_transaction_amount: float = pydantic.Field(
        description=("The median transaction amount of the recurring expense.\n")
    )
    days_since_last_transaction: int = pydantic.Field(
        description=(
            "Number of days since the last recurring expense occurred.\n"
            "\n"
            "Based on the frequency, you can infer how many days until the next charge will occur.\n"
        )
    )
    category: EnumRecurringExpenseCategory
    payment_type: EnumRecurringExpensePaymentType

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
