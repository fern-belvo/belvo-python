# This file was auto-generated by Fern from our API Definition.

import typing

from .tax_declaration_business import TaxDeclarationBusiness
from .tax_declaration_individual import TaxDeclarationIndividual

DetailTaxDeclarationResponse = typing.Union[TaxDeclarationIndividual, TaxDeclarationBusiness]
