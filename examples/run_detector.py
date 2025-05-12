import os
import pandas as pd
from sentinel_ai.bias import BiasScanner

# Hole den Pfad zum aktuellen Ordner (examples/)
base_dir = os.path.dirname(__file__)
csv_path = os.path.join(base_dir, "bias_examples.csv")

# Lade die Datei
df = pd.read_csv(csv_path)

# Scan ausführen
scanner = BiasScanner()
results = scanner.scan_many(df["text"].tolist())

# Ausgabe
for i, res in enumerate(results):
    print(f"Text {i+1}: {res['summary']} (Toxicity: {res['toxicity_score']:.2f})")
