import typing



class Resources:
    def __init__(self ,
                 resources : dict[str, int | float] ):
        
        self.resources = resources
    
    def _combined_resource_key_set(self , other : typing.Self) -> set[str]:
        
        return self.resources.keys() | other.resources.keys()
    def __add__(self, other : typing.Self ):
        
        complete_resource_set = self._combined_resource_key_set(other)
        combined_resources = { resource : self.resources.get(resource,0) + other.resources.get(resource,0) for resource in complete_resource_set }
        
        return Resources(combined_resources)
    
    def __mul__(self, other : int  | float): #numeric type
        if type(other) == int :
            return Resources(
                { resource : self.resources.get(resource,0) * other for resource in self.resources.keys() }
                )
        if type(other) == float :
            return Resources(
                { resource : self.resources.get(resource,0) * other for resource in self.resources.keys() }
                )
        raise NotImplementedError
    
    def round(self , rounding_up : bool = False) -> typing.Self[dict[str,int]] :
        if rounding_up :
            return Resources(
                { resource : int(round(self.resources.get(resource,0))) for resource in self.resources.keys() }
                )
        else :
            return Resources(
                { resource : int(round(self.resources.get(resource,0) , 1)) for resource in self.resources.keys() }
                )
    
    def __sub__(self, other : typing.Self ):
        return self + (-1) * other
    
    def __neg__(self):
        return Resources(
            { resource : -1 * self.resources.get(resource,0) for resource in self.resources.keys() }
            )
    
    def __str__(self):
        return str(self.resources)

    def __repr__(self):
        return str(self)
    
    def get_json(self) -> dict[str,int | float]:
        return self.resources
    
    def __eq__(self, other : typing.Self ):
        
        complete_resource_set = self._combined_resource_key_set(other)
        return all(
            [self.resources.get(resource,0) == other.resources.get(resource,0) for resource in complete_resource_set and self.resources.keys() == other.resources.keys()]
            )
    def __le__(self, other : typing.Self ):
        return self == other or self < other
    def __lt__(self, other : typing.Self ):
        return all(
            [self.resources.get(resource,0) < other.resources.get(resource,0) for resource in self.resources.keys() and other.resources.keys()]
            )
    
    def __ge__(self, other : typing.Self ):
        return self == other or self > other
    def __gt__(self, other : typing.Self ):
        return all(
            [self.resources.get(resource,0) > other.resources.get(resource,0) for resource in self.resources.keys() and other.resources.keys()]
            )
    