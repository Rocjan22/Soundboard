import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication

from soundboard.ui.main_window import MainWindow
from soundboard.audio.player import AudioPlayer
from soundboard.storage.repository import SoundRepository


def main():
    app = QApplication(sys.argv)
    repository = SoundRepository(Path("data"))
    player = AudioPlayer()
    window = MainWindow(repository, player)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()