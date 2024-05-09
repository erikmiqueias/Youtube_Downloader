from pytube import YouTube
import os
from pywebio.input import *
from pywebio.output import *

def download(link: str, quality, path):
    if link.split("//")[0] == "https:":
        url = YouTube(link)
        video = url.streams.get_by_resolution(quality)
        video.download(path)
        return True
    return False
        
def main():
    PATH = "/home/erik_miqueias/Downloads"
    while True:
        link = input("Digite o link do vídeo que deseja baixar: ")
        quality = input("Digite a qualidade [720p, 480p, 360p, 240p, 144p]: ")
        put_text(f"Fazendo o download do vídeo...".title()).style("color: yellow; font-size: 50px;")
        
        verification = download(link, quality, PATH)
        if verification == True:
            download(link, quality, PATH)
            put_text("Video baixado com sucesso :)".title()).style("color: green; font-size: 50px;")
            
        else:
            put_text("Falha no download do video :(".title()).style("color: red; font-size: 50px;")
            
if __name__ == "__main__":
    main()
        

                
        

    
        