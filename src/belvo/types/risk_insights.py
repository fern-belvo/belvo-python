# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .risk_insights_balance_metrics import RiskInsightsBalanceMetrics
from .risk_insights_cashflow_metrics import RiskInsightsCashflowMetrics
from .risk_insights_credit_card_metrics import RiskInsightsCreditCardMetrics
from .risk_insights_loans_metrics import RiskInsightsLoansMetrics
from .risk_insights_transaction_metrics import RiskInsightsTransactionMetrics


class RiskInsights(pydantic.BaseModel):
    id: str = pydantic.Field(description=("Belvo's unique ID for the risk insights request.\n"))
    link: str = pydantic.Field(description=("The `link.id` the risk insights analysis belongs to.\n"))
    accounts: typing.Optional[typing.List[str]] = pydantic.Field(
        description=(
            "An array of Belvo-generated account numbers (UUIDs) that were used during the risk insights analysis. If no accounts were found, we return an empty array.\n"
        )
    )
    created_at: str = pydantic.Field(
        description=("The ISO-8601 timestamp of when the data point was last updated in Belvo's database.\n")
    )
    transactions_metrics: typing.Optional[RiskInsightsTransactionMetrics]
    balances_metrics: typing.Optional[RiskInsightsBalanceMetrics]
    cashflow_metrics: typing.Optional[RiskInsightsCashflowMetrics]
    credit_cards_metrics: typing.Optional[RiskInsightsCreditCardMetrics]
    loans_metrics: typing.Optional[RiskInsightsLoansMetrics]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
