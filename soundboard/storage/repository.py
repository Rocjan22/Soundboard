import json
from pathlib import Path
from soundboard.models.sound import Sound


class SoundRepository:  # clase
    def __init__(self, data_dir: Path):  # metodo
        self.sounds_dir = data_dir / "sounds"  # atributo
        self.sounds_dir.mkdir(parents=True, exist_ok=True)
        self.data_file = data_dir / "sounds.json"

    def load_sounds(self) -> list[Sound]:
        if not self.data_file.exists():
            return []
        with self.data_file.open("r", encoding="utf-8") as sounds_file:
            raw_sounds = json.load(sounds_file)
        sounds_list = []
        for raw_sound in raw_sounds:
            sound = Sound(
                name=raw_sound["name"],
                file_path=self.sounds_dir / raw_sound["file"],
            )
            sounds_list.append(sound)
        return sounds_list

    def save_sounds(self, sounds: list[Sound]) -> None:
        raw_sounds = []
        for sound in sounds:
            raw_sound = {
                "name": sound.name,
                "file": sound.file_path.name,
            }
            raw_sounds.append(raw_sound)
        with self.data_file.open("w", encoding="utf-8") as sounds_file:
            json.dump(raw_sounds, sounds_file, indent=4, ensure_ascii=False)