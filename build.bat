@echo off
echo Limpiando ficheros antiguos...
del /Q dist\*.exe
rmdir /s /q build
rmdir /s /q dist
del app_main.spec

echo ¡Proceso completado!
pause
