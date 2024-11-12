from repositories.cartao_repository import CartaoRepository
from repositories.estatistica_repository import EstatisticaRepository
from repositories.gol_repository import GolRepository
from repositories.partida_repository import PartidaRepository

repository = PartidaRepository()
gol_repository = GolRepository()
estatistica_repository = EstatisticaRepository()
cartao_repository = CartaoRepository()

class PartidaService:

    def find_by_id(self, id: int) -> dict:
        return repository.find_by_id(id)