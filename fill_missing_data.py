import pandas as pd
import geocoder

# Load the dataset
ufo_df = pd.read_csv("data/ufo_data/ufo-sightings-transformed.csv")

def get_country(lat, lon):
    g = geocoder.osm([lat, lon], method='reverse')
    if g.ok:
        return g.country, g.country_code
    return None, None

# Fill missing Country and Country_Code using latitude and longitude
for index, row in ufo_df.iterrows():
    if pd.isnull(row['Country']) or pd.isnull(row['Country_Code']):
        country, country_code = get_country(row['latitude'], row['longitude'])
        if country:
            ufo_df.at[index, 'Country'] = country
        if country_code:
            ufo_df.at[index, 'Country_Code'] = country_code

# Save the updated dataset
#ufo_df.to_csv("data/ufo_data/updated_ufo_sightings.csv", index=False)

print("Country and Country_Code filled in successfully.")
