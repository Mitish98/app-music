import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv
import os

# Carrega variáveis do arquivo .env
load_dotenv()

# Configuração usando variáveis de ambiente
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)



# Upload do arquivo MP3
response = cloudinary.uploader.upload("audios/Orlande de Lassus - Lagrime di San Pietro： I. Il magnanimo Pietro.mp3", resource_type="video")

print("URL pública:", response['secure_url'])

