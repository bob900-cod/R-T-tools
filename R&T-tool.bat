@echo off
title Multi-Tool Reseaux et Telecommunications

:menu
cls
echo ================================
echo Multi-Tool Reseaux et Telecommunications
echo ================================
echo 1. Calculer le masque de sous-réseau
echo 2. Afficher le tableau de la transformee de Fourier
echo 3. Quitter
echo ================================
set /p choice=Choisissez une option (1-3):

if %choice%==1 goto subnet_calculator
if %choice%==2 goto fourier_transform
if %choice%==3 goto end

:subnet_calculator
cls
set /p ip=Entrez l'adresse IP:
set /p mask=Entrez le masque de sous-reseau:

REM Calcul du sous-réseau
for /f "tokens=1-4 delims=." %%a in ("%ip%") do (
    set octet1=%%a
    set octet2=%%b
    set octet3=%%c
    set octet4=%%d
)

for /f "tokens=1-4 delims=." %%a in ("%mask%") do (
    set mask1=%%a
    set mask2=%%b
    set mask3=%%c
    set mask4=%%d
)

set /a subnet1=octet1 & mask1
set /a subnet2=octet2 & mask2
set /a subnet3=octet3 & mask3
set /a subnet4=octet4 & mask4

echo Le sous-réseau est: %subnet1%.%subnet2%.%subnet3%.%subnet4%
pause
goto menu

:fourier_transform
cls
python fourier_transform.py
pause
goto menu

:end
exit