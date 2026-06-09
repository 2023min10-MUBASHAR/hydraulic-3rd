$DesktopPath = [Environment]::GetFolderPath("Desktop")
$ShortcutPath = Join-Path $DesktopPath "Hydraulic Analyzer.lnk"
$TargetPath = "c:\Users\Prime Laptops\OneDrive\Documents\Desktop\hydraulic 3rd\launch.bat"
$WorkingDirectory = "c:\Users\Prime Laptops\OneDrive\Documents\Desktop\hydraulic 3rd"

$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut($ShortcutPath)
$Shortcut.TargetPath = $TargetPath
$Shortcut.WorkingDirectory = $WorkingDirectory
$Shortcut.Description = "Hydraulic Drill Machine Performance & Efficiency Analyzer"
$Shortcut.IconLocation = "C:\Windows\System32\python.exe,0"
$Shortcut.Save()

Write-Host "Desktop shortcut created successfully at: $ShortcutPath"
