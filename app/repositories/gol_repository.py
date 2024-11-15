from typing import List
import pandas as pd

class GolRepository:

    def __init__(self):
        self.df = self._read_dataframe()

    def find_by_partidas(self, partidas_ids: List[int]) -> List[dict]:
        return self.df[self.df["partida_id"].isin(partidas_ids)].to_dict(orient='records')
    
    def find_by_partida(self, partida_id: int) -> List[dict]:
        return self.df[self.df["partida_id"] == partida_id].to_dict(orient='records')

    def find_all(self) -> List[dict]:
        return self.df.to_dict(orient='records')

    def get_dataframe(self) -> pd.DataFrame:
        return self.df
    
    def update_dataframe(self) -> None:
        self.df = self._read_dataframe()

    def _read_dataframe(self) -> None:
        return pd.read_csv('gols.csv')