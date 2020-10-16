class pycharm:
    def execute(self):
        print("executing")
class vscode:
    def execute(self):
        print("vs running")

class laptop:
    def code(self,ide):
        ide.execute()

lap1=laptop()
ide=pycharm()
ide1=vscode()
lap1.code(ide1)
