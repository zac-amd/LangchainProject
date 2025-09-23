from dotenv import load_dotenv
import os

load_dotenv()
def main():
    print("Hello from langchainproject!")
    print(os.getenv('OPEN_API_KEY'))

if __name__ == "__main__":
    main()
