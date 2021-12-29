# Standard imports
from typing import List, Dict, Any
from dataclasses import dataclass


@dataclass
class LoadedModel:
    name: str
    tasks: List[str]
    execute_kwargs: Dict[str, Any]
