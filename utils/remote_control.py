from app.command import Command

class RemoteControl:

    def __init__(self):
        self._commands = []
        self._history = []
        
    def add_command(self, command: Command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()
            self._history.append(command)
        self._commands.clear()
        
    def undo_command(self):
        if self._history:
            command = self._history.pop()
            command.undo()