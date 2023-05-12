# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .tax_status_address_between_street_sat import TaxStatusAddressBetweenStreetSat


class TaxStatusAddressSat(pydantic.BaseModel):
    postal_code: typing.Optional[str] = pydantic.Field(description=("The postcode of the address.\n"))
    street_type: typing.Optional[str] = pydantic.Field(description=("The `street` type.\n"))
    street: typing.Optional[str] = pydantic.Field(description=("The tax payers street.\n"))
    exterior_number: typing.Optional[str] = pydantic.Field(description=("The street number.\n"))
    interior_number: typing.Optional[str] = pydantic.Field(description=("Additional address information.\n"))
    suburb: typing.Optional[str] = pydantic.Field(description=("The suburb of the tax payer.\n"))
    locality: typing.Optional[str] = pydantic.Field(description=("The locality of the address.\n"))
    municipality: typing.Optional[str] = pydantic.Field(description=("The municipality of the address.\n"))
    state: typing.Optional[str] = pydantic.Field(description=("The state that the address is in.\n"))
    between_street: typing.Optional[typing.List[TaxStatusAddressBetweenStreetSat]] = pydantic.Field(
        description=("Additional information about where the `street` is located.\n")
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
