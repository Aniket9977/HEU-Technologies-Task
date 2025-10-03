import pandas as pd
from pathlib import Path
import re

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
        q_lower = query.lower()
        
        best_match_product_name = None
        max_match_len = 0

        
        for product_name_from_df in self.df["product"].unique():
            product_name_lower = product_name_from_df.lower()
            
            
            pattern = r'\b' + re.escape(product_name_lower) + r'\b'
            
            if re.search(pattern, q_lower):
            
                if len(product_name_lower) > max_match_len:
                    best_match_product_name = product_name_from_df
                    max_match_len = len(product_name_lower)
        
        if best_match_product_name:
            
            hits = self.df[self.df["product"].str.lower() == best_match_product_name.lower()]
            if not hits.empty:
                return hits.iloc[0].to_dict()
        
        return {}
