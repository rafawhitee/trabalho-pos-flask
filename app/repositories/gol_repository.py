import pandas as pd

df = pd.read_csv('gols.csv')

class GolRepository:

    def find_by_partida(self, partida_id: int) -> dict:
        return df[df["partida_id"] == partida_id].to_dict(orient='records')

    def find_all(self) -> dict:
        return df.to_dict(orient='records')

    def get_dataframe(self) -> pd.DataFrame:
        return df