# This file was auto-generated by Fern from our API Definition.

import typing

from .bank_account_details_ofpi import BankAccountDetailsOfpi
from .bank_account_details_ofpi_pix import BankAccountDetailsOfpiPix

BankAccountOfpiResponseDetails = typing.Union[BankAccountDetailsOfpi, BankAccountDetailsOfpiPix]
