# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class ValidationError(pydantic.BaseModel):
    """
    This error occurs when you try to resume a request session that has already expired. This is usually because the user took too long to provide their authentication token.
    """

    code: typing.Optional[str] = pydantic.Field(
        description=(
            "A unique error code (`null`, `does_not_exist`, `required`) that allows you to classify and handle the error programmatically.\n"
            "\n"
            "ℹ️ Check our DevPortal for more information on how to handle:\n"
            '  - <a href="https://developers.belvo.com/docs/belvo-api-errors#400-blank" target="_blank">400 blank errors</a>\n'
            '  - <a href="https://developers.belvo.com/docs/belvo-api-errors#400-null" target="_blank">400 null errors</a>\n'
            '  - <a href="https://developers.belvo.com/docs/belvo-api-errors#400-does_not_exist" target="_blank">400 does_not_exist errors</a>\n'
            '  - <a href="https://developers.belvo.com/docs/belvo-api-errors#400-required" target="_blank">400 required errors</a>\n'
        )
    )
    message: typing.Optional[str] = pydantic.Field(
        description=(
            "A short description of the error.\n"
            "\n"
            "For `session_expired` errors, the description can be (among others):\n"
            "\n"
            "  - `This field is required.`\n"
            "  - `Object with name=narnia does not exist.`\n"
            "  - `This field may not be null.`\n"
            "  - `This field may not be blank.`\n"
        )
    )
    request_id: typing.Optional[str] = pydantic.Field(
        description=(
            "A 32-character unique ID of the request (matching a regex pattern of: `[a-f0-9]{32}`). Provide this ID when contacting the Belvo support team to accelerate investigations.\n"
        )
    )
    field: typing.Optional[str] = pydantic.Field(description=("Name of the field where the error was encountered.\n"))

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
