from pathlib import Path

from PySide6.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QInputDialog,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    )

from soundboard.audio.player import AudioPlayer
from soundboard.storage.repository import SoundRepository


class MainWindow(QMainWindow):
    def __init__(self, repository: SoundRepository, player: AudioPlayer):
        super().__init__()
        self.setWindowTitle("Soundboard")
        self.repository = repository
        self.player = player

        area = self.screen().availableGeometry()
        width = area.width() * 0.65
        height = area.height() * 0.7
        self.resize(int(width), int(height))
        self.move(area.center() - self.rect().center())

        central = QWidget()
        layout = QVBoxLayout(central)
        self.setCentralWidget(central)
        layout.addLayout(self._build_header())

        self.add_button.clicked.connect(self._on_add_clicked)

    def _build_header(self) -> QHBoxLayout:
        header = QHBoxLayout()
        title = QLabel("Soundboard")
        self.add_button = QPushButton("+")
        header.addWidget(title)
        header.addStretch()
        header.addWidget(self.add_button)
        return header

    def _on_add_clicked(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Selecciona un sonido",
            "",
            "Audio (*.mp3)",
        )
        if not file_path:
            return
        path = Path(file_path)
        name, ok = QInputDialog.getText(
            self,
            "Nombre del botón",
            "¿Cómo quieres llamar a este sonido?",
            text=path.stem,
        )
        if not ok:
            return
        new_sound = self.repository.add_sound(source_path=path, name=name.strip())
        print(new_sound)
        
