import pandas as pd
from pathlib import Path

class CSVActor:
    def __init__(self, csv_path="data/prices.csv"):
        if not Path(csv_path).exists():
            demo = pd.DataFrame({
                "product":["Widget A","Widget B","Gadget X","Service: Analysis"],
                "price":[19.99,29.99,149.0,500.0],
                "currency":["USD"]*4
            })
            demo.to_csv(csv_path, index=False)
        self.df = pd.read_csv(csv_path)

    def lookup(self, query):
        q = query.lower()
        hits = self.df[self.df["product"].str.lower().str.contains(q, na=False)]
        if hits.empty: return {}
        return hits.iloc[0].to_dict()
