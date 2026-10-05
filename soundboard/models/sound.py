from dataclasses import dataclass
from pathlib import Path


@dataclass
class Sound:
    name: str
    file_path: Path