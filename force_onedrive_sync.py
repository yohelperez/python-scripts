import os
import time
import subprocess

def force_onedrive_sync():
    # Ruta al ejecutable de OneDrive
    onedrive_executable = r"C:\Program Files\Microsoft OneDrive\OneDrive.exe"

    # Detener OneDrive (opcional, si hay problemas de sincronización)
    print("Deteniendo OneDrive...")
    subprocess.run(["taskkill", "/f", "/im", "OneDrive.exe"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(2)  # Espera un momento para asegurarte de que OneDrive se detuvo.

    # Reiniciar OneDrive
    print("Reiniciando OneDrive...")
    subprocess.Popen(onedrive_executable, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(5)  # Espera a que OneDrive reinicie.

    # Mensaje final
    print("OneDrive ha sido sincronizado.")