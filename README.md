# RemoteApp
A Python-based application for executing remote apps on your computer

## Usage
At the moment, RemoteApp is only distributed as a Python script.


´git clone https://github.com/alexaib2002/RemoteApp.git´
´cd RemoteApp´
´python3 main.py´

This will open a new window, where you will introduce the remote username, the password, the application you want to 
execute (ex: explorer.exe), and the IP address of the machine.

## Roadmap
### Current
- [x] Check host PC dependencies before starting the app (XFreeRDP, PySide2)
- [ ] Application history, so its more convenient to user.
### Future
- [ ] Distribute as Snap / AppImage for ease-of-use in all distributions
- [ ] Prettify interface?
- [ ] Give the user an option for creating a desktop shortcut for the current application
