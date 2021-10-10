@echo off
color 2
echo ShortcutZ R.B.D
echo RECOVER BACKUP AND DESTROY
echo MATAR WSCRIPT EN EJECUCIÓN
echo RECUPERAR ARCHIVOS OCULTOS
echo HACER BACKUP DE LOS COMPONENTES A ELIMINAR EN EL CASO QUE USTED UTILIZE ALGUNO DE ELLOS EN SU PENDRIVE POR ALGUN MOTIVO
echo EJ: VIDEOJUEGOS, PROGRAMAS, OFICE SCRIPTING, ETC
echo MATAR EL VIRII
echo.
::Modificado por thekorko
::Basado en el script "Desocultar":  Arquezvall2004
echo.
echo Unidades disponibles en tu PC:
echo.
wmic logicaldisk get caption | findstr /r /v "^Caption" 

:unidad
::Obtenemos la unidad a desocultar
set /p unidad=Unidad: 
if not defined unidad (goto:unidad)
echo intentando matar wscript.exe
taskkill /F /IM wscript.exe

echo Recuperando archivos y directorios...

::obtenemos todas las carpetas y subcarpetas y las guardamos en lista.txt
dir /a:d /s /b %unidad%:\ > lista.txt
::matamos todos los atributos picantes (extra dedicated scan slow mode, E.D.S.S.M for short)
FOR /F "delims=" %%i in (lista.txt) do ( attrib -s -r -h "%%i" )

echo Archivos y directorios recuperados...
::Casi hacker
echo Iniciando modulo BACK...
::Ah que

:backup
echo ATENCION ESTE SCRIPT ELIMINA TODOS LOS SIGUIENTES TIPOS DE ARCHIVOS ENCONTRADOS.
set /P hacer_backup=Hacer backup de: Archivo por Lotes de Windows, Accesos directos, Archivos Inf y archivos de Visual Basic Script?[SI/NO/BAT]?
if /I "%hacer_backup%" EQU "SI" goto :si_robocopy
if /I "%hacer_backup%" EQU "NO" goto :no_robocopy
if /I "%hacer_backup%" EQU "BAT" goto :si_bat
goto :backup


::Seccion con backup incluido, el nombre robocopy es de onda(aguante robocopy), usamos xcopy /R /C /H /Y
:si_robocopy
echo El comando xcopy /R /C /H /Y es usado, para dar soporte a WinXP, tenga en cuenta que posee una limitacion de ruta de 256 caracteres
echo **************************************************************************
echo "Copiando archivos a carpetas con propiedad -read only"
echo Dentro de cada carpeta en la que se contiene un archivo de tipo vbs, inf, lnk o bat. 
echo Se creara una carpeta oculta con una copia de esos mismos archivos anteriormente eliminados.
pause
set carpeta=b4ckup%random%
mkdir "%carpeta%"
taskkil /F /IM wscript.exe


