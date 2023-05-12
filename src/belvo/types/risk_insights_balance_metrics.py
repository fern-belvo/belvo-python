# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class RiskInsightsBalanceMetrics(pydantic.BaseModel):
    min_balance_1_w: typing.Optional[float] = pydantic.Field(
        alias="min_balance_1w", description=("The minimum balance in the period (one week).\n")
    )
    min_balance_1_m: typing.Optional[float] = pydantic.Field(
        alias="min_balance_1m", description=("The minimum balance in the period (one month).\n")
    )
    min_balance_3_m: typing.Optional[float] = pydantic.Field(
        alias="min_balance_3m", description=("The minimum balance in the period (three months).\n")
    )
    max_balance_1_w: typing.Optional[float] = pydantic.Field(
        alias="max_balance_1w", description=("The maximum balance in the period (one week).\n")
    )
    max_balance_1_m: typing.Optional[float] = pydantic.Field(
        alias="max_balance_1m", description=("The maximum balance in the period (one month).\n")
    )
    max_balance_3_m: typing.Optional[float] = pydantic.Field(
        alias="max_balance_3m", description=("The maximum balance in the period (three months).\n")
    )
    closing_balance: typing.Optional[float] = pydantic.Field(
        description=("The balance of all the accounts at the `collected_at` time.\n")
    )
    days_balance_below_0_1_w: typing.Optional[int] = pydantic.Field(
        alias="days_balance_below_0_1w",
        description=(
            "The number of days that the total balance of the account is less than or equal to 0 in the last week.\n"
        ),
    )
    days_balance_below_0_1_m: typing.Optional[int] = pydantic.Field(
        alias="days_balance_below_0_1m",
        description=(
            "The number of days that the total balance of the account is less than or equal to 0 in the last month.\n"
        ),
    )
    days_balance_below_0_3_m: typing.Optional[int] = pydantic.Field(
        alias="days_balance_below_0_3m",
        description=(
            "The number of days that the total balance of the account is less than or equal to 0 in the last three months.\n"
        ),
    )
    days_balance_below_x_1_w: typing.Optional[int] = pydantic.Field(
        alias="days_balance_below_x_1w",
        description=(
            "The number of days that the total balance of the account is less than or equal to the amount specified in `balance_threshold_x` in the last week.\n"
        ),
    )
    days_balance_below_x_1_m: typing.Optional[int] = pydantic.Field(
        alias="days_balance_below_x_1m",
        description=(
            "The number of days that the total balance of the account is less than or equal to the amount specified in `balance_threshold_x` in the last month.\n"
        ),
    )
    days_balance_below_x_3_m: typing.Optional[int] = pydantic.Field(
        alias="days_balance_below_x_3m",
        description=(
            "The number of days that the total balance of the account is less than or equal to the amount specified in `balance_threshold_x` in the last three months.\n"
        ),
    )
    balance_threshold_x: float = pydantic.Field(
        description=(
            "The threshold used to compute `days_balance_below_x_period`. Please note, this is value is country specific (both in terms of the amount and the currency).\n"
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
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
