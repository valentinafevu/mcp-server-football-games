from fastmcp import FastMCP
from typing import List

mcp = FastMCP("FashionColorAgent")

STUBBED_PALETTE = {
    "season": "Summer",
    "sub_season": "Cool Summer",
    "undertone": "cool",
    "colors": [
        # Lights / neutrals
        {"name": "Blush Rose",       "hex": "#E8868A", "role": "light"},
        {"name": "Soft Pink",        "hex": "#F0AEBB", "role": "light"},
        {"name": "Cool Beige",       "hex": "#E0D8CC", "role": "neutral_light"},
        # Mids
        {"name": "Dusty Rose",       "hex": "#D08898", "role": "primary"},
        {"name": "Rose Mauve",       "hex": "#A87080", "role": "secondary"},
        {"name": "Warm Taupe",       "hex": "#A09080", "role": "neutral_mid"},
        {"name": "Steel Blue",       "hex": "#708090", "role": "neutral_cool"},
        {"name": "Periwinkle",       "hex": "#6890B8", "role": "accent"},
        # Deeps
        {"name": "Burgundy",         "hex": "#882040", "role": "deep"},
        {"name": "Dark Teal",        "hex": "#2A6060", "role": "deep_cool"},
        {"name": "Navy Blue",        "hex": "#2A3870", "role": "deep"},
        {"name": "Deep Purple",      "hex": "#503060", "role": "deep_accent"},
        # Brights (lower row of the palette)
        {"name": "Teal Jade",        "hex": "#2A9080", "role": "bright_cool"},
        {"name": "Aqua Teal",        "hex": "#28C8A0", "role": "bright_cool"},
        {"name": "Slate Teal",       "hex": "#408080", "role": "secondary"},
        {"name": "Soft Lavender",    "hex": "#7070A0", "role": "accent"},
    ],
}

STUBBED_PRODUCTS = [
    # Tops
    {
        "id": "prod_001",
        "name": "Dusty Rose Silk Blouse",
        "category": "Tops",
        "color": "Dusty Rose",
        "hex": "#D08898",
        "price_usd": 55.00,
        "match_score": 0.97,
        "url": "https://example.com/products/dusty-rose-blouse",
    },
    {
        "id": "prod_002",
        "name": "Periwinkle Knit Sweater",
        "category": "Tops",
        "color": "Periwinkle",
        "hex": "#6890B8",
        "price_usd": 68.00,
        "match_score": 0.95,
        "url": "https://example.com/products/periwinkle-sweater",
    },
    {
        "id": "prod_003",
        "name": "Teal Jade Linen Shirt",
        "category": "Tops",
        "color": "Teal Jade",
        "hex": "#2A9080",
        "price_usd": 48.50,
        "match_score": 0.92,
        "url": "https://example.com/products/teal-linen-shirt",
    },
    # Bottoms
    {
        "id": "prod_004",
        "name": "Navy Straight-Leg Trousers",
        "category": "Bottoms",
        "color": "Navy Blue",
        "hex": "#2A3870",
        "price_usd": 72.00,
        "match_score": 0.96,
        "url": "https://example.com/products/navy-trousers",
    },
    {
        "id": "prod_005",
        "name": "Cool Beige Midi Skirt",
        "category": "Bottoms",
        "color": "Cool Beige",
        "hex": "#E0D8CC",
        "price_usd": 54.00,
        "match_score": 0.90,
        "url": "https://example.com/products/beige-midi-skirt",
    },
    {
        "id": "prod_006",
        "name": "Burgundy Wool Pencil Skirt",
        "category": "Bottoms",
        "color": "Burgundy",
        "hex": "#882040",
        "price_usd": 79.00,
        "match_score": 0.88,
        "url": "https://example.com/products/burgundy-pencil-skirt",
    },
    # Dresses
    {
        "id": "prod_007",
        "name": "Rose Mauve Wrap Dress",
        "category": "Dresses",
        "color": "Rose Mauve",
        "hex": "#A87080",
        "price_usd": 95.00,
        "match_score": 0.94,
        "url": "https://example.com/products/mauve-wrap-dress",
    },
    {
        "id": "prod_008",
        "name": "Slate Teal Slip Dress",
        "category": "Dresses",
        "color": "Slate Teal",
        "hex": "#408080",
        "price_usd": 88.00,
        "match_score": 0.91,
        "url": "https://example.com/products/slate-teal-slip-dress",
    },
    # Accessories
    {
        "id": "prod_009",
        "name": "Silver & Periwinkle Stud Earrings",
        "category": "Accessories",
        "color": "Periwinkle",
        "hex": "#6890B8",
        "price_usd": 22.00,
        "match_score": 0.93,
        "url": "https://example.com/products/periwinkle-studs",
    },
    {
        "id": "prod_010",
        "name": "Deep Purple Structured Bag",
        "category": "Accessories",
        "color": "Deep Purple",
        "hex": "#503060",
        "price_usd": 120.00,
        "match_score": 0.89,
        "url": "https://example.com/products/deep-purple-bag",
    },
    {
        "id": "prod_011",
        "name": "Warm Taupe Leather Belt",
        "category": "Accessories",
        "color": "Warm Taupe",
        "hex": "#A09080",
        "price_usd": 34.00,
        "match_score": 0.86,
        "url": "https://example.com/products/taupe-belt",
    },
    {
        "id": "prod_012",
        "name": "Aqua Teal Silk Scarf",
        "category": "Accessories",
        "color": "Aqua Teal",
        "hex": "#28C8A0",
        "price_usd": 41.00,
        "match_score": 0.84,
        "url": "https://example.com/products/aqua-scarf",
    },
    # Outerwear
    {
        "id": "prod_013",
        "name": "Dark Teal Trench Coat",
        "category": "Outerwear",
        "color": "Dark Teal",
        "hex": "#2A6060",
        "price_usd": 185.00,
        "match_score": 0.92,
        "url": "https://example.com/products/dark-teal-trench",
    },
    {
        "id": "prod_014",
        "name": "Blush Rose Oversized Blazer",
        "category": "Outerwear",
        "color": "Blush Rose",
        "hex": "#E8868A",
        "price_usd": 140.00,
        "match_score": 0.87,
        "url": "https://example.com/products/blush-blazer",
    },
]


