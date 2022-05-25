from dataclasses import dataclass

class test:
    name: str = 'test'

@dataclass(slots=True)
class User:
    discord_id: int
    roblox_id: int
    verified: bool = False
    
