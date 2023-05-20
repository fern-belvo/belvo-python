# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class TransactionMerchantData(pydantic.BaseModel):
    """
    Additional data regarding the merchant involved in the transaction.
    We only return merchant information for new transactions made from *checking* or *credit card* accounts.
    > **Get merchant information**
     We retrieve the merchant information for a transaction as part of our [Transaction categorization](https://developers.belvo.com/docs/banking#categorizing-transactions) product, turning raw data into actionable insights. To enable this product, just [reach out](https://belvo.com/contact/?utm_source=documentation) to us, and we'll get right to it.
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
