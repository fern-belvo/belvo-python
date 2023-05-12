# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .charge import Charge
from .enum_payment_intent_status import EnumPaymentIntentStatus
from .enum_payment_link_allowed_payment_method import EnumPaymentLinkAllowedPaymentMethod
from .enum_payment_link_provider import EnumPaymentLinkProvider
from .enum_payments_currency import EnumPaymentsCurrency
from .payment_intent_payment_method_details_pse import PaymentIntentPaymentMethodDetailsPse
from .payment_intent_pse_last_error import PaymentIntentPseLastError
from .payment_intent_pse_next_step import PaymentIntentPseNextStep
from .payment_method_information_pse import PaymentMethodInformationPse


class PaymentIntentPse(pydantic.BaseModel):
    id: str = pydantic.Field(description=("Belvo's unique ID for the current payment intent.\n"))
    created_at: str = pydantic.Field(
        description=("The ISO-8601 timestamp of when the data point was last updated in Belvo's database.\n")
    )
    created_by: str = pydantic.Field(description=("Belvo's unique ID for the user that created this payment intent.\n"))
    customer: str = pydantic.Field(description=("Belvo's unique ID for the customer related to this payment intent.\n"))
    allowed_payment_method_types: typing.List[EnumPaymentLinkAllowedPaymentMethod] = pydantic.Field(
        description=(
            "A list of payment method types allowed in this payment intent. For PSE, the value will be `pse`.\n"
        )
    )
    amount: str = pydantic.Field(description=("Amount to be paid by your customer.\n"))
    currency: EnumPaymentsCurrency
    description: str = pydantic.Field(description=("The description of the payment.\n"))
    failure_code: typing.Optional[str] = pydantic.Field(
        description=("Error code that explains the reason behind a payment being unsuccessful (if applicable).\n")
    )
    failure_message: typing.Optional[str] = pydantic.Field(
        description=("Further information regarding the `failure_code`.\n")
    )
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        description=(
            "Optional and customizable object where you can provide any additional key-value pairs for your internal purposes. For example, an internal reference number.\n"
            "\n"
            "⚠️ **Note**: You can only provide up to 50 keys (keys can have up to 50 characters each and each value can be up to 500 characters). We do not support nested objects, only ASCII values.\n"
        )
    )
    next_step: PaymentIntentPseNextStep
    last_error: PaymentIntentPseLastError
    payment_method_details: PaymentIntentPaymentMethodDetailsPse
    payment_method_information: PaymentMethodInformationPse
    charges: typing.Optional[typing.List[Charge]] = pydantic.Field(
        description=(
            "An array of charge objects related to this paymnet intent. If no charges are associated, we return an empty array.\n"
            "\n"
            "**Note**: The charges resource will be deprecated and removed from our API by end of Q1 2023. We recommend not using any data from this resource.\n"
        )
    )
    provider: EnumPaymentLinkProvider
    selected_payment_method_type: EnumPaymentLinkAllowedPaymentMethod
    status: EnumPaymentIntentStatus
    updated_at: typing.Optional[str] = pydantic.Field(
        description=("The ISO-8601 timestamp of when the payment intent was last updated.\n")
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