# WDI G20 Dataset Description

## Dataset Overview

**File**: `WDI_G20_2010-2024.csv`
**Location**: `/home/felladog/Desktop/LabUAH/BMC_spec/WDI_Dataset/`
**Extraction Date**: 2025-12-21
**Source**: World Bank World Development Indicators (WDI) via wbgapi
**File Size**: 70 KB
**Format**: Wide-format CSV

## Purpose

This dataset provides a clean, representative subset of World Bank development indicators for testing thematic dashboards and multi-zone visualization systems. It balances comprehensive thematic coverage with manageable data size.

## Data Structure

### Dimensions
- **Rows**: 304 (17 indicators × 19 countries, excluding header)
- **Columns**: 19 total
  - 4 metadata columns (Country code, series code, Country name, Series name)
  - 15 year columns (2010-2024)

### Schema

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| `Country` (code) | string | ISO 3166-1 alpha-3 country code | USA, GBR, CHN |
| `series` | string | WDI indicator code (CETS format) | SP.DYN.LE00.IN |
| `Country` (name) | string | Full country name | United States |
| `Series` | string | Full indicator description | Life expectancy at birth, total (years) |
| `2010`-`2024` | float | Annual values for each year | 78.54, 80.40, etc. |

### Data Format
- **Type**: Wide format (years as columns)
- **Missing Values**: Represented as empty cells or NaN
- **Numeric Precision**: Float64 with varying decimal places depending on indicator

## Indicators Included

### Zone 1: Health (3 indicators)

| Code | Name | Coverage | Unit |
|------|------|----------|------|
| `SP.DYN.LE00.IN` | Life expectancy at birth | Excellent (99%+) | Years |
| `SP.DYN.IMRT.IN` | Infant mortality rate | Excellent (99%+) | Per 1,000 live births |
| `SH.STA.MMRT` | Maternal mortality ratio | Good (95%+) | Per 100,000 births |

### Zone 2: Economy (4 indicators)

| Code | Name | Coverage | Unit |
|------|------|----------|------|
| `NY.GDP.MKTP.CD` | GDP (current US$) | Excellent (99%+) | Current USD |
| `NY.GDP.PCAP.PP.CD` | GDP per capita, PPP | Excellent (99%+) | International $ |
| `SL.UEM.TOTL.ZS` | Unemployment rate | Excellent (99%+) | % of labor force |
| `NE.TRD.GNFS.ZS` | Trade (% of GDP) | Excellent (99%+) | % of GDP |

### Zone 3: Environment (2 indicators)

| Code | Name | Coverage | Unit |
|------|------|----------|------|
| `AG.LND.FRST.ZS` | Forest area | Good (95%+) | % of land area |
| `EG.FEC.RNEW.ZS` | Renewable energy consumption | Good (95%+) | % of total |

### Zone 4: Infrastructure (3 indicators)

| Code | Name | Coverage | Unit |
|------|------|----------|------|
| `EG.ELC.ACCS.ZS` | Access to electricity | Excellent (99%+) | % of population |
| `IT.NET.USER.ZS` | Internet users | Excellent (99%+) | % of population |
| `IT.CEL.SETS.P2` | Mobile subscriptions | Excellent (99%+) | Per 100 people |

### Zone 5: Education (2 indicators)

| Code | Name | Coverage | Unit |
|------|------|----------|------|
| `SE.PRM.ENRR` | Primary school enrollment | Excellent (99%+) | % gross |
| `SE.SEC.ENRR` | Secondary school enrollment | Excellent (99%+) | % gross |

### Zone 6: Demographics (2 indicators)

| Code | Name | Coverage | Unit |
|------|------|----------|------|
| `SP.POP.TOTL` | Total population | Excellent (100%) | Count |
| `SP.URB.TOTL.IN.ZS` | Urban population | Excellent (99%+) | % of total |

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

### Year Range: 2010-2024 (15 years)

### Data Completeness by Year

| Year | Non-Null Values | Completeness |
|------|----------------|--------------|
| 2010 | 294/304 | 96.7% |
| 2011 | 296/304 | 97.4% |
| 2012 | 298/304 | 98.0% |
| 2013 | 301/304 | 99.0% |
| 2014 | 302/304 | 99.3% |
| 2015 | 303/304 | 99.7% |
| 2016 | 302/304 | 99.3% |
| 2017 | 303/304 | 99.7% |
| 2018 | 303/304 | 99.7% |
| 2019 | 303/304 | 99.7% |
| 2020 | 303/304 | 99.7% |
| 2021 | 302/304 | 99.3% |
| 2022 | 284/304 | 93.4% |
| 2023 | 275/304 | 90.5% |
| 2024 | 132/304 | 43.4% |

