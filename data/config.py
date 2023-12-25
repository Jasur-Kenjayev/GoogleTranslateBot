from environs import Env


env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN") 
ADMINS = env.list("ADMINS") 
IP = env.str("ip") 

CHANNELS = ["-1001772783109"] #CHANEL ID
