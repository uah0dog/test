import pandas as pd
import numpy as np

# Load the data
df = pd.read_csv('WDI_Dataset/WDI_G20_2010-2024.csv')

# Rename duplicate columns
# Original: Country,series,Country,Series,2010...2024
new_cols = ['CountryCode', 'IndicatorCode', 'CountryName', 'IndicatorName'] + [str(y) for y in range(2010, 2025)]
df.columns = new_cols

# Convert to long format
df_long = df.melt(
    id_vars=['CountryCode', 'CountryName', 'IndicatorCode', 'IndicatorName'],
    var_name='Year',
    value_name='Value'
)

# Convert Year to integer
df_long['Year'] = df_long['Year'].astype(int)

# Add Zone mapping
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
df_long['Zone'] = df_long['IndicatorCode'].map(zone_map)

# Save to CSV
df_long.to_csv('WDI_Dataset/WDI_G20_2010-2024_long.csv', index=False)
print("Converted to long format and saved to WDI_Dataset/WDI_G20_2010-2024_long.csv")
