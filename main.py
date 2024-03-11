from pathlib import Path
from image_utils.image_uploader.local_file_image_uploader import (
    LocalFileImageUploader,
)


if __name__ == "__main__":

    def initial_setup():
        Path("media").mkdir(exist_ok=True)

    initial_setup()
    LocalFileImageUploader("media/second_test.png").upload_image()
