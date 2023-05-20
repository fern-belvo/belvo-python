# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class InvoiceSenderDetailsDian(pydantic.BaseModel):
    """
    Details regarding the sender.
    """

    collected_at: typing.Optional[str] = pydantic.Field(
        description=("The ISO-8601 timestamp when the data point was collected.\n")
    )
    tax_payer_type: typing.Optional[str] = pydantic.Field(
        description=(
            "Indicates if the sender is a business or an individual. Can be either:\n"
            "\n"
            "  - `Persona Jurídica`\n"
            "  - `Persona Natural`\n"
        )
    )
    regimen: typing.Optional[str] = pydantic.Field(
        description=(
            "The sender's regimen type.\n"
            "\n"
            "For detailed information regarding DIAN's regimens, please see their [official PDF](https://www.dian.gov.co/impuestos/factura-electronica/Documents/Anexo_tecnico_factura_electronica_vr_1_7_2020.pdf).\n"
        )
    )
    tax_scheme: typing.Optional[str] = pydantic.Field(
        description=(
            "The sender's fiscal responsibilities.\n"
            "\n"
            "For detailed information regarding DIAN's tax schemes, please see their [official PDF](https://www.dian.gov.co/impuestos/factura-electronica/Documents/Anexo_tecnico_factura_electronica_vr_1_7_2020.pdf).\n"
        )
    )
    country: typing.Optional[str] = pydantic.Field(description=("The country where the sender pays their taxes.\n"))
    address: typing.Optional[str] = pydantic.Field(description=("The sender's address.\n"))
    phone_number: typing.Optional[str] = pydantic.Field(description=("The sender's phone number.\n"))
    email: typing.Optional[str] = pydantic.Field(description=("The sender's email address.\n"))

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
