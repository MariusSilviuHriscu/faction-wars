import typing


class PendingEvent():
    def __init__(self,
                 start_tick : int ,
                 end_tick : int ,
                 event_callable : typing.Callable[[],dict],
                 event_extension : typing.Callable[...,typing.Self]
                 ):
        self.start_tick = start_tick
        self.end_tick = end_tick
        self.event_callable = event_callable
        self.event_extension = event_extension
    
    def get_event_json(self) -> dict:
        pass
    
async def load_pending_event(account_data_access : AsyncAccountDataAccess) -> PendingEvent:
    pass