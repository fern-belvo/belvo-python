# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class CategorizationMerchantData(pydantic.BaseModel):
    """
    Additional data regarding the merchant involved in the transaction.
    """

    logo: typing.Optional[str] = pydantic.Field(description=("The URL to the merchant's logo.\n"))
    website: typing.Optional[str] = pydantic.Field(description=("The URL to the merchant's website.\n"))
    merchant_name: typing.Optional[str] = pydantic.Field(description=("The name of the merchant.\n"))

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
