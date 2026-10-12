from PySide6.QtWidgets import QPushButton

from soundboard.models.sound import Sound


class SoundButton(QPushButton):
    WIDTH = 200
    HEIGHT = 100

    def __init__(self, sound: Sound):
        super().__init__(sound.name)
        self.sound = sound
        self.setFixedSize(self.WIDTH, self.HEIGHT)