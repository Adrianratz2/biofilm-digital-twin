import os
import pandas as pd
from datetime import datetime

INPUT_DIR = "data/input"
OUTPUT_DIR = "results/output"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def digital_twin_predict(df):
    """
    Placeholder for GRNN prediction.
    Replace with real GRNN inference.
    """
    df["predicted_gene_expression"] = df["Pi_uM"] * 0.03
    df["biofilm_risk"] = 1 / (1 + (df["Pi_uM"] / 50))
    return df

for file in os.listdir(INPUT_DIR):
    if not file.endswith(".csv"):
        continue

    input_path = os.path.join(INPUT_DIR, file)
    output_file = file.replace(".csv", "_predicted.csv")
    output_path = os.path.join(OUTPUT_DIR, output_file)

    # Skip if already processed
    if os.path.exists(output_path):
        continue

    print(f"Processing {file}")

    df = pd.read_csv(input_path)
    result = digital_twin_predict(df)

    result["timestamp"] = datetime.utcnow().isoformat()
    result.to_csv(output_path, index=False)

    print(f"Saved {output_file}")
