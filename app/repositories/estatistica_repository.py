import csv
from typing import List
import pandas as pd

class EstatisticaRepository:

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
    
    def update_dataframe(self, new_data: pd.DataFrame, ignore_index: bool = True) -> None:
        if not set(new_data.columns).issubset(self.df.columns):
            raise Exception("Colunas inválidas")
        self.df = pd.concat([self.df, new_data], ignore_index=ignore_index)
        self.df.to_csv('estatisticas.csv', quoting=csv.QUOTE_ALL, quotechar='"', index=False)

    def _read_dataframe(self) -> pd.DataFrame:
        return pd.read_csv('estatisticas.csv', quoting=csv.QUOTE_ALL, quotechar='"')