::A cada carpeta le hacemos el backup
taskkil /F /IM wscript.exe
FOR /f "delims=" %%i in (lista.txt) do ( echo D | xcopy /R /C /H /Y "%%i\*.vbs" "%%i\%carpeta%\" | attrib "%%i\%carpeta%" +r )
taskkil /F /IM wscript.exe
taskkil /F /IM wscript.exe
FOR /F "delims=" %%i in (lista.txt) do ( echo D | xcopy /R /C /H /Y "%%i\*.lnk" "%%i\%carpeta%\" | attrib "%%i\%carpeta%" +r )
taskkil /F /IM wscript.exe
taskkil /F /IM wscript.exe
FOR /F "delims=" %%i in (lista.txt) do ( echo D | xcopy /R /C /H /Y "%%i\*.bat" "%%i\%carpeta%\" | attrib "%%i\%carpeta%" +r )
taskkil /F /IM wscript.exe
taskkil /F /IM wscript.exe
FOR /F "delims=" %%i in (lista.txt) do ( echo D | xcopy /R /C /H /Y "%%i\*.LNK" "%%i\%carpeta%\" | attrib "%%i\%carpeta%" +r )
taskkil /F /IM wscript.exe
taskkil /F /IM wscript.exe
FOR /F "delims=" %%i in (lista.txt) do ( echo D | xcopy /R /C /H /Y "%%i\*.BAT" "%%i\%carpeta%\" | attrib "%%i\%carpeta%" +r )
taskkil /F /IM wscript.exe
FOR /F "delims=" %%i in (lista.txt) do ( echo D | xcopy /R /C /H /Y "%%i\*.inf" "%%i\%carpeta%\" | attrib "%%i\%carpeta%" +r )
taskkil /F /IM wscript.exe
FOR /F "delims=" %%i in (lista.txt) do ( echo D | xcopy /R /C /H /Y "%%i\*.INF" "%%i\%carpeta%\" | attrib "%%i\%carpeta%" +r )
taskkil /F /IM wscript.exe
FOR /F "delims=" %%i in (lista.txt) do ( echo D | xcopy /R /C /H /Y "%%i\*.VBS" "%%i\%carpeta%\" | attrib "%%i\%carpeta%" +r )
taskkil /F /IM wscript.exe
FOR /F "delims=" %%i in (lista.txt) do ( echo D | xcopy /R /C /H /Y "%%i\*.vbs" "%%i\%carpeta%\" | attrib "%%i\%carpeta%" +r )
taskkil /F /IM wscript.exe
FOR /F "delims=" %%i in (lista.txt) do ( echo D | xcopy /R /C /H /Y "%%i\RADB59~1.VBS" "%%i\%carpeta%\" | attrib "%%i\%carpeta%" +r )
taskkil /F /IM wscript.exe
FOR /F "delims=" %%i in (lista.txt) do ( echo D | xcopy /R /C /H /Y "%%i\RADB59*.*" "%%i\%carpeta%\" | attrib "%%i\%carpeta%" +r )

taskkil /F /IM wscript.exe
xcopy /R /C /H /Y "*.INF" "%unidad%:\%carpeta%"
xcopy /R /C /H /Y "*.VBS" "%unidad%:\%carpeta%"
xcopy /R /C /H /Y "*.lnk" "%unidad%:\%carpeta%"
xcopy /R /C /H /Y "*.vbs" "%unidad%:\%carpeta%"
taskkil /F /IM wscript.exe

xcopy /R /C /H /Y "*.LNK" "%unidad%:\%carpeta%"
xcopy /R /C /H /Y "*.bat" "%unidad%:\%carpeta%"
xcopy /R /C /H /Y "*.BAT" "%unidad%:\%carpeta%"
xcopy /R /C /H /Y "RADB59~1.VBS" "%unidad%:\%carpeta%"
xcopy /R /C /H /Y "RADB59*.*" "%unidad%:\%carpeta%"
attrib "%unidad%:\%carpeta%" +r
echo Backup general realizado con exito
pause
goto:no_robocopy


:si_bat
taskkil /F /IM wscript.exe
echo SE VAN A SALVAGUARDAR TODOS LOS ARCHIVOS .BAT EXCLUSIVAMENTE
echo El comando xcopy /R /C /H /Y es usado, para dar soporte a WinXP, tenga en cuenta que posee una limitacion de ruta de 256 caracteres
echo **************************************************************************
echo "Copiando archivos a carpetas con propiedad -read only"
echo Dentro de cada carpeta en la que se contiene un archivo de tipo vbs, inf, lnk o bat. 
echo Se creara una carpeta oculta con una copia de esos mismos archivos anteriormente eliminados con del /F /Q.
pause

echo deletea2 con exito
xcopy /R /C /H /Y "*.bat" "%unidad%:\%carpeta%"
xcopy /R /C /H /Y "*.BAT" "%unidad%:\%carpeta%"
FOR /F "delims=" %%i in (lista.txt) do ( echo D | xcopy /R /C /H /Y "%%i\*.BAT" "%%i\%carpeta%\" | attrib "%%i\%carpeta%" +r )
FOR /F "delims=" %%i in (lista.txt) do ( echo D | xcopy /R /C /H /Y "%%i\*.bat" "%%i\%carpeta%\" | attrib "%%i\%carpeta%" +r )
echo Backup de archivos BAT realizado con exito
pause
goto:no_robocopy


:no_robocopy
taskkil /F /IM wscript.exe
::Sin robocopy, solo se elimina, no se salva, tambien los modulos de backup redirigen aca, para la eliminacion.
::A cada carpeta forzamos la eliminacion total
FOR /F "delims=" %%i in (lista.txt) do ( del /F /Q "%%i\*.vbs" )
FOR /F "delims=" %%i in (lista.txt) do ( del /F /Q "%%i\*.lnk" )
FOR /F "delims=" %%i in (lista.txt) do ( del /F /Q "%%i\*.VBS" )
FOR /F "delims=" %%i in (lista.txt) do ( del /F /Q "%%i\*.LNK" )
FOR /F "delims=" %%i in (lista.txt) do ( del /F /Q "%%i\*.BAT" )
FOR /F "delims=" %%i in (lista.txt) do ( del /F /Q "%%i\*.bat" )
FOR /F "delims=" %%i in (lista.txt) do ( del /F /Q "%%i\*.inf" )
FOR /F "delims=" %%i in (lista.txt) do ( del /F /Q "%%i\*.bat" )
FOR /F "delims=" %%i in (lista.txt) do ( del /F /Q "%%i\*.INF" )
FOR /F "delims=" %%i in (lista.txt) do ( del /F /Q "%%i\RADB59~1.VBS" )
FOR /F "delims=" %%i in (lista.txt) do ( del /F /Q "%%i\RADB59*.*" )
del /F /Q "RADB59~1.VBS"
del /F /Q "RADB59*.*"
del /F /Q "*.vbs"

echo Deletear *.vbs
	del /F /Q *.vbs
echo del "RADB59~1.VBS"
	del /F /Q "RADB59*.*"
	del /F /Q "RADB59~1.VBS"
echo Deletear todos los *.LNK
	del /F /Q *.lnk

::borramos el archivo lista.txt

del /F /Q lista.txt

exit
