@echo off
title Multi-Tool Reseaux et Telecommunications

:menu
cls
:::    _|_|_|      _|    _|_|_|_|_|      _|  _|_|_|_|_|    _|_|      _|_|    _|       
:::    _|    _|  _|  _|      _|        _|        _|      _|    _|  _|    _|  _|       
:::    _|_|_|      _|_|  _|  _|      _|          _|      _|    _|  _|    _|  _|       
:::    _|    _|  _|    _|    _|    _|            _|      _|    _|  _|    _|  _|       
:::    _|    _|    _|_|  _|  _|  _|              _|        _|_|      _|_|    _|_|_|_| 

for /f "delims=: tokens=*" %%A in ('findstr /b ::: "%~f0"') do powershell -command "& {Write-Host '%%A' -ForegroundColor Red}"

echo ================================
echo 1. Calculer le nombre d'hôtes ou le masque de sous-réseau
echo 2. Afficher le tableau de la transformee de Fourier
echo 3. Tracer un signal
echo 4. Tracer la transformee de Fourier
echo 5. Analyser un fichier audio
echo 6. Quitter
echo ================================
set /p choice=Choisissez une option (1-6):

if %choice%==1 goto subnet_calculator
if %choice%==2 goto fourier_transform
if %choice%==3 goto plot_signal
if %choice%==4 goto plot_fourier_transform
if %choice%==5 goto Fichier-audio
if %choice%==6 goto end

:subnet_calculator
cls
echo Choisissez une option :
echo 1. Calculer le nombre d'hôtes
echo 2. Calculer le masque de sous-réseau
echo 3. Afficher toutes les informations
set /p subnet_choice=Choisissez une option (1-3):

if %subnet_choice%==1 (
    set /p cidr=Entrez la notation CIDR (ex: /24):
    python subnet_calculator.py hosts %cidr%
) else if %subnet_choice%==2 (
    set /p cidr=Entrez la notation CIDR (ex: /24):
    python subnet_calculator.py mask %cidr%
) else if %subnet_choice%==3 (
    set /p cidr=Entrez la notation CIDR (ex: /24):
    python subnet_calculator.py all %cidr%
) else (
    echo Option invalide.
)
pause
goto menu

:fourier_transform
cls
python fourier_table.py
pause
goto menu

:plot_signal
cls
set /p expression=Entrez l'expression du signal (ex: 5*cos(2*np.pi*1000*t)):
set /p time_unit=Afficher l'axe des abscisses en (s) secondes ou (radian) ?:
python plot_signal.py "%expression%" %time_unit%
pause
goto menu

:plot_fourier_transform
cls
set /p expression=Entrez l'expression du signal (ex: 5*cos(2*np.pi*1000*t)):
python TFT.py "%expression%"
pause
goto menu

:Fichier-audio
cls
set /p audio_filename=Entrez le nom du fichier audio :
python Fichier-audio.py "%audio_filename%"
pause
goto menu

:end
exit