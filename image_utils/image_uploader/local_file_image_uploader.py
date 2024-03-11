import shutil
from tkinter.filedialog import askopenfilename


class LocalFileImageUploader:
    def __init__(self, dst_image_path: str):
        self.dst_image_path = dst_image_path

    def upload_image(self):
        path = askopenfilename(filetypes=[("Image File", ".jpg .png .jpeg")])
        shutil.copy(path, self.dst_image_path)
