import os  # Importing the os module to interact with environment variables
from openai import OpenAI
import replicate

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
REPLICATE_API_TOKEN = os.environ["REPLICATE_API_TOKEN"]
openai_client = OpenAI(api_key=OPENAI_API_KEY)
replicate_client = replicate.Client(api_token=REPLICATE_API_TOKEN)