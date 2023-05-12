# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class TaxStatusEconomicActivitySat(pydantic.BaseModel):
    economic_activity: typing.Optional[str] = pydantic.Field(
        description=("The description of the economic activity.\n")
    )
    initial_date: typing.Optional[str] = pydantic.Field(description=("The start date of the economic activity.\n"))
    end_date: typing.Optional[str] = pydantic.Field(description=("The end date of the economic activity.\n"))
    order: typing.Optional[str] = pydantic.Field(description=("The order of the economic activity.\n"))
    percentage: typing.Optional[str] = pydantic.Field(description=("The percentage of the economic activity.\n"))

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
