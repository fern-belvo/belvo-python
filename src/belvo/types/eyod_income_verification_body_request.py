# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .enum_income_verification_account_category import EnumIncomeVerificationAccountCategory
from .enum_income_verification_account_holder_type import EnumIncomeVerificationAccountHolderType
from .enum_income_verification_type import EnumIncomeVerificationType


class EyodIncomeVerificationBodyRequest(pydantic.BaseModel):
    transaction_id: str = pydantic.Field(description=("Your unique ID for the income.\n"))
    account_holder_type: EnumIncomeVerificationAccountHolderType
    account_holder_id: str = pydantic.Field(description=("Your unique ID for the account holder, in UUID format.\n"))
    account_id: str = pydantic.Field(description=("Your unique ID for the account where the transaction occurred.\n"))
    account_category: EnumIncomeVerificationAccountCategory
    value_date: str = pydantic.Field(
        description=("The date when the income transaction occurred, in `YYYY-MM-DD` format.\n")
    )
    description: str = pydantic.Field(description=("The description of the income.\n"))
    type: typing.Optional[EnumIncomeVerificationType]
    amount: float = pydantic.Field(description=("The income amount.\n"))
    currency: str = pydantic.Field(
        description=(
            "The three-letter currency code of the income. For example:\n"
            "\n"
            "  • 🇧🇷 BRL (Brazilian Real)\n"
            "  • 🇨🇴 COP (Colombian Peso)\n"
            "  • 🇲🇽 MXN (Mexican Peso)\n"
        )
    )
    institution: str = pydantic.Field(
        description=(
            "The institution where the account is registered.\n"
            "\n"
            "**Note:** This is the name that you use in your system to identify the institution. For example BBVA Retail.\n"
        )
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
