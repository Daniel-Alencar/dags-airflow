from dotenv import load_dotenv
import os

variable = load_dotenv()

print(os.environ['PASSWORD'])

