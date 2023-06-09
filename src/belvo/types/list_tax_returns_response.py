# This file was auto-generated by Fern from our API Definition.

import typing

from .tax_returns_business_monthly_paginated import TaxReturnsBusinessMonthlyPaginated
from .tax_returns_business_paginated import TaxReturnsBusinessPaginated
from .tax_returns_personal_monthly_paginated import TaxReturnsPersonalMonthlyPaginated
from .tax_returns_personal_paginated import TaxReturnsPersonalPaginated

ListTaxReturnsResponse = typing.Union[
    TaxReturnsPersonalPaginated,
    TaxReturnsPersonalMonthlyPaginated,
    TaxReturnsBusinessPaginated,
    TaxReturnsBusinessMonthlyPaginated,
]
