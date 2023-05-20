# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .enum_tax_retention_payment_status import EnumTaxRetentionPaymentStatus


class RetentionBreakdown(pydantic.BaseModel):
    """
    A breakdown of the retained taxes
    """

    base_amount: typing.Optional[float] = pydantic.Field(
        description=("The base amount that was used to calculate the tax retention.\n")
    )
    tax_type: typing.Optional[str] = pydantic.Field(
        description=(
            "Optional attribute to indicate the type of tax withheld for the period or year according to the [SAT catalog](https://developers.belvo.com/docs/sat-catalogs#retention-code).\n"
        )
    )
    retained_amount: typing.Optional[float] = pydantic.Field(description=("The amount retained.\n"))
    payment_status: typing.Optional[EnumTaxRetentionPaymentStatus]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
