#!/usr/bin/env python3
"""
WDI Data Extraction Script
Extracts 18 core indicators for G20 countries (2003-2023)
"""

import wbgapi as wb
import pandas as pd
from pathlib import Path

# Configuration
OUTPUT_FILE = "WDI_Dataset/WDI_G20_2003-2023.csv"

# 18 recommended indicators across 6 thematic zones
INDICATORS = [
    # Zone 1: Health (3 indicators)
    'SP.DYN.LE00.IN',      # Life expectancy at birth
    'SP.DYN.IMRT.IN',      # Infant mortality rate
    'SH.STA.MMRT',         # Maternal mortality ratio

    # Zone 2: Economy (4 indicators)
    'NY.GDP.MKTP.CD',      # GDP (current US$)
    'NY.GDP.PCAP.PP.CD',   # GDP per capita, PPP
    'SL.UEM.TOTL.ZS',      # Unemployment rate
    'NE.TRD.GNFS.ZS',      # Trade (% of GDP)

    # Zone 3: Environment (3 indicators)
    'EN.ATM.CO2E.PC',      # CO2 emissions per capita
    'AG.LND.FRST.ZS',      # Forest area (% of land)
    'EG.FEC.RNEW.ZS',      # Renewable energy consumption

    # Zone 4: Infrastructure (3 indicators)
    'EG.ELC.ACCS.ZS',      # Access to electricity
    'IT.NET.USER.ZS',      # Internet users
    'IT.CEL.SETS.P2',      # Mobile subscriptions

    # Zone 5: Education (2 indicators)
    'SE.PRM.ENRR',         # Primary school enrollment
    'SE.SEC.ENRR',         # Secondary school enrollment

    # Zone 6: Demographics (2 indicators)
    'SP.POP.TOTL',         # Total population
    'SP.URB.TOTL.IN.ZS',   # Urban population (%)
]

# Human-readable column names
COLUMN_NAMES = {
    'SP.DYN.LE00.IN': 'Life_Expectancy',
    'SP.DYN.IMRT.IN': 'Infant_Mortality',
    'SH.STA.MMRT': 'Maternal_Mortality',
    'NY.GDP.MKTP.CD': 'GDP_Current_USD',
    'NY.GDP.PCAP.PP.CD': 'GDP_Per_Capita_PPP',
    'SL.UEM.TOTL.ZS': 'Unemployment_Rate',
    'NE.TRD.GNFS.ZS': 'Trade_Pct_GDP',
    'EN.ATM.CO2E.PC': 'CO2_Per_Capita',
    'AG.LND.FRST.ZS': 'Forest_Area_Pct',
    'EG.FEC.RNEW.ZS': 'Renewable_Energy_Pct',
    'EG.ELC.ACCS.ZS': 'Electricity_Access_Pct',
    'IT.NET.USER.ZS': 'Internet_Users_Pct',
    'IT.CEL.SETS.P2': 'Mobile_Subscriptions_Per100',
    'SE.PRM.ENRR': 'Primary_Enrollment_Pct',
    'SE.SEC.ENRR': 'Secondary_Enrollment_Pct',
    'SP.POP.TOTL': 'Population_Total',
    'SP.URB.TOTL.IN.ZS': 'Urban_Population_Pct',
}

# G20 countries (ISO 3166-1 alpha-3 codes)
G20_COUNTRIES = [
    'ARG',  # Argentina
    'AUS',  # Australia
    'BRA',  # Brazil
    'CAN',  # Canada
    'CHN',  # China
    'FRA',  # France
    'DEU',  # Germany
    'IND',  # India
    'IDN',  # Indonesia
    'ITA',  # Italy
    'JPN',  # Japan
    'KOR',  # South Korea
    'MEX',  # Mexico
    'RUS',  # Russia
    'SAU',  # Saudi Arabia
    'ZAF',  # South Africa
    'TUR',  # Turkey
    'GBR',  # United Kingdom
    'USA',  # United States
]

# Timeframe
START_YEAR = 2003
END_YEAR = 2023

def main():
    print("=" * 60)
    print("WDI Data Extraction")
    print("=" * 60)
    print(f"Indicators: {len(INDICATORS)}")
    print(f"Countries: {len(G20_COUNTRIES)}")
    print(f"Timeframe: {START_YEAR}-{END_YEAR}")
    print()

    try:
        print("Fetching data from World Bank API...")
        # Fetch data using wbgapi
        df = wb.data.DataFrame(
            INDICATORS,
            G20_COUNTRIES,
            range(START_YEAR, END_YEAR + 1),
            labels=True,
            numericTimeKeys=True
        )

        print(f"✓ Data fetched successfully: {df.shape}")

        # Reset index to make Country and Year explicit columns
        df = df.reset_index()

        # Rename indicator columns to human-readable names (for wide format if applicable)
        # Note: wb.data.DataFrame with numericTimeKeys=True returns years as columns
        
        # Create a new column with human-readable indicator names from the 'series' column
        if 'series' in df.columns:
            df['IndicatorName'] = df['series'].map(COLUMN_NAMES)
            # We keep 'series' for now as 'IndicatorCode' equivalent or rename it
        
        # Explicitly rename columns to be safe and unique
        cols = list(df.columns)
        new_cols = []
        seen_country = 0
        
        for col in cols:
            if col == 'economy':
                new_cols.append('CountryCode')
            elif col == 'Country': # wbgapi adds 'Country' as the name
                # If we encounter 'Country' and we haven't seen one, it might be code or name depending on version
                # But usually 'economy' is index->column.
                # Let's handle the standard output from wbgapi labels=True
                # It usually produces: index(economy), series, Country, Series (names)
                new_cols.append('CountryName')
            elif col == 'series':
                new_cols.append('IndicatorCode')
            elif col == 'Series':
                new_cols.append('OriginalIndicatorName')
            elif col == 'IndicatorName': # The one we added
                new_cols.append('IndicatorName')
            else:
                new_cols.append(str(col))
        
        df.columns = new_cols
        
        # Drop duplicates if any (e.g. if we have multiple indicator name columns)
        # Reorder to: CountryCode, CountryName, IndicatorCode, IndicatorName, OriginalIndicatorName, Years...
        
        base_cols = ['CountryCode', 'CountryName', 'IndicatorCode', 'IndicatorName', 'OriginalIndicatorName']
        # Filter to only existing base columns
        base_cols = [c for c in base_cols if c in df.columns]
        
        year_cols = [str(y) for y in range(START_YEAR, END_YEAR + 1)]
        
        final_cols = base_cols + year_cols
        
        # Select only valid columns
        df = df[[c for c in final_cols if c in df.columns]]

        # Save to CSV
        output_path = Path(OUTPUT_FILE)
        df.to_csv(output_path, index=False)

        file_size_mb = output_path.stat().st_size / (1024 * 1024)

        print()
        print("=" * 60)
        print("Extraction Complete")
        print("=" * 60)
        print(f"Output file: {output_path.absolute()}")
        print(f"File size: {file_size_mb:.2f} MB")
        print(f"Rows: {len(df):,}")
        print(f"Columns: {len(df.columns)}")
        print()
        print("Data preview:")
        print(df.head())
        print()
        print("Data info:")
        print(df.info())

    except Exception as e:
        print(f"✗ Error during extraction: {e}")
        raise

if __name__ == "__main__":
    main()
