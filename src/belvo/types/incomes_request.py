# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .enum_income_minimum_confidence_level_request import EnumIncomeMinimumConfidenceLevelRequest
from .enum_invoice_allowed_income_types_request import EnumInvoiceAllowedIncomeTypesRequest


class IncomesRequest(pydantic.BaseModel):
    link: str = pydantic.Field(description=("The `link.id` that you want to get information for.\n"))
    allowed_income_types: typing.Optional[typing.List[EnumInvoiceAllowedIncomeTypesRequest]]
    minimum_confidence_level: typing.Optional[EnumIncomeMinimumConfidenceLevelRequest]
    date_from: typing.Optional[str] = pydantic.Field(
        description=(
            "The date from which you want to start getting incomes for, in `YYYY-MM-DD` format, within the last 365 days. When you use this parameter, you must also send `date_to`.\n"
            "\n"
            "⚠️ You must have at least 90 days between `date_from` and `date_to`.\n"
            "\n"
            "⚠️ The value of `date_from` cannot be greater than `date_to`.\n"
        )
    )
    date_to: typing.Optional[str] = pydantic.Field(
        description=(
            "The date you want to stop getting incomes for, in `YYYY-MM-DD` format, within the last 365 days. When you use this parameter, you must also send `date_from`.\n"
            "\n"
            "⚠️ You must have at least 90 days between `date_from` and `date_to`.\n"
            "\n"
            "⚠️ The value of `date_to` cannot be greater than today's date (in other words, no future dates).\n"
        )
    )
    token: typing.Optional[str] = pydantic.Field(description=("The OTP token generated by the bank.\n"))
    save_data: typing.Optional[bool] = pydantic.Field(
        description=(
            "Indicates whether or not to persist the data in Belvo. By default, this is set to `true` and we return a 201 Created response.\n"
            "When set to `false`, the data won't be persisted and we return a 200 OK response.\n"
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