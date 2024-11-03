# not a class, a "struct" or "data class"
from dataclasses import dataclass
from satellite import Satellite


@dataclass
class PairD:

    key: str
    value: Satellite
