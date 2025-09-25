# logs-windows.ps1
# Muestra los últimos 10 errores del log del sistema

Get-EventLog -LogName System -EntryType Error -Newest 10 | Format-Table TimeGenerated, Source, EventID, Message
