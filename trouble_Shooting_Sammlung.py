# Hier werden die Probleme mit VSCode gesammelt
# 1
# VSCode Kommentar-Shortcut: 
# Zeilenkommentar
# Windows:
# Strg + k+ c

# auskommentieren:
# Strg + k + u

# MacOS:
# Command + k + c
# Blockkommentar:
# Shift + alt + a


# 2
# venv-Aktivieren: 
# in Terminal unter dem Ordner, wo die Python-Programme gespeichert sind:
# .\venv\Scripts\activate
# dann kann man wieder sein venv benutzen: 
# es siehr so aus: 
# (venv) PS C:\Users\...\> 

# 3
# lxml-Package für Python installieren
# in Powershell eingeben, welche Version für Python ist: 
# py --version
# Wenn die Version: 
# Python 3.13.7
# Dann brauche ich eine whl-Datei für das lxml-Package: 
# lxml-6.0.0-cp313-cp313-win_arm64.whl
# diese whl-Datei lade ich auf der Webseite herunter: 
# https://pypi.org/project/lxml/#files
# dann installiere ich das Packege in Powershell: 
# pip install "C:\Users\...\lxml-6.0.0-cp313-cp313-win_amd64.whl"
# whl-Datei sollte in Pfad eingegeben werden. 
