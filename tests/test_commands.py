import pytest
from app import App
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand
from app.commands.discord import DiscordCommand
from app.commands import CommandHandler, Command

class MockCommand(Command):
    def execute(self):
        print("Mock command executed.")

def test_list_commands(capfd: pytest.CaptureFixture[str]):
    handler = CommandHandler()
    
    # Register a mock command to have something in the commands dictionary
    handler.register_command("mock", MockCommand())
    
    # Now call the list_commands method
    handler.list_commands()

    # Capture the output
    out, err = capfd.readouterr()
    assert "Available commands:" in out
    assert "- mock" in out

def test_list_commands_no_commands(capfd: pytest.CaptureFixture[str]):
    handler = CommandHandler()
    
    # Call the list_commands method when no commands are registered
    handler.list_commands()

    # Capture the output
    out, err = capfd.readouterr()
    assert "No commands available." in out
    
def test_discord_command(capfd: pytest.CaptureFixture[str]):
    """Test that the DiscordCommand prints the expected output."""
    command = DiscordCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert out == "I WIll send something to discord\n", "The DiscordCommand should print the expected output."

def test_greet_command(capfd: pytest.CaptureFixture[str]):
    command = GreetCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert out == "Hello, World!\n", "The GreetCommand should print 'Hello, World!'"

def test_goodbye_command(capfd: pytest.CaptureFixture[str]):
    command = GoodbyeCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert out == "Goodbye\n", "The GreetCommand should print 'Hello, World!'"

def test_app_discord_command(capfd: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch):
    """Test that the REPL correctly handles the 'discord' command."""
    # Simulate user entering 'discord' followed by 'exit'
    inputs = iter(['discord', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    
    with pytest.raises(SystemExit):
        app.start()  # This should include registering and executing the discord command

    # Capture output after running the command
    captured = capfd.readouterr()
    assert "I WIll send something to discord" in captured.out  # Check if the output is correct
    
def test_app_greet_command(capfd: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_menu_command(capfd: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))


    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"
