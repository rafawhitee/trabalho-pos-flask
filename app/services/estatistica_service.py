import pandas as pd
from typing import Any
from utils.pandas_utils import do_basic_statistics_by_column, remove_not_numbers_values
from repositories.estatistica_repository import EstatisticaRepository

repository = EstatisticaRepository()

class EstatisticaService:
  
    def statistics(self) -> dict:
        df: Any = repository.get_dataframe()
        statistics_dict: dict = {
            "chutes": do_basic_statistics_by_column(df, "chutes"),
            "chutes_no_alvo": do_basic_statistics_by_column(df, "chutes_no_alvo"),
            "posse_de_bola": do_basic_statistics_by_column(df, "posse_de_bola"),
            "passes": do_basic_statistics_by_column(df, "passes"),
            "precisao_passes": do_basic_statistics_by_column(df, "precisao_passes"),
            "faltas": do_basic_statistics_by_column(df, "faltas"),
            "cartao_amarelo": do_basic_statistics_by_column(df, "cartao_amarelo"),
            "cartao_vermelho": do_basic_statistics_by_column(df, "cartao_vermelho"),
            "impedimentos": do_basic_statistics_by_column(df, "cartao_vermelho"),
            "escanteios": do_basic_statistics_by_column(df, "escanteios") 
        }
        return statistics_dict