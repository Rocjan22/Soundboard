from pathlib import Path

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import (
    QFileDialog,
    QGridLayout,
    QHBoxLayout,
    QInputDialog,
    QLabel,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
    )

from soundboard.audio.player import AudioPlayer
from soundboard.models.sound import Sound
from soundboard.storage.repository import SoundRepository
from soundboard.ui.sound_button import SoundButton


class MainWindow(QMainWindow):
    INITIAL_COLUMNS = 6
    WINDOW_PADDING = 32

    # ------------------------------------------------------------------------

    def __init__(self, repository: SoundRepository, player: AudioPlayer):
        super().__init__()
        self.setWindowTitle("Soundboard")
        self.repository = repository
        self.player = player

        central = QWidget()
        layout = QVBoxLayout(central)
        self.setCentralWidget(central)
        layout.addLayout(self._build_header())
        layout.addWidget(self._build_grid())

        area = self.screen().availableGeometry()
        content_width = self.INITIAL_COLUMNS * self._cell_width()
        width = content_width + self.WINDOW_PADDING
        width = min(width, area.width())
        height = area.height() * 0.7
        self.resize(int(width), int(height))
        self.move(area.center() - self.rect().center())

        self.sound_buttons = []
        for sound in self.repository.load_sounds():
            self._add_sound_button(sound)

        self.add_button.clicked.connect(self._on_add_clicked)
    
    # ------------------------------------------------------------------------

    def _build_header(self) -> QHBoxLayout:
        header = QHBoxLayout()
        title = QLabel("Soundboard")
        self.add_button = QPushButton("+")
        header.addWidget(title)
        header.addStretch()
        header.addWidget(self.add_button)
        return header

    def _build_grid(self) -> QScrollArea:
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        content = QWidget()
        self.grid = QGridLayout(content)
        self.scroll.setWidget(content)
        self.grid.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        return self.scroll
    
    # ------------------------------------------------------------------------

    def _on_add_clicked(self) -> None:
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
        self._add_sound_button(new_sound)

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        QTimer.singleShot(0, self._relayout_buttons)
    
    # ------------------------------------------------------------------------

    def _add_sound_button(self, sound: Sound) -> None:
        button = SoundButton(sound)
        self.sound_buttons.append(button)
        button.clicked.connect(lambda: self.player.play_sound(sound))
        self._relayout_buttons()

    def _relayout_buttons(self) -> None:
        columns = max(1, self.scroll.viewport().width() // self._cell_width())
        for index, button in enumerate(self.sound_buttons):
            row = index // columns
            col = index % columns
            self.grid.addWidget(button, row, col)

    def _cell_width(self) -> int:
        return SoundButton.WIDTH + self.grid.horizontalSpacing()
        
