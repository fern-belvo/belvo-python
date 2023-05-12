# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .display_token_required_content_pse import DisplayTokenRequiredContentPse
from .next_step_display_token_required_pse_type import NextStepDisplayTokenRequiredPseType


class NextStepDisplayTokenRequiredPse(pydantic.BaseModel):
    """
    Object detailing the next steps you should follow for a specific `next_step` type.
    """

    type: typing.Optional[NextStepDisplayTokenRequiredPseType] = pydantic.Field(
        description=("The type of `next_step` you need to follow.\n")
    )
    pse_display_token_required: typing.Optional[DisplayTokenRequiredContentPse]
    ready_to_confirm: typing.Optional[bool] = pydantic.Field(
        description=(
            "Boolean that indicates whether the payment intent is ready to be confirmed. This value will return:\n"
            "\n"
            "  - `false` when a customer wants to pay for the very first time. This is so because you still need to input information about your customer in the following steps to process a payment successfully.\n"
            "  - `true` when a customer wants to pay and this is not their first time. This is so because the payment intent has all the information needed about the customer to process a payment.\n"
            "\n"
            "\n"
            "**Note:** When the value is `true`, you'll need to confirm the payment intent. You can do this by making a PATCH request sending through the parameter `confirm: true`.\n"
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
