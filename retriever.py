import json
import re
from pathlib import Path


MENU_PATH = Path(__file__).parent / "menu.json"


def load_menu():
    """Load the coffee shop menu from menu.json."""
    with open(MENU_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def search_menu(query: str, max_results: int = 5):
    """
    Retrieve relevant menu items using weighted keyword matching
    with hard dietary/allergen filtering.
    """

    menu = load_menu()
    query_lower = query.lower()

    query_words = set(
        re.findall(r"\b[a-zA-Z]+\b", query_lower)
    )

    # Detect explicit dietary restrictions.
    dairy_free_request = (
        "dairy-free" in query_lower
        or "dairy free" in query_lower
        or "no dairy" in query_lower
        or "without dairy" in query_lower
        or "dairy allergy" in query_lower
        or "allergic to dairy" in query_lower
    )

    vegan_request = (
        "vegan" in query_lower
        or "plant-based" in query_lower
        or "plant based" in query_lower
    )

    results = []

    for item in menu:
        name = item["name"].lower()
        description = item["description"].lower()
        tags = [tag.lower() for tag in item.get("tags", [])]
        allergens = [
            allergen.lower()
            for allergen in item.get("allergens", [])
        ]

        # Hard dietary filters.
        if dairy_free_request:
            if "dairy" in allergens or "dairy-free" not in tags:
                continue

        if vegan_request:
            if "vegan" not in tags:
                continue

        score = 0

        # Exact product-name match.
        if name in query_lower:
            score += 10

        # Preference/tag matches.
        matched_tags = 0

        for word in query_words:
            if word in tags:
                score += 5
                matched_tags += 1

        # Strong bonus when an item satisfies
        # multiple customer preferences.
        if matched_tags >= 2:
            score += 8

        # Product-name word matches.
        name_words = set(
            re.findall(r"\b[a-zA-Z]+\b", name)
        )

        for word in query_words:
            if word in name_words:
                score += 4

        # Description matches.
        for word in query_words:
            if word in description:
                score += 1

        if score > 0:
            results.append(
                {
                    "item": item,
                    "score": score,
                }
            )

    results.sort(
        key=lambda result: result["score"],
        reverse=True,
    )

    return [
        result["item"]
        for result in results[:max_results]
    ]


def format_results(items):
    """Format retrieved menu items as readable grounded context."""

    if not items:
        return "No matching menu items were found."

    formatted = []

    for item in items:
        formatted.append(
            f"""
Name: {item['name']}
Description: {item['description']}
Price: ${item['price']:.2f}
Tags: {', '.join(item.get('tags', []))}
Allergens: {', '.join(item.get('allergens', [])) if item.get('allergens') else 'None'}
""".strip()
        )

    return "\n\n".join(formatted)


def retrieve_menu(query: str) -> str:
    """
    ADK tool for retrieving grounded menu information.

    Returns formatted text instead of raw Python objects.
    """

    results = search_menu(query)

    return format_results(results)