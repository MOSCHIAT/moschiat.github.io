"""Utility functions for managing quotes and favorites.

This module handles quote operations including random selection,
categorization, searching, and favorite management with JSON persistence.
"""

import json
import random
from pathlib import Path
from typing import Optional
from quotes import QUOTES

FAVORITES_FILE: str = "favorites.json"


def get_random_quote() -> dict:
    """Get a random quote from the database.
    
    Returns:
        dict: A randomly selected quote with id, author, category, and quote.
    """
    return random.choice(QUOTES)


def get_quote_by_category(category: str) -> list[dict]:
    """Get all quotes from a specific category.
    
    Args:
        category: The category name to filter quotes.
    
    Returns:
        list[dict]: All quotes matching the given category.
                   Returns empty list if category not found.
    """
    return [quote for quote in QUOTES if quote["category"].lower() == category.lower()]


def search_quote(keyword: str) -> list[dict]:
    """Search quotes by keyword in the quote text.
    
    Args:
        keyword: The keyword to search for (case-insensitive).
    
    Returns:
        list[dict]: All quotes containing the keyword in the quote text.
    """
    keyword_lower = keyword.lower()
    return [quote for quote in QUOTES if keyword_lower in quote["quote"].lower()]


def get_all_categories() -> list[str]:
    """Get all available quote categories.
    
    Returns:
        list[str]: Sorted list of unique categories.
    """
    categories = set(quote["category"] for quote in QUOTES)
    return sorted(categories)


def favorite_quote(quote_id: int) -> bool:
    """Add a quote to favorites.
    
    Args:
        quote_id: The ID of the quote to add to favorites.
    
    Returns:
        bool: True if quote was added, False if quote doesn't exist or already favorited.
    """
    # Verify quote exists
    if not any(quote["id"] == quote_id for quote in QUOTES):
        return False
    
    favorites = load_favorites()
    
    # Check if already favorited
    if quote_id in favorites:
        return False
    
    favorites.append(quote_id)
    save_favorites()
    return True


def remove_favorite(quote_id: int) -> bool:
    """Remove a quote from favorites.
    
    Args:
        quote_id: The ID of the quote to remove from favorites.
    
    Returns:
        bool: True if quote was removed, False if not in favorites.
    """
    favorites = load_favorites()
    
    if quote_id not in favorites:
        return False
    
    favorites.remove(quote_id)
    save_favorites()
    return True


def list_favorites() -> list[dict]:
    """Get all favorited quotes.
    
    Returns:
        list[dict]: All quotes that have been marked as favorites.
    """
    favorites = load_favorites()
    
    return [
        quote for quote in QUOTES if quote["id"] in favorites
    ]


def save_favorites() -> None:
    """Save the current favorites list to JSON file.
    
    The favorites are stored in a file defined by FAVORITES_FILE constant.
    Creates the file if it doesn't exist.
    """
    try:
        favorites = load_favorites()
        with open(FAVORITES_FILE, "w", encoding="utf-8") as f:
            json.dump(favorites, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar favoritos: {e}")


def load_favorites() -> list[int]:
    """Load favorites from JSON file.
    
    Returns:
        list[int]: List of favorite quote IDs. Returns empty list if file doesn't exist.
    """
    try:
        if Path(FAVORITES_FILE).exists():
            with open(FAVORITES_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        pass
    
    return []
