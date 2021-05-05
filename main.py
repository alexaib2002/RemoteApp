import sys
from os import system

# Current dependencies of the program
dependencies: list = ['xfreerdp']
py_dependencies: list = ['PySide2']

for item in py_dependencies:
    system('pip install %s' % (item))

class main():
    def isInstalled(self, bin) -> bool:
        from shutil import which
        return which(bin) is not None

    def startConnection(self, user: str, app: str, machine: str, password: str) -> None:
        import os
        system('xfreerdp /u:%s /p:%s /app:"%s" /v:%s' % (user, password, app, machine))
        return


if __name__ == "__main__":  # init
    from ui_RemoteApp import *
    app = QApplication()
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    main = main()

    for dep in dependencies:
        if not main.isInstalled(dep):
            print("You must install %s before executing this program" % (dep))
            exit(-1)

    ui.setupUi(MainWindow)
    ui.start.released.connect(lambda: main.startConnection(ui.userEdit.text(), ui.programEdit.text(), ui.ipEdit.text(),
            ui.userPassword.text()))
    MainWindow.show()
    sys.exit(app.exec_())
