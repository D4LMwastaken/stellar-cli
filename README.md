# Stellar CLI

A command line utility for exploring and analyzing star catalogs.

## Features

- **Data Loading:** Efficiently ingest JSON-based star catalogs.
- **Filtering:** Filter star data by magnitude to focus on specific brightness levels.
- **Sorting:** Easily organize star catalogs by name or magnitude using built-in sorting logic.
- **Terminal Visualization:** Render clean, easy-to-read ASCII tables directly in your terminal.


## Installation & Setup

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd stellar-cli
   ```

2. Set up the environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

## Usage

```bash
# Run the tool with a star catalog
python3 -m src.main --file data/stars.json

# Filter by magnitude
python3 -m src.main --file data/stars.json --max-mag 0

# Sort by name
python3 -m src.main --file data/stars.json --sort name
```

## Developer Commands

I am testing `make` for development:

- `make test`: Runs the full test suite using `pytest`.
- `make run`: Executes the CLI tool with sample data.

---
*Built by D4LM for Stardance*