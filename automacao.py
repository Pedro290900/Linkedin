import pyautogui
import time


pyautogui.PAUSE = 0.8  
pyautogui.FAILSAFE = True  

try:
   
    pyautogui.hotkey("win", "r")
    time.sleep(1)
    pyautogui.write("chrome")
    pyautogui.press("enter")

    
    time.sleep(3)

    
    url = "https://www.linkedin.com/in/pedro-coutinho-duarte-ti/"
    pyautogui.write(url)
    pyautogui.press("enter")

    
    time.sleep(5)

    
    pyautogui.alert("✅ Bem-vindo ao meu LinkedIn!\nAproveite para se conectar comigo 😉")

except Exception as e:
    pyautogui.alert(f"❌ Ocorreu um erro: {e}")
