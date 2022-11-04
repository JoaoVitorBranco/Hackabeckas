import abc

from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.helpers.errors.domain_errors import EntityError

class Hamburguer(abc.ABC):
    flavor: FLAVOR
    
    def __init__(self, flavor: FLAVOR):
        if(flavor == None or type(flavor) != FLAVOR):
            raise EntityError('flavor')
        self.flavor = flavor
        
    
        
    