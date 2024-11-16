import pandas as pd
from typing import List
from repositories.cartao_repository import CartaoRepository
from repositories.estatistica_repository import EstatisticaRepository
from repositories.gol_repository import GolRepository
from repositories.partida_repository import PartidaRepository

repository = PartidaRepository()
gol_repository = GolRepository()
estatistica_repository = EstatisticaRepository()
cartao_repository = CartaoRepository()

class PartidaService:

    def update_dataframe(self, request_body: List[dict]) -> None:
        new_data = pd.DataFrame(request_body)
        repository.update_dataframe(new_data)
        
    def find_all_by_team(self, team: str) -> List[dict]:
        partidas: List[dict] = repository.find_all_by_team(team)
        for partida in partidas:
            partida = self._find_statistics(partida)
        return partidas
    
    def find_by_id(self, id: int) -> dict:
        return self._find_statistics(repository.find_by_id(id))
    
    def _find_statistics(self, partida: dict) -> dict:
        id: int = partida["ID"]
        partida["gols"] = gol_repository.find_by_partida(id)
        partida["estatisticas"] = estatistica_repository.find_by_partida(id)
        partida["cartoes"] = cartao_repository.find_by_partida(id)
        return partida