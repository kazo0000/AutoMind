"""
Placeholder functions for aggregating external automotive data.

AutoMind aims to collect unbiased information about vehicles from
multiple sources: YouTube reviews, classifieds like Drom, user
review sites such as Otzovik, and various forums. In this MVP
implementation these functions return static dummy data, but they
illustrate the API that a real implementation would provide.
"""

from typing import List


def fetch_youtube_reviews(model: str) -> List[str]:
    """Return a list of YouTube URLs for reviews of a given model.

    Parameters
    ----------
    model : str
        The car model name.

    Returns
    -------
    list of str
        Dummy list of YouTube URLs.
    """
    # In a real implementation this function would call the YouTube API
    # or scrape search results. Here we return static examples.
    return [
        f"https://www.youtube.com/watch?v=dummy_review_{model.lower()}_1",
        f"https://www.youtube.com/watch?v=dummy_review_{model.lower()}_2",
    ]


def fetch_drom_reviews(model: str) -> List[str]:
    """Return a list of Drom URLs for reviews of a given model."""
    return [
        f"https://www.drom.ru/review/{model.lower()}-dummy-1.html",
        f"https://www.drom.ru/review/{model.lower()}-dummy-2.html",
    ]


def fetch_otzovik_reviews(model: str) -> List[str]:
    """Return a list of Otzovik URLs for reviews of a given model."""
    return [
        f"https://otzovik.com/review_{model.lower()}_1.html",
        f"https://otzovik.com/review_{model.lower()}_2.html",
    ]


def clean_reviews(reviews: List[str]) -> List[str]:
    """Clean a list of review links.

    A future implementation would remove promotional content, filter
    duplicates, and perhaps summarize sentiments. Here we simply
    return the input unchanged.
    """
    return reviews
