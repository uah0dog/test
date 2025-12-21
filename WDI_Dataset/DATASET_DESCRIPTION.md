# WDI G20 Dataset Description

## Dataset Overview

**File**: `WDI_G20_2003-2023.csv`
**Location**: `WDI_Dataset/`
**Extraction Date**: 2025-12-21
**Source**: World Bank World Development Indicators (WDI) via wbgapi
**File Size**: ~90 KB
**Format**: Wide-format CSV

## Purpose

This dataset provides a clean, representative subset of World Bank development indicators for testing thematic dashboards and multi-zone visualization systems. It balances comprehensive thematic coverage with manageable data size.

## Data Structure

### Dimensions
- **Rows**: 304 (17 indicators × 19 countries, excluding header)
- **Columns**: 26 total
  - 5 metadata columns (CountryCode, CountryName, IndicatorCode, IndicatorName, OriginalIndicatorName)
  - 21 year columns (2003-2023)

### Schema

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| `CountryCode` | string | ISO 3166-1 alpha-3 country code | USA, GBR, CHN |
| `CountryName` | string | Full country name | United States |
| `IndicatorCode` | string | WDI indicator code | SP.DYN.LE00.IN |
| `IndicatorName` | string | Simplified human-readable indicator name | Life_Expectancy |
| `OriginalIndicatorName` | string | Full indicator description | Life expectancy at birth, total (years) |
| `2003`-`2023` | float | Annual values for each year | 77.04, 78.45, etc. |

### Data Format
- **Type**: Wide format (years as columns)
- **Missing Values**: Represented as empty cells or NaN
- **Numeric Precision**: Float64 with varying decimal places depending on indicator

## Indicators Included

### Zone 1: Health (3 indicators)

| Code | Name | Coverage | Unit | Simplified Name |
|------|------|----------|------|-----------------|
| `SP.DYN.LE00.IN` | Life expectancy at birth | Excellent (99%+) | Years | Life_Expectancy |
| `SP.DYN.IMRT.IN` | Infant mortality rate | Excellent (99%+) | Per 1,000 live births | Infant_Mortality |
| `SH.STA.MMRT` | Maternal mortality ratio | Good (95%+) | Per 100,000 births | Maternal_Mortality |

### Zone 2: Economy (4 indicators)

| Code | Name | Coverage | Unit | Simplified Name |
|------|------|----------|------|-----------------|
| `NY.GDP.MKTP.CD` | GDP (current US$) | Excellent (99%+) | Current USD | GDP_Current_USD |
| `NY.GDP.PCAP.PP.CD` | GDP per capita, PPP | Excellent (99%+) | International $ | GDP_Per_Capita_PPP |
| `SL.UEM.TOTL.ZS` | Unemployment rate | Excellent (99%+) | % of labor force | Unemployment_Rate |
| `NE.TRD.GNFS.ZS` | Trade (% of GDP) | Excellent (99%+) | % of GDP | Trade_Pct_GDP |

### Zone 3: Environment (2 indicators)

| Code | Name | Coverage | Unit | Simplified Name |
|------|------|----------|------|-----------------|
| `AG.LND.FRST.ZS` | Forest area | Good (95%+) | % of land area | Forest_Area_Pct |
| `EG.FEC.RNEW.ZS` | Renewable energy consumption | Good (95%+) | % of total | Renewable_Energy_Pct |

### Zone 4: Infrastructure (3 indicators)

| Code | Name | Coverage | Unit | Simplified Name |
|------|------|----------|------|-----------------|
| `EG.ELC.ACCS.ZS` | Access to electricity | Excellent (99%+) | % of population | Electricity_Access_Pct |
| `IT.NET.USER.ZS` | Internet users | Excellent (99%+) | % of population | Internet_Users_Pct |
| `IT.CEL.SETS.P2` | Mobile subscriptions | Excellent (99%+) | Per 100 people | Mobile_Subscriptions_Per100 |

### Zone 5: Education (2 indicators)

| Code | Name | Coverage | Unit | Simplified Name |
|------|------|----------|------|-----------------|
| `SE.PRM.ENRR` | Primary school enrollment | Excellent (99%+) | % gross | Primary_Enrollment_Pct |
| `SE.SEC.ENRR` | Secondary school enrollment | Excellent (99%+) | % gross | Secondary_Enrollment_Pct |

