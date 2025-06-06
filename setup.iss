[Setup]
AppName=RegistroActividad
AppVersion=1.0
DefaultDirName={commonappdata}\RegistroActividad
DefaultGroupName=RegistroActividad
OutputBaseFilename=monitoring_service_installer
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\app_main.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "config\*"; DestDir: "{app}\config"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "programar_monitoreo.ps1"; DestDir: "{app}"; Flags: ignoreversion

[Run]
Filename: "powershell.exe"; Parameters: "-ExecutionPolicy Bypass -File ""{app}\programar_monitoreo.ps1"""; Flags: runhidden
