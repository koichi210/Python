::%1 is path name for the analysis

set CUURENT_DIR=%~dp0

python %CUURENT_DIR%Proc.py %1

exit(%ERRORLEVEL%)
