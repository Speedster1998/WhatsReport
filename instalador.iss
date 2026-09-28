; Script de Inno Setup para Generador de Reportes de WhatsApp
#define MyAppName "Generador de Reportes de WhatsApp"
#define MyAppVersion "1.4.5"
#define MyAppPublisher "Alexander Jesus Laura Julca - TI"
#define MyAppExeName "Generador de Reportes.exe"

[Setup]
; Identificador de la aplicación
AppId={{D9A4C73E-5B92-4C10-8A5F-E1D83A412A34}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
DisableProgramGroupPage=yes
OutputDir=dist_installer
OutputBaseFilename=Instalador_Generador_Reportes_v1.4
SetupIconFile=icons\favicon.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"

[Files]
; Archivo ejecutable principal compilado previamente con PyInstaller
Source: "dist\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
; Acceso directo en el Menú Inicio
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\{#MyAppExeName}"
; Acceso directo en el Escritorio
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
; Opción para iniciar la aplicación al finalizar la instalación
Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Filename: "{app}\{#MyAppExeName}"; Flags: nowait postinstall skipifsilent