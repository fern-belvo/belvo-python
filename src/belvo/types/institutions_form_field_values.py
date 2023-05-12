# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class InstitutionsFormFieldValues(pydantic.BaseModel):
    code: typing.Optional[str] = pydantic.Field(description=("The code of the document.\n"))
    label: typing.Optional[str] = pydantic.Field(
        description=(
            "The label for the field. For example:\n"
            "- Cédula de Ciudadanía\n"
            "- Cédula de Extranjería\n"
            "- Pasaporte\n"
        )
    )
    validation: typing.Optional[str] = pydantic.Field(
        description=("The type of input validation used for the field.\n")
    )
    validation_message: typing.Optional[str] = pydantic.Field(
        description=("The message displayed when an invalid input is provided in the form field.\n")
    )
    placeholder: typing.Optional[str] = pydantic.Field(description=("The placeholder text in the form field.\n"))

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}