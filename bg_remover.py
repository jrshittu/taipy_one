from PIL import Image
from rembg import remove
from taipy.gui import Gui, notify
from io import BytesIO

image_upload = ""
image_download = "removebg_img.png"
old_image = None
new_image = None
bg_removed = False

def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

def rm_bg(state):
    notify(state, 'info', 'Uploading image...')
    image = Image.open(state.image_upload)
    
    notify(state, 'info', 'Removing bg...')
    new_image = remove(image)
    new_image.save("removebg_img.png")

    notify(state, 'success', 'bg removed successfully!')
    state.old_image = convert_image(image)
    state.new_image = convert_image(new_image)
    state.bg_removed = True

page = """
# Image Background Remover {: .color-primary}
Upload an Image: <|{image_upload}|file_selector|extensions=.png,.jpg|on_action=rm_bg|> <br />
<|{old_image}|image|>
<|{new_image}|image|><br/>
<|{image_download}|file_download|label=Download Image|active={bg_removed}|>
"""

Gui(page).run(debug=True)