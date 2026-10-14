import pygame

from soundboard.models.sound import Sound


class AudioPlayer:
    def __init__(self):
        pygame.mixer.init()

    def play_sound(self, sound: Sound) -> None:
        pygame.mixer.music.load(str(sound.file_path))
        pygame.mixer.music.play()

    def stop_sound(self) -> None:
        pygame.mixer.music.stop()
