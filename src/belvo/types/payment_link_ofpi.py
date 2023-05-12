# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .enum_payment_links_status import EnumPaymentLinksStatus
from .payment_intent_ofpi import PaymentIntentOfpi
from .payment_link_callback_urls_response import PaymentLinkCallbackUrlsResponse


class PaymentLinkOfpi(pydantic.BaseModel):
    id: str = pydantic.Field(description=("Belvo's unique ID for the current payment link.\n"))
    created_at: str = pydantic.Field(
        description=("The ISO-8601 timestamp of when the data point was last updated in Belvo's database.\n")
    )
    created_by: str = pydantic.Field(description=("Belvo's unique ID for the user that created the payment link.\n"))
    payment_url: str = pydantic.Field(
        description=("The URL for the hosted-widget that will guide your user through the payments process.\n")
    )
    access_token: typing.Optional[str] = pydantic.Field(
        description=(
            "The Belvo-generated access token for the payment link.\n"
            "\n"
            "**Note:** You'll need the `access_token` to make [Get details for a payment link](https://developers.belvo.com/reference/detailcreatepaymentlink) requests.\n"
        )
    )
    callback_urls: PaymentLinkCallbackUrlsResponse
    payment_intent: typing.Optional[PaymentIntentOfpi]
    updated_at: typing.Optional[str] = pydantic.Field(
        description=("The ISO-8601 timestamp of when the payment link was last updated.\n")
    )
    status: EnumPaymentLinksStatus
    expires_in: str = pydantic.Field(description=("The payment link expiration time.  \n"))
    expires_at: str = pydantic.Field(
        description=("The ISO-8601 timestamp of when the payment link is set to expire.\n")
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
