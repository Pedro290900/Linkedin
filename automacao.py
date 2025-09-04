import pyautogui
import time

# Configurações globais
pyautogui.PAUSE = 0.8  # intervalo padrão entre os comandos
pyautogui.FAILSAFE = True  # mover o mouse para o canto da tela aborta o script

try:
    # Abrir o Chrome pelo "Executar"
    pyautogui.hotkey("win", "r")
    time.sleep(1)
    pyautogui.write("chrome")
    pyautogui.press("enter")

    # Esperar o navegador abrir
    time.sleep(3)

    # Abrir o LinkedIn
    url = "https://www.linkedin.com/in/pedro-coutinho-duarte-3371b7216/"
    pyautogui.write(url)
    pyautogui.press("enter")

    # Espera carregar
    time.sleep(5)

    # Mensagem de sucesso
    pyautogui.alert("✅ Bem-vindo ao meu LinkedIn!\nAproveite para se conectar comigo 😉")

except Exception as e:
    pyautogui.alert(f"❌ Ocorreu um erro: {e}")
