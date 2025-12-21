import pandas as pd
import numpy as np

# Load the data
input_file = 'WDI_Dataset/WDI_G20_2003-2023.csv'
try:
    df = pd.read_csv(input_file)
except FileNotFoundError:
    print(f"Error: {input_file} not found. Please run extract_wdi.py first.")
    exit(1)

# Identify year columns (digits only)
year_cols = [col for col in df.columns if col.isdigit()]

# Convert to long format
df_long = df.melt(
    id_vars=['CountryCode', 'CountryName', 'IndicatorName', 'OriginalIndicatorName'],
    value_vars=year_cols,
    var_name='Year',
    value_name='Value'
)

# Convert Year to integer
df_long['Year'] = df_long['Year'].astype(int)

# Add Zone mapping based on IndicatorName
zone_map = {
    'Life_Expectancy': 'Health', 
    'Infant_Mortality': 'Health', 
    'Maternal_Mortality': 'Health',
    
    'GDP_Current_USD': 'Economy', 
    'GDP_Per_Capita_PPP': 'Economy', 
    'Unemployment_Rate': 'Economy', 
    'Trade_Pct_GDP': 'Economy',
    
    'Forest_Area_Pct': 'Environment', 
    'Renewable_Energy_Pct': 'Environment',
    
    'Electricity_Access_Pct': 'Infrastructure', 
    'Internet_Users_Pct': 'Infrastructure', 
    'Mobile_Subscriptions_Per100': 'Infrastructure',
    
    'Primary_Enrollment_Pct': 'Education', 
    'Secondary_Enrollment_Pct': 'Education',
    
    'Population_Total': 'Demographics', 
    'Urban_Population_Pct': 'Demographics'
}

df_long['Zone'] = df_long['IndicatorName'].map(zone_map)

# Save to CSV
output_file = 'WDI_Dataset/WDI_G20_2003-2023_long.csv'
df_long.to_csv(output_file, index=False)
print(f"Converted {input_file} to long format and saved to {output_file}")
print(f"Rows: {len(df_long)}")
print(f"Columns: {df_long.columns.tolist()}")