### Zone 6: Demographics (2 indicators)

| Code | Name | Coverage | Unit | Simplified Name |
|------|------|----------|------|-----------------|
| `SP.POP.TOTL` | Total population | Excellent (100%) | Count | Population_Total |
| `SP.URB.TOTL.IN.ZS` | Urban population | Excellent (99%+) | % of total | Urban_Population_Pct |

## Countries Covered

### G20 Economies (19 countries)

| Code | Country | Region | Income Group |
|------|---------|--------|--------------|
| ARG | Argentina | Latin America & Caribbean | Upper middle income |
| AUS | Australia | East Asia & Pacific | High income |
| BRA | Brazil | Latin America & Caribbean | Upper middle income |
| CAN | Canada | North America | High income |
| CHN | China | East Asia & Pacific | Upper middle income |
| FRA | France | Europe & Central Asia | High income |
| DEU | Germany | Europe & Central Asia | High income |
| IND | India | South Asia | Lower middle income |
| IDN | Indonesia | East Asia & Pacific | Lower middle income |
| ITA | Italy | Europe & Central Asia | High income |
| JPN | Japan | East Asia & Pacific | High income |
| KOR | South Korea (Korea, Rep.) | East Asia & Pacific | High income |
| MEX | Mexico | Latin America & Caribbean | Upper middle income |
| RUS | Russian Federation | Europe & Central Asia | Upper middle income |
| SAU | Saudi Arabia | Middle East & North Africa | High income |
| ZAF | South Africa | Sub-Saharan Africa | Upper middle income |
| TUR | Turkey (Türkiye) | Europe & Central Asia | Upper middle income |
| GBR | United Kingdom | Europe & Central Asia | High income |
| USA | United States | North America | High income |

**Coverage Rationale**: G20 countries ensure high data quality and completeness across all indicators while representing diverse geographic regions, income levels, and development contexts.

## Temporal Coverage

### Year Range: 2003-2023 (21 years)

## Data Quality Notes

### Missing Data Patterns

1. **Recent Years (2022-2023)**: Expected lag as countries finalize statistics.
2. **Indicator-Specific Gaps**:
   - Maternal mortality: Survey-dependent.
   - Renewable energy: Some gaps in earlier years.
   - Education enrollment: Generally complete.

3. **Country-Specific Gaps**:
   - Russia: Some indicators affected by geopolitical factors.
   - Saudi Arabia: Historically limited transparency in certain indicators.

### Known Issues

1. **Missing CO2 Emissions Indicator**:
   - `EN.ATM.CO2E.PC` was requested but not returned by API.
   - **Recommendation**: Check for alternative codes or use CAIT/EDGAR datasets.

2. **Duplicate Column Names (Mitigated)**:
   - Extraction script now handles duplicates and ensures unique, descriptive column names (`CountryName`, `CountryCode`, `IndicatorName`).

## Usage Guidelines

### Loading the Data

**Python (pandas)**:
```python
import pandas as pd

# Load data
df = pd.read_csv('WDI_Dataset/WDI_G20_2003-2023.csv')

# Convert to long format for visualization (or use the pre-generated long file)
# The pre-generated long file is 'WDI_Dataset/WDI_G20_2003-2023_long.csv'
```

### Recommended Transformations

1. **Long Format Conversion**: The dataset comes with a `convert_to_long.py` script to generate a long-format CSV suitable for visualization tools like Vega-Lite. This file (`WDI_G20_2003-2023_long.csv`) includes a `Zone` column for thematic filtering.

2. **Zone Tagging**: The conversion script adds a "Zone" column (Health, Economy, Environment, Infrastructure, Education, Demographics) to enable thematic grouping.

## Dataset Provenance

### Extraction Details

- **Tool**: `wbgapi` (World Bank API Python library)
- **Script**: `extract_wdi.py`
- **API Version**: World Bank API v2
- **Extraction Command**: `uv run WDI_Dataset/extract_wdi.py`
- **Runtime**: ~15 seconds
- **Dependencies**: wbgapi, pandas

### Reproducibility

To reproduce:
```bash
uv run WDI_Dataset/extract_wdi.py
uv run WDI_Dataset/convert_to_long.py
```
