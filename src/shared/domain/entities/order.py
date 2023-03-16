import abc
from src.shared.helpers.errors.domain_errors import EntityError

from src.shared.domain.entities.hamburguer import Hamburguer

class Order(abc.ABC):
    hamburguer: Hamburguer
    table: int
    id_order: int
    
    def __init__(self, hamburguer: Hamburguer, table: int, id_order: int):
        if(type(id_order) != int):
            raise EntityError('id_order')
        self.id_order = id_order
        
        if(hamburguer == None and type(hamburguer) != Hamburguer):
            raise EntityError('hamburguer')
        self.hamburguer = hamburguer
        
        if(table == None and type(table) != int):
            raise EntityError('table')
        self.table = table
        
        