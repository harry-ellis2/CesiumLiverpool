import geopandas as gpd # type: ignore
from pathlib import Path
import pandas as pd # type: ignore
from tqdm import tqdm # type: ignore


# Paths
input_folder = Path("resources_raw")
output_folder = Path("resources")
output_folder.mkdir(exist_ok=True)

# Load Liverpool and Wirral ward boundaries
liverpool_wards = gpd.read_file(input_folder / "Westminster_Wards_Liverpool.json")
wirral_wards = gpd.read_file(input_folder / "Westminster_Wards_Wirral.json")

# Set CRS if missing (most GeoJSONs are EPSG:4326)
if liverpool_wards.crs is None:
    liverpool_wards = liverpool_wards.set_crs("EPSG:4326")
if wirral_wards.crs is None:
    wirral_wards = wirral_wards.set_crs("EPSG:4326")

# Combine both into one GeoDataFrame
combined = gpd.GeoDataFrame(pd.concat([liverpool_wards, wirral_wards], ignore_index=True), crs=liverpool_wards.crs)

# Optional: buffer around combined area (e.g., 5 km = 5000 m)
# This part is correct: buffer in a projected CRS (meters)
combined_buffer = combined.to_crs(epsg=27700).buffer(5000)  
combined_buffer = gpd.GeoDataFrame(geometry=combined_buffer, crs="EPSG:27700")

# Process each UK GeoJSON file
# Using tqdm.glob for a progress bar
for geojson_file in tqdm(input_folder.glob("*.geojson")):
    if geojson_file.name in ["Westminster_Wards_Liverpool.json", "Westminster_Wards_Wirral.json"]:
        continue  # skip ward files themselves
    print(f"Processing {geojson_file.name}...")
    
    uk = gpd.read_file(geojson_file)
    if uk.crs is None:
        uk = uk.set_crs("EPSG:4326")
    
    # Correct: convert to 27700 for clipping
    uk = uk.to_crs("EPSG:27700")
    
    # Correct: clip in 27700
    clipped = gpd.clip(uk, combined_buffer)
    
    # --- THE FIX ---
    # Convert the final result back to 4326 for web compatibility
    clipped_web = clipped.to_crs("EPSG:4326")
    
    output_file = output_folder / geojson_file.name
    
    # Save the 4326 (web-friendly) version
    clipped_web.to_file(output_file, driver="GeoJSON")

print("All files processed!")