import pandas as pd

df = pd.read_csv('partidas.csv')

class PartidaRepository:
    
    def find_all(self) -> dict:
        return df.to_dict(orient='records')

    def get_dataframe(self) -> pd.DataFrame:
        return df