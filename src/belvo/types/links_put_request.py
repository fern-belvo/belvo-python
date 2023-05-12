# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class LinksPutRequest(pydantic.BaseModel):
    password: str = pydantic.Field(description=("The end-user's password used to log in to the institution.\n"))
    password_2: typing.Optional[str] = pydantic.Field(
        alias="password2",
        description=(
            "The end-user's second password used to log in to the institution.\n"
            "\n"
            "ℹ️ This is only required by some institutions. To know which institutions require a second password, get the [details](https://developers.belvo.com/reference/detailinstitution) for the institution and check the `form_fields` array in the response.\n"
        ),
    )
    token: typing.Optional[str] = pydantic.Field(description=("The MFA token required by the bank to log in.\n"))
    username_type: typing.Optional[str] = pydantic.Field(
        description=(
            "Type of document to be used as a username.\n"
            "\n"
            "  Some banking institutions accept different documents to be used as the `username` to login. For example, the *Cédula de Ciudadanía*, *Cédula de Extranjería*, *Pasaporte'*, and so on.\n"
            "\n"
            "  For banks that require a document to log in, you **must** provide the `username_type` parameter to specify which document is used when creating the link.\n"
            "\n"
            "  ℹ️ To know which institutions require the `username_type` parameter, get the [details](https://developers.belvo.com/reference/detailinstitution) for the institution and check the `form_fields` array in the response.\n"
            "\n"
            "  For a list of standards codes, see the table below.\n"
            "\n"
            "| Code | Description |\n"
            "|-----------|-------|\n"
            "| `001` | Cédula de Ciudadanía |\n"
            "| `002` | Cédula de Extranjería |\n"
            "| `003` | Pasaporte |\n"
            "| `004` | Tarjeta de Identidad |\n"
            "| `005` | Registro Civil |\n"
            "| `006` | Número Identificación Personal |\n"
            "| `020` | NIT |\n"
            "| `021` | NIT Persona Natural |\n"
            "| `022` | NIT Persona Extranjera |\n"
            "| `023` | NIT Persona Jurídica |\n"
            "| `024` | NIT Menores |\n"
            "| `025` | NIT Desasociado |\n"
            "| `030` | Trj. Seguro Social Extranjero |\n"
            "| `031` | Sociedad Extranjera sin NIT en Colombia |\n"
            "| `032` | Fideicomiso |\n"
            "| `033` | RIF Venezuela |\n"
            "| `034` | CIF |\n"
            "| `035` | Número de Identidad |\n"
            "| `036` | RTN |\n"
            "| `037` | Cédula de Identidad |\n"
            "| `038` | DIMEX |\n"
            "| `039` | CED |\n"
            "| `040` | PAS |\n"
            "| `041` | Documento Único de Identidad |\n"
            "| `042` | NIT Salvadoreño |\n"
            "| `100` | Agência e conta |\n"
            "| `101` | Código do operador |\n"
            "| `102` | Cartão de crédito |\n"
            "| `103` | CPF |\n"
        )
    )
    certificate: typing.Optional[str] = pydantic.Field(
        description=(
            "For certain fiscal institutions, it is possible to log in using a certificate and a private key, which enables a faster connection to the institution.\n"
            "\n"
            "Belvo supports a base64 encoded `certificate`. If the `certificate` parameter is used, you *must* also provide the `private_key` parameter.\n"
        )
    )
    private_key: typing.Optional[str] = pydantic.Field(
        description=(
            "For certain fiscal institutions, it is possible to log in using a certificate and a private key, which enables a faster connection to the institution.\n"
            "\n"
            "Belvo supports a base64 encoded `private_key`. If the `private_key` parameter is used, you *must* also provide the `certificate` parameter.\n"
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
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}