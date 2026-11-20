# Fashion Color Agent – MCP Server

Servidor MCP que ayuda a recomendar productos de moda según la paleta de colores personal del usuario.

## Herramientas disponibles

### `extract_color_palette`
Analiza una foto y extrae la paleta de colores personal: temporada (Spring/Summer/Autumn/Winter), subtono (warm/cool/neutral) y los colores que mejor complementan a la persona.

**Input:**
| Parámetro   | Tipo   | Descripción                        |
|-------------|--------|------------------------------------|
| `image_url` | string | URL o ruta local de la foto        |

**Output:**
```json
{
  "season": "Spring",
  "undertone": "warm",
  "colors": [
    { "name": "Coral Peach", "hex": "#FF6B6B", "role": "primary" },
    ...
  ]
}
```

---

### `recommend_products`
Recomienda productos de moda que coinciden con la paleta de colores del usuario.

**Input:**
| Parámetro     | Tipo         | Descripción                                           |
|---------------|--------------|-------------------------------------------------------|
| `season`      | string       | Temporada de color (e.g. "Spring")                    |
| `undertone`   | string       | Subtono de piel: "warm", "cool" o "neutral"           |
| `hex_colors`  | list[string] | Lista de códigos HEX de la paleta                     |
| `category`    | string       | Filtro de categoría: "Tops", "Bottoms", "Accessories" o "all" |
| `max_results` | int          | Máximo de productos a retornar (default: 5)           |

**Output:**
```json
{
  "query_summary": { ... },
  "products": [
    {
      "id": "prod_001",
      "name": "Coral Linen Blouse",
      "category": "Tops",
      "color": "Coral Peach",
      "hex": "#FF6B6B",
      "price_usd": 45.99,
      "match_score": 0.97,
      "url": "https://example.com/..."
    },
    ...
  ]
}
```

---

## Cómo correr el servidor

```bash
pip install fastmcp
python main.py
```

El servidor corre por HTTP. Para conectarlo a Claude u otro cliente MCP, apunta al host/puerto donde esté escuchando.

## Estructura

```
fashion/
├── main.py        # Servidor MCP con las dos herramientas
└── README.md      # Este archivo
```

## Notas de desarrollo

Los datos en `main.py` están **quemados (stubbed)** como punto de partida:
- `STUBBED_PALETTE` → reemplazar con tu algoritmo de extracción de paleta
- `STUBBED_PRODUCTS` → reemplazar con tu lista/base de datos real de productos
- La lógica de filtrado y scoring en `recommend_products` también es un stub básico
