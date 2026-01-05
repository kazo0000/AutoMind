"""
Generate detailed reports for individual car models.

The report combines static attributes from the dataset with aggregated
external reviews and a simple cost forecast. In a real application
this module could integrate predictive maintenance algorithms,
historical failure statistics and user‑submitted data.
"""

from __future__ import annotations

import os
from typing import Any, Dict, Optional
import pandas as pd

from .aggregator import (
    fetch_youtube_reviews,
    fetch_drom_reviews,
    fetch_otzovik_reviews,
    clean_reviews,
)


# Location of the dataset relative to this file
DATA_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'data', 'cars.csv')
)


def _load_dataset() -> pd.DataFrame:
    return pd.read_csv(DATA_PATH)


def generate_report(car_id: int) -> Optional[Dict[str, Any]]:
    """Generate a detailed report for a specific car.

    Parameters
    ----------
    car_id : int
        Identifier of the car as stored in the CSV dataset.

    Returns
    -------
    dict or None
        A dictionary containing the car attributes, lists of review
        links and a predicted annual cost. Returns ``None`` if the car
        is not found.
    """
    df = _load_dataset()
    row_matches = df[df['id'] == car_id]
    if row_matches.empty:
        return None

    row = row_matches.iloc[0].to_dict()
    model = row.get('model', '')

    # Fetch and clean external reviews
    yt_reviews = clean_reviews(fetch_youtube_reviews(model))
    drom_reviews = clean_reviews(fetch_drom_reviews(model))
    otzovik_reviews = clean_reviews(fetch_otzovik_reviews(model))

    # Simple prediction: annual cost is 10 % of the price
    price = row.get('price', 0)
    try:
        predicted_cost = float(price) * 0.1
    except (ValueError, TypeError):
        predicted_cost = None

    return {
        'car': row,
        'youtube_reviews': yt_reviews,
        'drom_reviews': drom_reviews,
        'otzovik_reviews': otzovik_reviews,
        'predicted_annual_cost': predicted_cost,
    }
