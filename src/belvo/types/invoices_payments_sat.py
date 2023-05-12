# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .invoices_payments_related_documents_sat import InvoicesPaymentsRelatedDocumentsSat


class InvoicesPaymentsSat(pydantic.BaseModel):
    date: typing.Optional[str] = pydantic.Field(description=("ISO-8601 timestamp when the payment was made.\n"))
    payment_type: typing.Optional[str] = pydantic.Field(
        description=(
            "Payment type code used for this invoice, as defined by the country's legal entity.\n"
            "\n"
            "- 🇲🇽 Mexico [SAT catalog reference article](https://developers.belvo.com/docs/sat-catalogs#payment-type)\n"
        )
    )
    currency: typing.Optional[str] = pydantic.Field(
        description=(
            "The currency of the payment. For example:\n"
            "\n"
            "- 🇧🇷 BRL (Brazilian Real)\n"
            "- 🇨🇴 COP (Colombian Peso)\n"
            "- 🇲🇽 MXN (Mexican Peso)\n"
            "\n"
            "Please note that other currencies other than in the list above may be returned.\n"
        )
    )
    exchange_rate: typing.Optional[str] = pydantic.Field(
        description=("The `currency` to MXN currency exchange rate when the payment was made.\n")
    )
    amount: typing.Optional[float] = pydantic.Field(
        description=("The invoice amount, in the currency of the original invoice.\n")
    )
    operation_number: typing.Optional[str] = pydantic.Field(
        description=("The fiscal institution's internal identifier for the operation.\n")
    )
    beneficiary_rfc: typing.Optional[str] = pydantic.Field(description=("The fiscal ID of the payment beneficiary.\n"))
    beneficiary_account_number: typing.Optional[str] = pydantic.Field(
        description=("The bank account number of the payment beneficiary.\n")
    )
    payer_rfc: typing.Optional[str] = pydantic.Field(description=("The fiscal ID of the payment issuer.\n"))
    payer_account_number: typing.Optional[str] = pydantic.Field(
        description=("The bank account number of the payment issuer.\n")
    )
    payer_bank_name: typing.Optional[str] = pydantic.Field(
        description=("The banking institution that was used by the payment issuer.\n")
    )
    related_documents: typing.List[InvoicesPaymentsRelatedDocumentsSat] = pydantic.Field(
        description=("A list of all the related deferred invoices affected by the payment.\n")
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
