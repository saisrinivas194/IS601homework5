class App:
    @staticmethod
    def start() -> None:
        print("Hello World. Type 'exit' to exit.")

        while True:
            user_input = input(">>> ").strip().lower()

            if user_input == "exit":
                print("Exiting...")
                break
            elif user_input.startswith("add"):
                try:
                    _, x, y = user_input.split()
                    result = float(x) + float(y)
                    print(f"Result: {result}")
                except ValueError:
                    print("Invalid input. Usage: add <num1> <num2>")
            elif user_input.startswith("subtract"):
                try:
                    _, x, y = user_input.split()
                    result = float(x) - float(y)
                    print(f"Result: {result}")
                except ValueError:
                    print("Invalid input. Usage: subtract <num1> <num2>")
            elif user_input.startswith("multiply"):
                try:
                    _, x, y = user_input.split()
                    result = float(x) * float(y)
                    print(f"Result: {result}")
                except ValueError:
                    print("Invalid input. Usage: multiply <num1> <num2>")
            elif user_input.startswith("divide"):
                try:
                    _, x, y = user_input.split()
                    if float(y) == 0:
                        print("Cannot divide by zero.")
                    else:
                        result = float(x) / float(y)
                        print(f"Result: {result}")
                except ValueError:
                    print("Invalid input. Usage: divide <num1> <num2>")
            else:
                print("Unknown command. Type 'exit' to exit.")
