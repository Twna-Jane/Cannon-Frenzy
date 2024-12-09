"""This module includes the SoundManager class which manages the games' sounds."""

import pygame

class SoundManager:
    def __init__(self):
        self.game_start_sound = pygame.mixer.Sound("assets/audio/sfx/game_start.wav")
        self.game_start_sound.set_volume(0.5)

        self.game_over_sound = pygame.mixer.Sound("assets/audio/sfx/game_over.wav")
        self.game_over_sound.set_volume(0.5)

        self.target_hit_sound = pygame.mixer.Sound("assets/audio/sfx/target_hit.ogg")
        self.target_hit_sound.set_volume(0.5)

        self.start_menu_music = pygame.mixer.Sound("assets/audio/music/mixkit-games-music-706.mp3")
        self.start_menu_music.set_volume(0.5)

        # Level Transition sound
        self.level_entry_sound = pygame.mixer.Sound("assets/audio/music/mixkit-game-level-completed-2059.wav")
        self.level_entry_sound.set_volume(0.5)

