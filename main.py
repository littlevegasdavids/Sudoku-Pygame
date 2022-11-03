import pygame
import requests

response = requests.get('https://sugoku.herokuapp.com/board?difficulty=easy')

print(response.json()['board'])