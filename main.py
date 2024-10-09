# main.py
from app import App    

def main():
    """Main entry point of the application."""
    try:
        App.start()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
