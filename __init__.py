"""Core business logic for the AutoMind application.

This package contains modules for generating shortlists of vehicles
based on user preferences, aggregating external data (currently
placeholder functions), and producing detailed reports. Splitting
these responsibilities into separate modules simplifies future
extensions and unit testing.
"""

from .shortlist import generate_shortlist  # noqa: F401
from .report import generate_report        # noqa: F401