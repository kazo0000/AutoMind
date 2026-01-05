"""
Functions for generating a shortlist of vehicles based on user preferences.

This module uses a static CSV dataset located in ``data/cars.csv``. The
``generate_shortlist`` function filters the dataset according to the
provided preferences and returns the top N cars sorted by reliability.
In future iterations this logic can be replaced with a smarter ranking
algorithm that takes into account more parameters and user feedback.
"""

from __future__ import annotations

import os
import pandas as pd
from typing import Dict, List, Any, Optional


# Path to the cars dataset relative to this file. Using ``os.path``
# ensures portability when the package is moved or installed.
DATA_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'data', 'cars.csv')
)


def load_data() -> pd.DataFrame:
    """Load the CSV dataset into a pandas DataFrame.

    Returns
    -------
    pd.DataFrame
        The loaded car dataset.
    """
    return pd.read_csv(DATA_PATH)


def generate_shortlist(preferences: Dict[str, Any], top_n: int = 5) -> List[Dict[str, Any]]:
    """Generate a shortlist of cars based on user preferences.

    Parameters
    ----------
    preferences : dict
        A dictionary of user preferences with possible keys ``budget``,
        ``fuel_type`` and ``body_type``. Missing or ``None`` values are
        ignored.
    top_n : int, optional
        Maximum number of cars to return, by default 5.

    Returns
    -------
    list of dict
        A list of cars represented as dictionaries, sorted by
        ``reliability_score`` descending.
    """
    df = load_data().copy()

    # Filter by maximum budget if provided
    budget: Optional[float] = preferences.get('budget')
    if budget:
        df = df[df['price'] <= budget]

    # Filter by fuel type (case-insensitive) unless 'any'
    fuel_type: str = preferences.get('fuel_type', 'any')
    if fuel_type and fuel_type.lower() != 'any':
        df = df[df['fuel_type'].str.lower() == fuel_type.lower()]

    # Filter by body/category unless 'any'
    body_type: str = preferences.get('body_type', 'any')
    if body_type and body_type.lower() != 'any':
        df = df[df['category'].str.lower() == body_type.lower()]

    # Sort by reliability_score descending and by price ascending to break ties
    df = df.sort_values(by=['reliability_score', 'price'], ascending=[False, True])

    # Limit the number of results
    shortlist = df.head(top_n).to_dict(orient='records')
    return shortlist
