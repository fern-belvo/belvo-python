# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .enum_bank_account_pix_account_type_ofpi import EnumBankAccountPixAccountTypeOfpi
from .enum_payments_country import EnumPaymentsCountry


class BankAccountDetailsOpenFinance(pydantic.BaseModel):
    country: EnumPaymentsCountry
    account_type: EnumBankAccountPixAccountTypeOfpi
    agency: str = pydantic.Field(
        description=("The agency (branch number) of the institution where the account was created.\n")
    )
    number: str = pydantic.Field(description=("The bank account number.\n"))

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
