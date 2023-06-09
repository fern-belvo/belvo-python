# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .employment_record_document_id import EmploymentRecordDocumentId
from .employment_record_entitlement import EmploymentRecordEntitlement


class EmploymentRecordPersonalData(pydantic.BaseModel):
    """
    Details regarding the personal information of the individual.
    """

    official_name: typing.Optional[str] = pydantic.Field(description=("The legal name of the individual\n"))
    first_name: typing.Optional[str] = pydantic.Field(description=("The first name of the individual.\n"))
    last_name: typing.Optional[str] = pydantic.Field(description=("The last name of the individual.\n"))
    email: typing.Optional[str] = pydantic.Field(
        description=("The email address of the individual (as provided in the initial POST request).\n")
    )
    birth_date: typing.Optional[str] = pydantic.Field(
        description=("The date of the birth of the individual, in `YYYY-MM-DD` format.\n")
    )
    entitlements: typing.Optional[EmploymentRecordEntitlement]
    document_ids: typing.Optional[typing.List[EmploymentRecordDocumentId]] = pydantic.Field(
        description=("Details regarding the individual's ID documents.\n")
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
