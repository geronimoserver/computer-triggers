Dim Wsh
Set Wsh = Wscript.CreateObject("Wscript.Shell")
Wsh.SendKeys "{" + WScript.Arguments.Item(0) +"}"
