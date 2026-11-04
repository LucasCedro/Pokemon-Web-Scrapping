# Pokedex scraper

Two-level Scrapy crawl. An index page is parsed for Pokémon links, then each link is requested and reduced to a fixed schema. `ROBOTSTXT_OBEY` stays on. The sites are public.

| Spider | File | Source | What it keeps |
|--------|------|--------|----------------|
| `pokedex` | `BoardGames/spiders/GBG.py` | [pokemon.com/br/pokedex](https://www.pokemon.com/br/pokedex) | name, number, height, weight, ability, category, type, image |
| `pokestats` | `BoardGames/spiders/pokestats.py` | [pokemondb.net/pokedex/all](https://pokemondb.net/pokedex/all) | base / min / max for HP, Attack, Defense, Sp. Atk, Sp. Def, Speed |

`pokedex` rewrites `/us/` links to `/br/` before the detail request.

Each spider appends a CSV as it goes (`pokedex.csv`, `pokestats.csv`, with a header). `BoardGames/pipelines.py` upserts the same rows into `pokedex.sqlite`, tables `pokedex` and `pokestats`, keyed by Pokédex number.

The same shape shows up in recon: list a surface, follow every link, store a schema you can query. This one happens to be Pokémon.

## Run

```powershell
pip install -r requirements.txt
scrapy crawl pokedex
scrapy crawl pokestats
```

JSON instead of relying on the CSV, if you only want a file:

```powershell
scrapy crawl pokedex -O pokedex.json
scrapy crawl pokestats -O pokestats.json
```

Dashboard built on the extract: [Power BI](https://app.powerbi.com/view?r=eyJrIjoiYWQyZGVjMTYtNTlmNy00YjIxLTlmZmMtZWE0NzcxNmQ5MGRjIiwidCI6IjBkMzc1MDk0LWMzODctNDU1Zi1hZTg3LTRjYjJjMzE5ZTcwMCJ9&pageName=ReportSection18f103e5bd4dda82e072)

`BoardGames/` is the Scrapy project directory (`scrapy.cfg` points at it). `items.py` and `middlewares.py` are the unused Scrapy defaults.
