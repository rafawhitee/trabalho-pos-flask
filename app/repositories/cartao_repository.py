from typing import List
import pandas as pd

df = pd.read_csv('cartoes.csv')

class CartaoRepository:
    
    def find_by_partida(self, partida_id: int) -> List[dict]:
        return df[df["partida_id"] == partida_id].to_dict(orient='records')

    def find_all(self) -> List[dict]:
        return df.to_dict(orient='dict')

    def get_dataframe(self) -> pd.DataFrame:
        return df