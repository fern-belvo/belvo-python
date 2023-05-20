# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class RiskInsightsCashflowMetrics(pydantic.BaseModel):
    """
    Aggregated metrics calculated based on the user's transactions from checking, savings, credit, and loan accounts.

    However, internal transfers (transfers between accounts belonging to the same link) are not used in the calculation.
    """

    sum_positive_1_w: typing.Optional[float] = pydantic.Field(
        alias="sum_positive_1w",
        description=(
            "Sum total of all transactions leading to a positive cashflow in the last week (counted from the time of the request).\n"
        ),
    )
    sum_positive_1_m: typing.Optional[float] = pydantic.Field(
        alias="sum_positive_1m",
        description=(
            "Sum total of all transactions leading to a positive cashflow in the last month (counted from the time of the request).\n"
        ),
    )
    sum_positive_3_m: typing.Optional[float] = pydantic.Field(
        alias="sum_positive_3m",
        description=(
            "Sum total of all transactions leading to a positive cashflow in the last three months (counted from the time of the request).\n"
        ),
    )
    sum_negative_1_w: typing.Optional[float] = pydantic.Field(
        alias="sum_negative_1w",
        description=(
            "Sum total of all transactions leading to a negative cashflow in the last week (counted from the time of the request).\n"
        ),
    )
    sum_negative_1_m: typing.Optional[float] = pydantic.Field(
        alias="sum_negative_1m",
        description=(
            "Sum total of all transactions leading to a negative cashflow in the last month (counted from the time of the request).\n"
        ),
    )
    sum_negative_3_m: typing.Optional[float] = pydantic.Field(
        alias="sum_negative_3m",
        description=(
            "Sum total of all transactions leading to a negative cashflow in the last three months (counted from the time of the request).\n"
        ),
    )
    positive_to_negative_ratio_1_w: typing.Optional[float] = pydantic.Field(
        alias="positive_to_negative_ratio_1w",
        description=(
            "The ratio between sum_positive / sum_negative  in the last week (counted from the time of the request).\n"
            "\n"
            "ℹ️ If the ratio is greater than `1`, it means that the user has more income than outgoing, indicating that they spend less than they earn.\n"
            "\n"
            "**Note**: In the case that there have been no outgoing transactions, the value will be `null`.\n"
        ),
    )
    positive_to_negative_ratio_1_m: typing.Optional[float] = pydantic.Field(
        alias="positive_to_negative_ratio_1m",
        description=(
            "The ratio between sum_positive / sum_negative  in the last month (counted from the time of the request).\n"
            "\n"
            "ℹ️ If the ratio is greater than `1`, it means that the user has more income than outgoing, indicating that they spend less than they earn.\n"
        ),
    )
    positive_to_negative_ratio_3_m: typing.Optional[float] = pydantic.Field(
        alias="positive_to_negative_ratio_3m",
        description=(
            "The ratio between sum_positive / sum_negative  in the last three months (counted from the time of the request).\n"
            "\n"
            "ℹ️ If the ratio is greater than `1`, it means that the user has more income than outgoing, indicating that they spend less than they earn.\n"
        ),
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
