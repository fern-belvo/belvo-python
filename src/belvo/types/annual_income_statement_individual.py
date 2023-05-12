# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .annual_totals_individual import AnnualTotalsIndividual
from .gross_income_individual import GrossIncomeIndividual
from .net_income_individual import NetIncomeIndividual
from .non_taxable_income_individual import NonTaxableIncomeIndividual


class AnnualIncomeStatementIndividual(pydantic.BaseModel):
    """
    Object containing the reported annual incomes, deductions, and final balances of the tax payer.
    """

    gross_income: GrossIncomeIndividual
    non_taxable_income: NonTaxableIncomeIndividual
    net_income: NetIncomeIndividual
    annual_totals: AnnualTotalsIndividual

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}