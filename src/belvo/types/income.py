# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .enum_income_source_type import EnumIncomeSourceType
from .income_streams_body import IncomeStreamsBody


class Income(pydantic.BaseModel):
    """
    Income insights
    """

    id: str = pydantic.Field(description=("Belvo's unique identifier for the current income.\n"))
    link: str = pydantic.Field(description=("The `link.id` the account belongs to.\n"))
    created_at: str = pydantic.Field(
        description=("The ISO-8601 timestamp of when the data point was created in Belvo's database.\n")
    )
    income_streams: typing.List[IncomeStreamsBody] = pydantic.Field(
        description=("An array of enriched income stream objects.\n")
    )
    income_source_type: EnumIncomeSourceType
    first_transaction_date: typing.Optional[str] = pydantic.Field(
        description=("The date when the first transaction occurred, in `YYYY-MM-DD` format.\n")
    )
    last_transaction_date: str = pydantic.Field(
        description=("The date when when the last transaction occurred, in `YYYY-MM-DD` format.\n")
    )
    number_of_income_streams: int = pydantic.Field(description=("Number of total income streams analized.\n"))
    monthly_average: float = pydantic.Field(
        description=("Average amount of income received per month across all the accounts for the specific user.\n")
    )
    monthly_average_regular: float = pydantic.Field(
        description=(
            "Average amount of regular income (with a frequency of `MONTHLY`, `FORTNIGHTLY`, or `WEEKLY`) received per month for the specific user.\n"
        )
    )
    monthly_average_irregular: float = pydantic.Field(
        description=(
            "Average amount of irregular income (with a frequency of `SINGLE` or `IRREGULAR`) received per month for the specific user.\n"
        )
    )
    monthly_average_low_confidence: float = pydantic.Field(
        description=("Average amount of income received per month for the specific user with `LOW` confidence.\n")
    )
    monthly_average_medium_confidence: float = pydantic.Field(
        description=("Average amount of income received per month for the specific user with `MEDIUM` confidence.\n")
    )
    monthly_average_high_confidence: float = pydantic.Field(
        description=("Average amount of income received per month for the specific user with `HIGH` confidence.\n")
    )
    total_income_amount: float = pydantic.Field(
        description=("Total amount of all income received for the specific user.\n")
    )
    total_regular_income_amount: float = pydantic.Field(
        description=(
            "Total amount of regular income (with a frequency of `MONTHLY`, `FORTNIGHTLY`, `WEEKLY`) for the specific user.\n"
        )
    )
    total_irregular_income_amount: typing.Optional[float] = pydantic.Field(
        description=(
            "Total amount of irregular income (with a frequency of `SINGLE` or `IRREGULAR`) for the specific user.\n"
        )
    )
    total_low_confidence: float = pydantic.Field(
        description=("Total amount of income for the specific user with `LOW` confidence.\n")
    )
    total_medium_confidence: float = pydantic.Field(
        description=("Total amount of income for the specific user with `MEDIUM` confidence.\n")
    )
    total_high_confidence: float = pydantic.Field(
        description=("Total amount of income for the specific user with `HIGH` confidence.\n")
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