# ---------------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------------

@mcp.tool()
def extract_color_palette(image_url: str) -> dict:
    """
    Analyze an image (photo of a person) and extract their personal color palette.

    Returns the detected season, undertone, and a list of colors that
    best complement the person's skin tone, hair color, and eye color.

    Args:
        image_url: URL or local path to the photo that will be analyzed.

    Returns:
        A dict with keys:
            - season (str): e.g. "Spring", "Summer", "Autumn", "Winter"
            - undertone (str): "warm", "cool", or "neutral"
            - colors (list[dict]): each color has name, hex, and role
    """
    # TODO: replace with your real color-extraction algorithm
    return STUBBED_PALETTE


@mcp.tool()
def recommend_products(
    season: str,
    undertone: str,
    hex_colors: List[str],
    category: str = "all",
    max_results: int = 5,
) -> dict:
    """
    Recommend fashion products that match the user's personal color palette.

    Args:
        season: Color season of the user (e.g. "Spring", "Autumn").
        undertone: Skin undertone – "warm", "cool", or "neutral".
        hex_colors: List of HEX color codes from the user's palette (e.g. ["#FF6B6B"]).
        category: Filter by product category – "Tops", "Bottoms", "Accessories",
                  or "all" (default).
        max_results: Maximum number of products to return (default 5).

    Returns:
        A dict with keys:
            - query_summary (dict): echoes back the input palette info
            - products (list[dict]): sorted by match_score descending, each with
              id, name, category, color, hex, price_usd, match_score, url
    """
    # TODO: replace with your real recommendation algorithm
    products = STUBBED_PRODUCTS

    if category != "all":
        products = [p for p in products if p["category"].lower() == category.lower()]

    products = sorted(products, key=lambda p: p["match_score"], reverse=True)
    products = products[:max_results]

    return {
        "query_summary": {
            "season": season,
            "undertone": undertone,
            "hex_colors": hex_colors,
            "category_filter": category,
        },
        "products": products,
    }


if __name__ == "__main__":
    mcp.run(transport="stdio")
