# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .bank_account_holder_request_ofpi_information import BankAccountHolderRequestOfpiInformation
from .enum_bank_account_holder_type_ofpi import EnumBankAccountHolderTypeOfpi


class BankAccountHolderRequestOfpi(pydantic.BaseModel):
    """
    Details regarding the business bank account holder.
    """

    type: EnumBankAccountHolderTypeOfpi
    information: BankAccountHolderRequestOfpiInformation

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}