import os
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())
OPENAI_API_KEY = os.environ.get("OPEN_AI_KEY")

if __name__ == '__main__':
    print("\nHello World!")


