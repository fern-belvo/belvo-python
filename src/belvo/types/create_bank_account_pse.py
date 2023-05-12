# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .holder_business_pse import HolderBusinessPse
from .providers_pse import ProvidersPse


class CreateBankAccountPse(pydantic.BaseModel):
    holder: HolderBusinessPse = pydantic.Field(
        description=("Information regarding the business bank account holder.\n")
    )
    providers: ProvidersPse = pydantic.Field(
        description=(
            "Information about the payment service provider, required in order to establish a connection and process requests. For PSE, the value must be `payments_way`.\n"
        )
    )
    number: str = pydantic.Field(description=("The bank account number of the payment beneficiary.\n"))
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        description=(
            "Optional and customizable object where you can provide any additional key-value pairs for your internal purposes. For example, an internal reference number for the payment intent.\n"
            "\n"
            "⚠️ **Note**: You can only provide up to 50 keys (keys can have up to 50 characters each and each value can be up to 500 characters). We do not support nested objects, only ASCII values.\n"
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
