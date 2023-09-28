from dataclasses import dataclass

@dataclass
class Message:
    user_id: int
    text: str
    peer_id: int


@dataclass
class UpdateMessage:
    from_id: int
    text: str
    id: int


@dataclass
class UpdateObject:
    id: int
    user_id: int
    body: str
    peer_id: int


@dataclass
class Update:
    type: str
    object: UpdateObject
