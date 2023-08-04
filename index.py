import gradio as gr
from gradio.components import File, Gallery, Image
from PIL import Image as PILImage
import rarfile
import zipfile
import os
import numpy as np

def read_comic_book(comic_file):
    with open(comic_file.name, "wb") as f:
        f.write(comic_file.read())
    
    images = []
    if comic_file.name.lower().endswith('.cbr'):
        with rarfile.RarFile(comic_file.name) as archive:
            for entry in archive.infolist():
                if entry.filename.lower().endswith(('jpg', 'jpeg', 'png')):
                    image = Image.open(archive.open(entry))
                    images.append(np.array(image))
    elif comic_file.name.lower().endswith('.cbz'):
        with zipfile.ZipFile(comic_file.name) as archive:
            for entry in archive.infolist():
                if entry.filename.lower().endswith(('jpg', 'jpeg', 'png')):
                    image = Image.open(archive.open(entry))
                    images.append(np.array(image))  
    
    return images

iface = gr.Interface(
    fn=read_comic_book,
    inputs=File(type="file"),
    outputs=Gallery(),  # Removed type and plot parameters
    live=True,
    examples=[["/workspaces/cbreadergradio/examples/KTR2.cbr"], ["/workspaces/cbreadergradio/examples/KTR1.cbz"]],
    allow_flagging='never'
)

iface.launch()