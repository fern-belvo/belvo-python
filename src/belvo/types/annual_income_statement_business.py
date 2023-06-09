# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class AnnualIncomeStatementBusiness(pydantic.BaseModel):
    """
    Object containing the reported annual incomes, deductions, and final balances of the tax payer.
    """

    gross_income_from_ordinary_activities: float = pydantic.Field(
        description=("Total gross income that the company generated from their main economic activity.\n")
    )
    dividends: float = pydantic.Field(description=("Total income that the company generated from dividends.\n"))
    other_income: float = pydantic.Field(
        description=(
            "Total income that the company generated from activities not associated with their main economic activity.\n"
        )
    )
    total_gross_income: float = pydantic.Field(description=("Total gross income the company generated.\n"))
    returns_rebates_and_discounts_on_sales: float = pydantic.Field(
        description=(
            "Total value of cancelled orders, corrected invoices, or similar, that can be discounted from the `total_gross_income`.\n"
        )
    )
    total_net_income: float = pydantic.Field(
        description=("Total net income of the company, taking into account `returns_rebates_and_discounts_on_sales`.\n")
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
