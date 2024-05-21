from faction_wars.event_loop.event_queue import EventQueue

class GameLoop():
    def __init__(self , event_queue : EventQueue):
        self.event_queue = event_queue