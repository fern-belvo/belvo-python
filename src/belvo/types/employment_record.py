# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .employment_record_detail import EmploymentRecordDetail
from .employment_record_file import EmploymentRecordFile
from .employment_record_personal_data import EmploymentRecordPersonalData
from .employment_record_social_security_summary import EmploymentRecordSocialSecuritySummary


class EmploymentRecord(pydantic.BaseModel):
    """
    Emploment record response payload
    """

    id: typing.Optional[str] = pydantic.Field(
        description=("The unique identifier created by Belvo for the current IMSS statement.\n")
    )
    link: typing.Optional[str] = pydantic.Field(
        description=("The unique identifier created by Belvo for the current user.\n")
    )
    created_at: typing.Optional[str] = pydantic.Field(
        description=("The ISO-8601 timestamp of when the data point was initially created in Belvo's database.\n")
    )
    collected_at: typing.Optional[str] = pydantic.Field(
        description=("The ISO-8601 timestamp when the data point was collected.\n")
    )
    report_date: typing.Optional[str] = pydantic.Field(
        description=("The date when the employment record report was generated, in `YYYY-MM-DD` format.\n")
    )
    internal_identification: typing.Optional[str] = pydantic.Field(
        description=("Unique ID for user according to the institution. For IMSS Mexico, this is the CURP.\n")
    )
    personal_data: typing.Optional[EmploymentRecordPersonalData]
    social_security_summary: typing.Optional[EmploymentRecordSocialSecuritySummary]
    employment_records: typing.Optional[typing.List[EmploymentRecordDetail]] = pydantic.Field(
        description=("Details regarding the individual's employment history.\n")
    )
    files: typing.Optional[typing.List[EmploymentRecordFile]] = pydantic.Field(
        description=("Additional PDF binary files relating to the individual's employment.\n")
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
