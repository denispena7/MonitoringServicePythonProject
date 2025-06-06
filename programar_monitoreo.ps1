# Obtener la ruta absoluta del directorio donde está este script
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition

# Ruta al ejecutable
$exePath = Join-Path $scriptDir "app_main.exe"

# Usuario actual
$currentUser = "$env:USERDOMAIN\$env:USERNAME"

$settings = New-ScheduledTaskSettingsSet -ExecutionTimeLimit (New-TimeSpan -Seconds 0)

# --- Tarea 1: monitor ---
$taskName1 = "RegistroActividad_Main"
$action1 = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-WindowStyle Hidden $exePath monitor"
$trigger1 = New-ScheduledTaskTrigger -AtLogOn
$principal1 = New-ScheduledTaskPrincipal -UserId $currentUser -RunLevel Highest
Register-ScheduledTask -TaskName $taskName1 -Action $action1 -Trigger $trigger1 -Principal $principal1 -Settings $settings -Force

# --- Tarea 2: run_api ---
$taskName2 = "RegistroActividad_API"
$action2 = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-WindowStyle Hidden $exePath run_api"
$trigger2 = New-ScheduledTaskTrigger -AtLogOn
$principal2 = New-ScheduledTaskPrincipal -UserId $currentUser -RunLevel Highest
Register-ScheduledTask -TaskName $taskName2 -Action $action2 -Trigger $trigger2 -Principal $principal2 -Settings $settings -Force

Write-Host "Tareas programadas correctamente para el usuario: $currentUser"
