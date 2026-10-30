# Data

Monthly records from two Met Office long-running UK stations, downloaded on **29 October 2026** and kept here as a fixed snapshot. The notebooks always read these files, never the live versions: the Met Office updates the live files every month and revises provisional values, so results computed from them would drift.

| File | Station | Source | Records | SHA-256 |
|---|---|---|---|---|
| `raw/oxforddata.txt` | Oxford | [oxforddata.txt](https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/oxforddata.txt) | January 1853 to September 2026 | `7bd7f15c624736b0685c6c4ee1e2442f6805544f9b68de58981ff2f137b4d7e3` |
| `raw/lerwickdata.txt` | Lerwick, Shetland | [lerwickdata.txt](https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/lerwickdata.txt) | December 1930 to September 2026 | `305a960d42bffef4c00f29af4e8680f6ce6d7f895698595179aa2bb2af5603c3` |

Both come from the Met Office [historic station data](https://www.metoffice.gov.uk/research/climate/maps-and-data/historic-station-data) page.

To check a file has not changed:

```bash
shasum -a 256 data/raw/*.txt        # Windows: certutil -hashfile data\raw\oxforddata.txt SHA256
```

## Columns

| Column | Meaning | Units |
|---|---|---|
| `yyyy` | Year | |
| `mm` | Month | 1 to 12 |
| `tmax` | Mean daily maximum temperature | °C |
| `tmin` | Mean daily minimum temperature | °C |
| `af` | Days of air frost | days |
| `rain` | Total rainfall | mm |
| `sun` | Total sunshine | hours |

## Markers in the raw files

These are deliberate teaching material; the notebooks handle each one.

| Marker | Meaning | Where |
|---|---|---|
| `---` | Missing (more than 2 days missing in the month) | Oxford sunshine 1853 to 1928; Oxford `tmin` and `af` for December 1860 |
| `*` after a value | Estimated | Both stations, including every Oxford temperature, frost and sunshine value for 2026 |
| `#` after a sunshine value | Automatic Kipp & Zonen sensor rather than a Campbell Stokes recorder | Lerwick from 2008; never Oxford |
| `Provisional` at the end of a row | Not yet quality-controlled; may be revised | January to September 2026 at both stations |

The files have five lines of free text, a row of column names and a row of units before the data, and use Windows (CRLF) line endings. `.gitattributes` stops git from changing them.

## Licence

Contains public sector information licensed under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/). Source: Met Office.
