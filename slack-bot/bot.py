import slack
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ["xoxb-3553278435542-3583678755472-I8MIoHu3IqBRnUxd8n5SX80p"])

client.chat_postMessage(channel='#buzz-bot', text="Hello World")