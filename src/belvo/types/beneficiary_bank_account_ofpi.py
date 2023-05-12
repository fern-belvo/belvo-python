# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .beneficiary_bank_account_ofpi_details import BeneficiaryBankAccountOfpiDetails
from .holder_response_ofpi import HolderResponseOfpi
from .payment_institution import PaymentInstitution


class BeneficiaryBankAccountOfpi(pydantic.BaseModel):
    id: str = pydantic.Field(description=("Belvo's unique ID for the beneficiary bank account.\n"))
    created_at: str = pydantic.Field(
        description=("The ISO-8601 timestamp of when the data point was last updated in Belvo's database.\n")
    )
    created_by: str = pydantic.Field(description=("Belvo's unique ID for the user that created the bank account.\n"))
    institution: PaymentInstitution
    details: typing.Optional[BeneficiaryBankAccountOfpiDetails]
    holder: HolderResponseOfpi

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
