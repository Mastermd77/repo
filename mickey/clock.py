import pygame
import time
import math


hand_img = pygame.image.load("mickey_hand.png")
hand_img = pygame.transform.scale(hand_img, (20, 100))


def draw_hand(screen, angle, length):
    rotated = pygame.transform.rotate(hand_img, -angle)
    rect = rotated.get_rect(center=(200, 200))
    screen.blit(rotated, rect)


def draw_clock(screen):
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min

    
    sec_angle = (seconds / 60) * 360
    min_angle = (minutes / 60) * 360

    draw_hand(screen, sec_angle, 80)   
    draw_hand(screen, min_angle, 60)   