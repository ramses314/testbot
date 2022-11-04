from environs import Env
import os

# Now we use the environs library instead of the python-dotenv library
env = Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')  # Taking the value of type str
ADMINS = env.list("ADMINS")  # Here we will have a list of admins
IP = env.str("ip")  # Also str, but for the IP address of the host

host = "127.0.0.1"
user = "postgres"
password = "gtx97"
db_name = "postgres"