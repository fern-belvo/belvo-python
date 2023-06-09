# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .enum_payment_transaction_type import EnumPaymentTransactionType
from .enum_payments_currency import EnumPaymentsCurrency
from .payment_transaction_payer import PaymentTransactionPayer


class PaymentTransaction(pydantic.BaseModel):
    id: str = pydantic.Field(description=("Belvo’s unique ID to reference the transaction.\n"))
    created_at: str = pydantic.Field(
        description=("The ISO-8601 timestamp of when the data point was last updated in Belvo's database.\n")
    )
    created_by: str = pydantic.Field(description=("Belvo's unique ID for the user that created the payment.\n"))
    amount: str = pydantic.Field(
        description=(
            "The transaction amount.\n"
            "\n"
            "\n"
            "**Note**: The amount displayed is always positive as we indicate the direction of the transaction in `transaction_type` parameter.\n"
        )
    )
    currency: EnumPaymentsCurrency
    description: str = pydantic.Field(description=("The description of the payment.\n"))
    transaction_type: EnumPaymentTransactionType
    beneficiary: str = pydantic.Field(
        description=("Belvo's unique ID used to identify the beneficiary's bank account.\n")
    )
    payer: PaymentTransactionPayer
    payment_intent: typing.Optional[str] = pydantic.Field(
        description=("The unique ID of the payment intent associated with the transaction.\n")
    )
    customer: typing.Optional[str] = pydantic.Field(
        description=("Belvo's unique ID for the customer asscociated with this transaction.\n")
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
