class ImageUploader:
    def __init__(self, dst_image_path: str):
        self.dst_image_path = dst_image_path

    def upload_image(self):
        raise NotImplementedError
