## WhatsApp Online Tracker
Bei dem hier vorliegenden Programm handelt es sich um ein Tracker für alle Whatsapp Kontakte welche im Chatverlauf hinterlegt sind. Es wird hierbei das Modul Selenium genutz um auf den Quellcode von WhatsAppWeb zu zu greifen. 
Das Programm schaut ob der Nutzer online ist und gibt die Info darüber in der cmd-line zurück bzw schreibt diese Online infos in eine nach dem Chatnamen benanten Datei im Pfad /tmp/timestamp bzw %tmp%\timestamp unter Windows
Bei einem Chatverlauf über 11 teilnehmer tritt eine komische reihenfolge der ab zu arbeitenden Chats ein was, wenn die vorbereitung beachtet wurde, ignoriert werden kann da alle Nutzer erfasst werden.

### Vorbereitungen:
1. zuerst muss nach der Anleitung [Chrome Remote Debugger](https://github.com/DanielMueller1309/Python/wiki/Chrome-Remote-Debugger) der Debugging modus von Chrome geöffnet und web.whatsapp.com aufgerufen werden.
1. sorgen sie durch langziehen des Chrome Fensters oder durch verschieben von Kontakten ins Archiev dafür das kein Scrollbarer Chatverlauf existiert. Falls dies doch der Fall ist, führt das dazu das nicht alle Kontakte im Verlauf erfasst werden. 
1.danach das Python Script starten.