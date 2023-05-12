# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .enum_loan_data_interest_rate_type import EnumLoanDataInterestRateType


class AccountsLoanDataInterestRate(pydantic.BaseModel):
    """
    Breakdown of the interest applied to the loan.
    """

    name: typing.Optional[str] = pydantic.Field(
        description=("The name of the type of interest rate applied to the loan.\n")
    )
    type: EnumLoanDataInterestRateType
    value: typing.Optional[float] = pydantic.Field(description=("The interest rate (in percent or currency value).\n"))

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
