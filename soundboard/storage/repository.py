from pathlib import Path


class SoundRepository:
    def __init__(self, data_dir: Path):
        self.sounds_dir = data_dir / "sounds"
        self.sounds_dir.mkdir(parents=True, exist_ok=True)
        self.data_file = data_dir / "sounds.json"