# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .annual_income_statement_individual import AnnualIncomeStatementIndividual
from .document_information_individual import DocumentInformationIndividual
from .equity_statement_individual import EquityStatementIndividual
from .pension_income_statement_individual import PensionIncomeStatementIndividual
from .tax_assessment_individual import TaxAssessmentIndividual
from .tax_payer_information_individual import TaxPayerInformationIndividual


class TaxDeclarationIndividual(pydantic.BaseModel):
    id: str = pydantic.Field(description=("Belvo's unique ID for the current tax declaration.\n"))
    link: str = pydantic.Field(
        description=("Belvo's unique ID of the user that this tax declaration is associated with.\n")
    )
    collected_at: str = pydantic.Field(description=("The ISO-8601 timestamp when the data point was collected.\n"))
    created_at: str = pydantic.Field(
        description=("The ISO-8601 timestamp of when the data point was last updated in Belvo's database.\n")
    )
    document_information: DocumentInformationIndividual
    tax_payer_information: TaxPayerInformationIndividual
    equity_statement: EquityStatementIndividual
    annual_income_statement: AnnualIncomeStatementIndividual
    pension_income_statement: PensionIncomeStatementIndividual
    tax_assessment: TaxAssessmentIndividual
    date_issued: str = pydantic.Field(
        description=("The date the tax declaration was issued by the fiscal institution.\n")
    )
    pdf: typing.Optional[str] = pydantic.Field(description=("The PDF of the tax declaration, as a binary string.\n"))

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
