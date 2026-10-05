import pygame
from soundboard.models.sound import Sound


class AudioPlayer:
    def __init__(self):
        pygame.mixer.init()

    def play_sound(self, sound: Sound):
        pygame.mixer.music.load(str(sound.file_path))
        pygame.mixer.music.play()
