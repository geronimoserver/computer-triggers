:: turn screen off
powershell (Add-Type '[DllImport(\"user32.dll\")]^public static extern int PostMessage(int hWnd, int hMsg, int wParam, int lParam);' -Name a -Pas)::PostMessage(-1,0x0112,0xF170,2)

:: mute system
call triggercmd_batches\util\nircmd.exe mutesysvolume 1

:: lock computer
Rundll32.exe user32.dll,LockWorkStation