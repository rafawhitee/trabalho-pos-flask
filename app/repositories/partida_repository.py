from typing import List
import pandas as pd

df = pd.read_csv('partidas.csv')

class PartidaRepository:
    
    def find_by_id(self, id: int) -> dict:
        return df[df["ID"] == id].to_dict(orient='records')[0]
    
    def find_all(self) -> List[dict]:
        return df.to_dict(orient='records')

    def get_dataframe(self) -> pd.DataFrame:
        return df