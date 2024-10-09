import pytest
from app import App

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    App.start()
    out, err = capfd.readouterr()

    # Check that the initial greeting is printed and the REPL exits gracefully
    assert "Hello World. Type 'exit' to exit." in out
    assert "Exiting..." in out

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, err = capfd.readouterr()

    # Check that the REPL responds to an unknown command and then exits after 'exit' command
    assert "Hello World. Type 'exit' to exit." in out
    assert "Unknown command. Type 'exit' to exit." in out
    assert "Exiting..." in out

def test_app_addition(capfd, monkeypatch):
    """Test the addition command."""
    inputs = iter(['add 3 4', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, err = capfd.readouterr()

    # Check that the result of the addition is printed correctly
    assert "Hello World. Type 'exit' to exit." in out
    assert "Result: 7.0" in out
    assert "Exiting..." in out

def test_app_subtraction(capfd, monkeypatch):
    """Test the subtraction command."""
    inputs = iter(['subtract 10 5', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, err = capfd.readouterr()

    # Check that the result of the subtraction is printed correctly
    assert "Hello World. Type 'exit' to exit." in out
    assert "Result: 5.0" in out
    assert "Exiting..." in out

def test_app_multiplication(capfd, monkeypatch):
    """Test the multiplication command."""
    inputs = iter(['multiply 3 5', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, err = capfd.readouterr()

    # Check that the result of the multiplication is printed correctly
    assert "Hello World. Type 'exit' to exit." in out
    assert "Result: 15.0" in out
    assert "Exiting..." in out

def test_app_division(capfd, monkeypatch):
    """Test the division command."""
    inputs = iter(['divide 20 5', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, err = capfd.readouterr()

    # Check that the result of the division is printed correctly
    assert "Hello World. Type 'exit' to exit." in out
    assert "Result: 4.0" in out
    assert "Exiting..." in out

def test_app_division_by_zero(capfd, monkeypatch):
    """Test how the REPL handles division by zero."""
    inputs = iter(['divide 10 0', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, err = capfd.readouterr()

    # Check that the division by zero error message is printed
    assert "Hello World. Type 'exit' to exit." in out
    assert "Cannot divide by zero." in out
    assert "Exiting..." in out

def test_app_invalid_input(capfd, monkeypatch):
    """Test how the REPL handles invalid input for arithmetic operations."""
    inputs = iter(['add a b', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, err = capfd.readouterr()

    # Check that the invalid input error message is printed
    assert "Hello World. Type 'exit' to exit." in out
    assert "Invalid input. Usage: add <num1> <num2>" in out
    assert "Exiting..." in out

def test_app_missing_add_arguments(capfd, monkeypatch):
    """Test how the REPL handles the 'add' command with missing arguments."""
    inputs = iter(['add', 'exit'])  # No arguments
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, err = capfd.readouterr()

    assert "Hello World. Type 'exit' to exit." in out
    assert "Invalid input. Usage: add <num1> <num2>" in out
    assert "Exiting..." in out

def test_app_missing_subtract_arguments(capfd, monkeypatch):
    """Test how the REPL handles the 'subtract' command with missing arguments."""
    inputs = iter(['subtract', 'exit'])  # No arguments
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, err = capfd.readouterr()

    assert "Hello World. Type 'exit' to exit." in out
    assert "Invalid input. Usage: subtract <num1> <num2>" in out
    assert "Exiting..." in out

def test_app_missing_multiply_arguments(capfd, monkeypatch):
    """Test how the REPL handles the 'multiply' command with missing arguments."""
    inputs = iter(['multiply', 'exit'])  # No arguments
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, err = capfd.readouterr()

    assert "Hello World. Type 'exit' to exit." in out
    assert "Invalid input. Usage: multiply <num1> <num2>" in out
    assert "Exiting..." in out

def test_app_missing_divide_arguments(capfd, monkeypatch):
    """Test how the REPL handles the 'divide' command with missing arguments."""
    inputs = iter(['divide', 'exit'])  # No arguments
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, err = capfd.readouterr()

    assert "Hello World. Type 'exit' to exit." in out
    assert "Invalid input. Usage: divide <num1> <num2>" in out
    assert "Exiting..." in out

def test_app_add_too_many_arguments(capfd, monkeypatch):
    """Test how the REPL handles too many arguments in the 'add' command."""
    inputs = iter(['add 1 2 3', 'exit'])  # Too many arguments
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, err = capfd.readouterr()

    assert "Hello World. Type 'exit' to exit." in out
    assert "Invalid input. Usage: add <num1> <num2>" in out
    assert "Exiting..." in out

def test_app_subtract_too_many_arguments(capfd, monkeypatch):
    """Test how the REPL handles too many arguments in the 'subtract' command."""
    inputs = iter(['subtract 1 2 3', 'exit'])  # Too many arguments
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, err = capfd.readouterr()

    assert "Hello World. Type 'exit' to exit." in out
    assert "Invalid input. Usage: subtract <num1> <num2>" in out
    assert "Exiting..." in out

def test_app_multiply_too_many_arguments(capfd, monkeypatch):
    """Test how the REPL handles too many arguments in the 'multiply' command."""
    inputs = iter(['multiply 1 2 3', 'exit'])  # Too many arguments
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, err = capfd.readouterr()

    assert "Hello World. Type 'exit' to exit." in out
    assert "Invalid input. Usage: multiply <num1> <num2>" in out
    assert "Exiting..." in out

def test_app_divide_too_many_arguments(capfd, monkeypatch):
    """Test how the REPL handles too many arguments in the 'divide' command."""
    inputs = iter(['divide 1 2 3', 'exit'])  # Too many arguments
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, err = capfd.readouterr()

    assert "Hello World. Type 'exit' to exit." in out
    assert "Invalid input. Usage: divide <num1> <num2>" in out
    assert "Exiting..." in out