**Coverage Patterns**:
- **2013-2021**: Peak data availability (99%+ completeness)
- **2010-2012**: Slightly lower but still excellent (96-98%)
- **2022-2023**: Good coverage but declining as recent data is finalized (90-93%)
- **2024**: Partial coverage (43%) - data collection in progress

## Data Quality Notes

### Missing Data Patterns

1. **Recent Years (2022-2024)**: Expected lag as countries finalize statistics
   - National accounts: Usually complete within 12 months
   - Health/education: 18-24 month lag common
   - Environmental: Can lag 24-36 months

2. **Indicator-Specific Gaps**:
   - Maternal mortality: Survey-dependent, some gaps in 2010-2012
   - Renewable energy: Some gaps in early years (2010-2012)
   - Education enrollment: Generally complete across all years

3. **Country-Specific Gaps**:
   - Russia: Some indicators affected by geopolitical factors post-2020
   - Saudi Arabia: Historically limited transparency in certain indicators

### Known Issues

1. **Missing CO2 Emissions Indicator**:
   - `EN.ATM.CO2E.PC` was requested but not returned by API
   - Possible causes: API restrictions, indicator code changes, or data embargo
   - **Recommendation**: Check for alternative codes or use CAIT/EDGAR datasets

2. **Duplicate Column Names**:
   - Both country code and country name columns labeled "Country"
   - Both indicator code and indicator name columns labeled differently
   - **Recommendation**: Rename columns when loading for analysis

3. **2024 Data Availability**:
   - Only 43% complete as of extraction date (Dec 2025)
   - Most missing values are expected and will be filled throughout 2025-2026
   - **Recommendation**: Focus analysis on 2010-2023 for complete time series

## Usage Guidelines

### Loading the Data

**Python (pandas)**:
```python
import pandas as pd

# Load data
df = pd.read_csv('WDI_G20_2010-2024.csv')

# Rename duplicate columns for clarity
df.columns = ['country_code', 'indicator_code', 'country_name',
              'indicator_name'] + [str(y) for y in range(2010, 2025)]

# Convert to long format for visualization
df_long = df.melt(
    id_vars=['country_code', 'country_name', 'indicator_code', 'indicator_name'],
    var_name='year',
    value_name='value'
)
df_long['year'] = df_long['year'].astype(int)
```

**R (tidyverse)**:
```r
library(tidyverse)

# Load data
df <- read_csv('WDI_G20_2010-2024.csv')

# Rename columns
colnames(df) <- c('country_code', 'indicator_code', 'country_name',
                  'indicator_name', paste0('y', 2010:2024))

# Convert to long format
df_long <- df %>%
  pivot_longer(
    cols = starts_with('y'),
    names_to = 'year',
    values_to = 'value',
    names_prefix = 'y'
  ) %>%
  mutate(year = as.integer(year))
```

### Recommended Transformations

1. **Long Format Conversion**: Most visualization tools (Vega-Lite, ggplot2, Tableau) work better with long format where each row is one observation (country-indicator-year combination).

2. **Column Renaming**: Address duplicate column names for clarity.

3. **Year Filtering**: Focus on 2010-2023 for complete time series analysis, or 2013-2021 for maximum completeness.

4. **Missing Value Handling**:
   - **Linear interpolation**: Suitable for stable indicators (forest area, infrastructure)
   - **Median imputation**: Use regional/income-group medians for sparse data
   - **Explicit exclusion**: Remove rows with missing values for critical analyses

5. **Zone Tagging**: Add a "zone" column to enable thematic filtering:
   ```python
   zone_map = {
       'SP.DYN.LE00.IN': 'Health', 'SP.DYN.IMRT.IN': 'Health', 'SH.STA.MMRT': 'Health',
       'NY.GDP.MKTP.CD': 'Economy', 'NY.GDP.PCAP.PP.CD': 'Economy',
       'SL.UEM.TOTL.ZS': 'Economy', 'NE.TRD.GNFS.ZS': 'Economy',
       'AG.LND.FRST.ZS': 'Environment', 'EG.FEC.RNEW.ZS': 'Environment',
       'EG.ELC.ACCS.ZS': 'Infrastructure', 'IT.NET.USER.ZS': 'Infrastructure',
       'IT.CEL.SETS.P2': 'Infrastructure',
       'SE.PRM.ENRR': 'Education', 'SE.SEC.ENRR': 'Education',
       'SP.POP.TOTL': 'Demographics', 'SP.URB.TOTL.IN.ZS': 'Demographics'
   }
   df_long['zone'] = df_long['indicator_code'].map(zone_map)
   ```

