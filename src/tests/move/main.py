# Robot codes 
from L9110URA import L9110URA
import time 
robot = L9110URA(13,12,5,23)
timeMove = 300
print("Frente...")
robot.passoFrente(timeMove)
time.sleep_ms(1000)
print("Re...")
robot.passoRe(timeMove)
time.sleep_ms(1000)
print("Esquerda...")
robot.passoEsquerda(timeMove)
time.sleep_ms(1000)
print("Direita...")
robot.passoDireita(timeMove)
time.sleep_ms(1000)
