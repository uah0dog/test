import pandas as pd

input_file = 'LA_CrimeDataset/Crime_Data_from_2023_to_Present.csv'
output_file = 'LA_CrimeDataset/Crime_Data_from_2023_to_Present_compressed.csv'

columns_to_keep = [
    'DR_NO', 'Date Rptd', 'DATE OCC', 'TIME OCC', 'AREA', 'Rpt Dist No', 'Part 1-2',
    'Crm Cd', 'Crm Cd Desc', 'Vict Age', 'Vict Sex', 'Vict Descent', 'Premis Cd',
    'Premis Desc', 'Weapon Used Cd', 'Weapon Desc', 'Status', 'LOCATION', 'LAT', 'LON', 'Crm Cd 1'
]

try:
    df = pd.read_csv(input_file)
    df_compressed = df[columns_to_keep]
    df_compressed.to_csv(output_file, index=False)
    print(f"Successfully compressed '{input_file}' to '{output_file}'")
except FileNotFoundError:
    print(f"Error: Input file '{input_file}' not found.")
except KeyError as e:
    print(f"Error: One or more specified columns not found in the input file: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
