# Equity Research Casebook

A portfolio-safe collection of three historical equity-research case studies
covering an A-share industrial company, a Hong Kong-listed medical-device
company, and a US semiconductor company.

The project demonstrates a repeatable workflow for combining price structure,
volatility, public filings, catalysts, and falsifiable monitoring conditions.
It intentionally excludes personal holdings, cost bases, account values, raw
broker exports, and individualized trade instructions.

## Case studies

| Market | Company | Research focus |
|---|---|---|
| China A-share | Baogang Steel (600010) | Cyclical recovery versus weak steel demand |
| Hong Kong | MicroPort NeuroTech (02172) | Fundamental improvement versus a weak price trend |
| United States | NVIDIA (NVDA) | Event risk, trend structure, and scenario monitoring |

The reports are dated research snapshots from July 2026. They are not current
recommendations and should not be read as evidence of future performance.

## Research workflow

```text
market snapshot + price history + public filings
                       |
             trend / volatility review
                       |
           catalyst and risk decomposition
                       |
          scenario conditions that can fail
                       |
        dated monitoring questions and caveats
```

Each public case study follows the same sequence:

1. State the dated market context.
2. Separate observed facts from interpretation.
3. Identify trend, volatility, and event-risk conditions.
4. Express conclusions as scenarios, not price certainties.
5. Document data and inference limitations.

## Repository layout

```text
reports/                  sanitized public case studies
docs/METHODOLOGY.md       analytical and privacy methodology
src/publication_guard.py  reusable publication-boundary scanner
scripts/check_publication.py
tests/                    tests for the privacy boundary
```

## Quality checks

```bash
python -m pip install -e '.[dev]'
ruff check .
pytest -q
python -m scripts.check_publication
```

The publication guard rejects original report exports and a deliberately
conservative set of personal-position phrases. It complements human review;
it does not prove that a document contains no sensitive information.

## Data and privacy boundary

- No broker credentials, account identifiers, position sizes, cost bases, or
  portfolio values are included.
- No raw Interactive Brokers exports or generated private HTML/JSON artifacts
  are included.
- Market observations are summarized as dated, derived research notes.
- Public-company claims link to public filings or investor-relations sources
  where available.
- Third-party market data remains subject to its provider's terms and is not
  redistributed here.

## Limitations

These reports are small historical case studies, not production investment
research. They do not include a live data pipeline, transaction-cost model,
formal valuation model, or statistically powered out-of-sample test. Technical
levels are descriptive scenario markers, not guaranteed execution prices.

## License

Code and original prose are released under the MIT License. Linked third-party
materials and data remain subject to their respective terms.
