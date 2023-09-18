import io
import os
import pathlib
import PySimpleGUI as sg
from PIL import Image

def resize_image(imagepath, size=(400,500)):
    image = Image.open(imagepath)
    image = image.resize(size)
    
    image_bytes = io.BytesIO()
    image.save(image_bytes, format="PNG")
    image_bytes = image_bytes.getvalue()
    
    return image_bytes

def create_photo_window(title=None, theme="DarkTeal9"):    
    # Definindo o nosso tema
    sg.theme(theme)
    
    parent_path = str(pathlib.Path(__file__).parent.resolve())
    image = "foto_carol.png"
    
    fullpath = os.path.join(parent_path, image)
    
    image = resize_image(fullpath)

    layout = [
        [
            sg.Image(data=image, size=(400, 500)),
        ],
    ]
    
    # Definindo o titulo da janela
    if title is None:
        title = "Anjo?"
    else:
        title = title

    # Criar a janela e deixa ela finalizável
    window = sg.Window(title, layout,element_justification='center', finalize=True, )
    
    # Retorna a nossa janela
    return window
