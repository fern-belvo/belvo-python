# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .display_payment_succeeded import DisplayPaymentSucceeded
from .next_step_display_payment_succeeded_type import NextStepDisplayPaymentSucceededType


class NextStepDisplayPaymentSucceeded(pydantic.BaseModel):
    """
    Object detailing the next steps you should follow for a specific `next_step` type.
    """

    type: typing.Optional[NextStepDisplayPaymentSucceededType] = pydantic.Field(
        description=("The type of `next_step` you need to follow.\n")
    )
    open_finance_display_payment_succeeded: typing.Optional[DisplayPaymentSucceeded]
    ready_to_confirm: typing.Optional[bool] = pydantic.Field(
        description=(
            "Boolean that indicates whether the payment intent is ready to be confirmed.\n"
            "\n"
            "  **Note:** When set to `true`, you need to confirm the payment by making a PATCH request sending through `confirm: true`.\n"
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
