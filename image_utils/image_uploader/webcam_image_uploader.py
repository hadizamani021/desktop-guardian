import shutil
from image_utils.image_uploader.image_uploader import ImageUploader
from image_utils.webcam_utils import WebcamUtils


class WebcamImageUploader(ImageUploader):
    def upload_image(self):
        path = WebcamUtils.take_picture()
        shutil.copy(path, self.dst_image_path)
