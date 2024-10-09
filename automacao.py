import pyautogui
import time


pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
time.sleep(3)
pyautogui.write("https://www.linkedin.com/in/pedro-coutinho-duarte-3371b7216/")
pyautogui.press("enter")
time.sleep(1)
pyautogui.alert("Bem-vindo ao meu Linkedin")
