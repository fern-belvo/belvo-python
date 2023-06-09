# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class AccountsCreditData(pydantic.BaseModel):
    """
    The credit options associated with this account.
    """

    credit_limit: typing.Optional[float] = pydantic.Field(
        description=("The maximum amount of credit the owner can receive.\n")
    )
    collected_at: typing.Optional[str] = pydantic.Field(
        description=("The ISO-8601 timestamp when the data point was collected.\n")
    )
    cutting_date: typing.Optional[str] = pydantic.Field(description=("The closing date of the credit period.\n"))
    next_payment_date: typing.Optional[str] = pydantic.Field(
        description=("The due date for the next payment (`YYYY-MM-DD`).\n")
    )
    minimum_payment: typing.Optional[float] = pydantic.Field(
        description=("The minimum amount to be paid on the `next_payment_date`.\n")
    )
    no_interest_payment: typing.Optional[float] = pydantic.Field(
        description=("The minimum amount required to pay to avoid generating interest.\n")
    )
    interest_rate: typing.Optional[float] = pydantic.Field(
        description=("The annualized interest rate of the credit.\n")
    )
    end_date: typing.Optional[str] = pydantic.Field(description=("*This field has been deprecated.*\n"))
    monthly_payment: typing.Optional[float] = pydantic.Field(
        description=("*This field has been deprecated.*\n" "\n" "*The recurrent monthly payment, if applicable.*\n")
    )
    last_payment_date: typing.Optional[str] = pydantic.Field(
        description=(
            "*This field has been deprecated.*\n" "\n" "\n" "*The date when the last credit payment was made.*\n"
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
