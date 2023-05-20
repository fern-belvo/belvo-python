# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .enum_transaction_bill_status import EnumTransactionBillStatus


class TransactionCreditCardData(pydantic.BaseModel):
    """
    Additional data provided by the institution for credit card transactions.
    """

    collected_at: typing.Optional[str] = pydantic.Field(
        description=("The ISO-8601 timestamp when the data point was collected.\n")
    )
    bill_name: typing.Optional[str] = pydantic.Field(
        description=(
            "The title of the monthly credit card bill the transaction belongs to. The format of the returned value is institution specific, however, some common examples are:\n"
            "\n"
            "- diciembre-2021\n"
            "- dec-2021\n"
            "- dec-21\n"
        )
    )
    bill_status: typing.Optional[EnumTransactionBillStatus]
    bill_amount: typing.Optional[float] = pydantic.Field(
        description=("The aggregate bill amount, as of `collected_at`.\n")
    )
    previous_bill_total: typing.Optional[str] = pydantic.Field(
        description=("The total amount of the previous month's bill, if available.\n")
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
