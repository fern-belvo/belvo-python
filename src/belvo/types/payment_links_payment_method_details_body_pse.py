# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class PaymentLinksPaymentMethodDetailsBodyPse(pydantic.BaseModel):
    """
    Details about the organization's bank account that will receive the payment.
    """

    beneficiary_bank_account: str = pydantic.Field(
        description=("Belvo's unique ID used to identify the beneficiary's bank account.\n")
    )
    callback_url: typing.Optional[str] = pydantic.Field(
        description=(
            "The URL to your application that your customer will be directed to once they confirm the payment in their bank application.\n"
        )
    )
    belvo_flow: bool = pydantic.Field(
        description=(
            "This parameter determines the payment flow of the payment intent. By default, this is set to `true` and the payment intent created is processed using the Belvo's payment flow and Belvo-integrated institutions. When set to `false`, the payment intent process uses institutions not integrated into Belvo's flow.\n"
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
