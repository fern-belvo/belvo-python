# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class ReportingId(pydantic.BaseModel):
    """
    Object containing information about where the tax payer reports their income.
    """

    reporting_type: str = pydantic.Field(
        description=(
            "The type of reporting ID. For DIAN, this is the sectional address code (*Codigo Dirrecion Seccional*)\n"
        )
    )
    reporting_value: str = pydantic.Field(description=("The value of the reporting ID.\n"))

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
