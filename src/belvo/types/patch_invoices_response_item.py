# This file was auto-generated by Fern from our API Definition.

import typing

from .invoice_dian import InvoiceDian
from .invoice_with_id_sat import InvoiceWithIdSat

PatchInvoicesResponseItem = typing.Union[InvoiceWithIdSat, InvoiceDian]
