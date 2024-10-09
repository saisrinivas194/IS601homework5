from app.commands import CommandHandler
from app.commands.discord import DiscordCommand
from app.commands.exit import ExitCommand
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand
from app.commands.menu import MenuCommand

class App:
    def __init__(self):
        """Constructor that initializes the command handler."""
        self.command_handler = CommandHandler()

    def start(self):
        """Starts the command-line interface."""
        # Register commands here
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("goodbye", GoodbyeCommand())
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("menu", MenuCommand())
        self.command_handler.register_command("discord", DiscordCommand())


        print("Hello World. Type 'exit' to exit.")
        
        while True:  # REPL: Read, Evaluate, Print, Loop
            user_input = input(">>> ").strip()
            if user_input:  # Check if the input is not empty
                try:
                    self.command_handler.execute_command(user_input)
                except Exception as e:
                    print(f"Error: {str(e)}")
            else:
                print("Invalid command. Please enter a command or type 'exit' to exit.")

# Ensure the application starts if this script is run directly
if __name__ == "__main__":
    app = App()
    app.start()
