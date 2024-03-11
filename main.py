from pathlib import Path
from image_utils.image_uploader.webcam_image_uploader import (
    WebcamImageUploader,
)


if __name__ == "__main__":

    def initial_setup():
        Path("media").mkdir(exist_ok=True)

    initial_setup()
    WebcamImageUploader("media/first_test.png").upload_image()
