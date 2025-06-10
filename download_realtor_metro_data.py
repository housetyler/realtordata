import requests
import os

# Direct URL to Realtor.com metro-level CSV
CSV_URL = "https://econdata.s3-us-west-2.amazonaws.com/Reports/Core/RDC_Inventory_Core_Metrics_Metro_History.csv"

# Fixed filename (no date)
filename = "realtor_metro_data.csv"

# Save path
output_dir = "data"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, filename)

# Download
response = requests.get(CSV_URL)
if response.status_code == 200:
    with open(output_path, 'wb') as f:
        f.write(response.content)
    print(f"✅ File saved to {output_path}")
else:
    print(f"❌ Failed to download. HTTP {response.status_code}")

