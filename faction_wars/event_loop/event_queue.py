
from faction_wars.database_interface.data_access import AsyncAccountDataAccess
from faction_wars.events.pending_event import PendingEvent

class EventQueue():
    def __init__(self , event_dict : dict[int , list[PendingEvent] | PendingEvent ] = None):
        
        self.event_list = event_dict if event_dict is not None else {}
    
    async def add_event(self, pending_event : PendingEvent):
        
        if pending_event.end_tick in self.event_list:
            
            self.event_list[pending_event.end_tick].append(pending_event)
            
        else:
            
            self.event_list[pending_event.end_tick] = [pending_event]
    
    async def get_events_by_tick(self , tick : int) -> list[PendingEvent]:
        
        return self.event_list.get(tick , [])

async def load_event_queue(account_data_access : AsyncAccountDataAccess ) -> EventQueue:
    
    account_data_access