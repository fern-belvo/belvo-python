# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .invoice_detail_retained_tax_sat import InvoiceDetailRetainedTaxSat


class InvoiceDetailSat(pydantic.BaseModel):
    description: typing.Optional[str] = pydantic.Field(
        description=("The description of the invoice item (an invoice can have one or more items).\n")
    )
    product_identification: typing.Optional[str] = pydantic.Field(
        description=(
            "The identification code of the product or the service, as defined by the legal entity in the country.\n"
            "- 🇲🇽 [Mexico](http://200.57.3.89/Pys/catPyS.aspx)\n"
        )
    )
    quantity: typing.Optional[int] = pydantic.Field(description=("The quantity of this invoice item.\n"))
    unit_code: typing.Optional[str] = pydantic.Field(
        description=(
            "The unit of measure, as defined by the legal entity in the country. \n"
            "- 🇲🇽 Mexico [SAT catalog reference](https://developers.belvo.com/docs/sat-catalogs#unit-code)\n"
        )
    )
    unit_description: typing.Optional[str] = pydantic.Field(
        description=(
            "The description of the item, as defined by the legal entity in the country.\n"
            "- 🇲🇽 Mexico [SAT catalog reference](https://developers.belvo.com/docs/sat-catalogs#unit-code)\n"
        )
    )
    unit_amount: typing.Optional[float] = pydantic.Field(description=("The price of one a singular item.\n"))
    tax_type: typing.Optional[str] = pydantic.Field(
        description=("**Note**: This field is not applicable for DIAN Colombia and will return `null`.\n")
    )
    pre_tax_amount: typing.Optional[float] = pydantic.Field(
        description=("The total price for this item before tax is applied (`quantity` x `unit_amount`).\n")
    )
    tax_percentage: typing.Optional[float] = pydantic.Field(description=("The tax percentage to apply.\n"))
    tax_amount: typing.Optional[float] = pydantic.Field(
        description=("The amount of tax for this invoice item (`pre_tax_amount` x `tax_percentage`).\n")
    )
    total_amount: typing.Optional[float] = pydantic.Field(
        description=("The total price for this invoice item (`pre_tax_amount` + `tax_amount`).\n")
    )
    retained_taxes: typing.Optional[typing.List[InvoiceDetailRetainedTaxSat]] = pydantic.Field(
        description=("The retained tax on the invoice item.\n")
    )
    collected_at: typing.Optional[str] = pydantic.Field(
        description=("The ISO-8601 timestamp when the data point was collected.\n")
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
