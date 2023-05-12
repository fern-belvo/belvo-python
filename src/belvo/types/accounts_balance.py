# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class AccountsBalance(pydantic.BaseModel):
    """
    Details regarding the current and available balances for the account.
    """

    current: typing.Optional[float] = pydantic.Field(
        description=(
            "The current balance is calculated differently according to the type of account.\n"
            "\n"
            "- **💰 Checking and saving accounts**:\n"
            "\n"
            "The user's account balance at the `collected_at` timestamp.\n"
            "- **💳 Credit cards**:\n"
            "\n"
            "The amount the user has spent in the current card billing period (see `credit_data.cutting_date` for information on when the current billing period finishes).\n"
            "- **🏡 Loan accounts**:\n"
            "\n"
            "The amount remaining to pay on the users's loan (same as `loan_data.outstanding_balance`).\n"
        )
    )
    available: typing.Optional[float] = pydantic.Field(
        description=(
            "The balance that the account owner can use.\n"
            "- **💰 Checking and saving accounts**:\n"
            "\n"
            "The available balance may be different to the `current` balance due to pending transactions.\n"
            "- **💳 Credit cards**:\n"
            "\n"
            "The credit amount the user still has available for the current period. The `available` balance may be different to the `current` balance due to pending transactions or future instalments.\n"
            "- **🏡 Loan accounts**:\n"
            "\n"
            "The present value required to pay off the loan, as provided by the institution.\n"
            "\n"
            "**Note:** If the institution does not provide this value, we return `null`.\n"
        )
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}