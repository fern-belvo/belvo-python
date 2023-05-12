# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class PaymentMethodInformationBodyPse(pydantic.BaseModel):
    """
    Payment method type selected.
    """

    provider_request_id: typing.Optional[str] = pydantic.Field(
        description=("Unique ID for the payment, as sent by the provider.\n")
    )
    redirect_url: typing.Optional[str] = pydantic.Field(
        description=("URL that redirects the user to the institution's website.\n")
    )
    bank_payment_id: typing.Optional[str] = pydantic.Field(
        description=("Unique payment ID provided the institution.\n")
    )
    end_to_end_id: typing.Optional[str] = pydantic.Field(
        description=("A unique ID for the transaction in Colombia's Payments Way system.\n")
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
