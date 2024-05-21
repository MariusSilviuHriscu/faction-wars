import typing


class EventResultChange():
    def __init__(self , object_identifier_data : dict[str,str] , changed_data : dict[str,str] ):
        self.object_identifier_data = object_identifier_data
        self.changed_data = changed_data
    async def get_json(self) -> dict[str,dict]:
        return {'object_identifier_data' : self.object_identifier_data , 'changed_data' : self.changed_data}
    
class EventResult():
    
    def __init__(self , changes : list[str] = None):
        
        self.changes = changes
    async def get_json(self) -> list[dict[str,str]]:
        
        return [change.get_json() for change in self.changes]

