from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        """Execute the command."""
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        """Register a new command."""
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        """Execute the specified command if it exists."""
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")

    def list_commands(self):
        """List all available commands."""
        if self.commands:
            print("Available commands:")
            for command_name in self.commands:
                print(f"- {command_name}")
        else:
            print("No commands available.")