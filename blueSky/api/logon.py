from dataclasses import dataclass

@dataclass
class LogonInfo():
    account: int
    password: str
    server: str