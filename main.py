from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication

from soundboard.audio.player import AudioPlayer
from soundboard.ui.main_window import MainWindow
from soundboard.storage.repository import SoundRepository


def get_base_path() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent


def main() -> None:
    app = QApplication(sys.argv)
    repository = SoundRepository(get_base_path() / "data")
    player = AudioPlayer()
    window = MainWindow(repository, player)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()