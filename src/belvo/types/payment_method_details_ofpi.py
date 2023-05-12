# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .payment_links_payment_method_details_body_ofpi import PaymentLinksPaymentMethodDetailsBodyOfpi


class PaymentMethodDetailsOfpi(pydantic.BaseModel):
    """
    Object with information required by Open Finance Payments in Brazil to create a payment intent.
    """

    open_finance: PaymentLinksPaymentMethodDetailsBodyOfpi

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
