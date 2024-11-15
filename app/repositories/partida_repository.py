from typing import List
import pandas as pd

class PartidaRepository:
    
    def __init__(self):
        self.df = self._read_dataframe()

    def find_all_by_team(self, team: str) -> List[dict]:
        filters = (self.df["mandante"].str.upper() == team.upper()) | (self.df["visitante"].str.upper() == team.upper())
        return self.df[filters].to_dict(orient='records')

    def find_by_id(self, id: int) -> dict:
        return self.df[self.df["ID"] == id].to_dict(orient='records')[0]
    
    def find_all(self) -> List[dict]:
        return self.df.to_dict(orient='records')

    def get_dataframe(self) -> pd.DataFrame:
        return self.df
    
    def update_dataframe(self) -> None:
        self.df = self._read_dataframe()
        
    def _read_dataframe(self) -> None:
        df = pd.read_csv('partidas.csv')
        df['data_formatada'] = df['data']
        df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
        return df