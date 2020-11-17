@echo off
echo chcete nainstalovat moduly pro funkcnost peti assistenta?
echo %cd%
pause
py -m pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl
py -m pip install gTTS
py -m pip install playsound
py -m pip install wikipedia
echo pokud nic nebylo cervene tak se vse nainstalovalo
pause