### Visualization Recommendations

**Suitable Chart Types by Indicator**:

- **Time Series (Line Charts)**: All indicators, especially for tracking trends
- **Choropleth Maps**: Percentage indicators (urbanization, internet access, enrollment)
- **Bar Charts**: Comparing countries within a year, especially GDP and population
- **Scatter Plots**: Correlation analysis (GDP per capita vs. life expectancy)
- **Small Multiples**: Comparing indicators across zones
- **Treemaps**: Hierarchical data (population, GDP)

**Multi-Zone Dashboard Examples**:

1. **Development Overview**: Life expectancy + GDP per capita + internet users (health + economy + infrastructure)
2. **Sustainability Monitor**: Forest area + renewable energy + urban population (environment + demographics)
3. **Education Access**: Primary enrollment + secondary enrollment + internet users (education + infrastructure)

## Dataset Provenance

### Extraction Details

- **Tool**: `wbgapi` (World Bank API Python library)
- **Script**: `extract_wdi.py`
- **API Version**: World Bank API v2
- **Extraction Command**: `uv run --with wbgapi --with pandas extract_wdi.py`
- **Runtime**: ~15 seconds
- **Dependencies**: wbgapi, pandas, numpy

### Reproducibility

The dataset can be regenerated using the included `extract_wdi.py` script. Note that values may differ slightly if extracted at a later date due to:
- Data revisions by national statistical offices
- Corrections by World Bank data team
- Updated methodologies for calculated indicators

To reproduce:
```bash
cd WDI_Dataset
uv run --with wbgapi --with pandas extract_wdi.py
```

## Limitations

1. **Coverage**: Limited to G20 countries only (19 of 217+ economies in WDI)
2. **Indicators**: 17 of 1,400+ available indicators (highly selective)
3. **Timeframe**: 2010-2024 only (excludes historical trends pre-2010)
4. **Missing Environment Zone Indicator**: CO2 emissions not available
5. **Data Lag**: Recent years (2022-2024) have incomplete data
6. **Aggregation**: No regional/income-group aggregates included

## Recommended Extensions

### To Expand Coverage

1. **Add More Countries**: Include regional representatives beyond G20
   ```python
   additional_countries = ['NGA', 'KEN', 'VNM', 'PHL', 'EGY', 'PAK']
   ```

2. **Add Missing CO2 Indicator**: Use alternative sources or codes
   - Try `EN.ATM.CO2E.KT` (total CO2 in kilotons) and calculate per capita
   - Use CAIT Climate Data Explorer or EDGAR datasets
   - Check if indicator code has been updated

3. **Extend Timeframe**: Include 2000-2009 for longer trend analysis
   ```python
   range(2000, 2025)
   ```

4. **Add More Indicators**: Expand zones or add new ones
   - **Governance**: `CC.EST` (Control of Corruption), `GE.EST` (Government Effectiveness)
   - **Gender**: `SG.GEN.PARL.ZS` (Women in parliament), `SE.ENR.PRSC.FM.ZS` (Gender parity in education)
   - **Innovation**: `GB.XPD.RSDV.GD.ZS` (R&D expenditure), `IP.PAT.RESD` (Patent applications)

5. **Add Metadata Columns**: Region, income group, lending category from `WDI_Country.csv`

## References

- **World Bank Data Catalog**: https://datacatalog.worldbank.org/
- **WDI Database**: https://databank.worldbank.org/source/world-development-indicators
- **API Documentation**: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589
- **wbgapi Documentation**: https://github.com/tgherzog/wbgapi
- **Indicator Methodology**: https://datatopics.worldbank.org/world-development-indicators/

## Change Log

### 2025-12-21 - Initial Extraction
- Created dataset with 17 indicators, 19 G20 countries, 2010-2024
- Identified missing CO2 emissions indicator
- Documented data quality patterns and usage guidelines
