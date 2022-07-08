Add-Type -AssemblyName 'System.Windows.Forms'

$everys = 9

while ($true)
{
    Start-Sleep -Seconds $everys

    [System.Windows.Forms.SendKeys]::SendWait(' ')  # Present!
}
