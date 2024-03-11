import uuid
import cv2


class WebcamUtils:
    @staticmethod
    def take_picture(cam_id: int = 0) -> str:
        tmp_file = f"/tmp/{str(uuid.uuid4())[:6]}.png"
        webcam = cv2.VideoCapture(cam_id)
        try:
            while True:
                _, frame = webcam.read()
                cv2.imshow("Capturing", frame)
                key = cv2.waitKey(1)
                if key != -1:
                    cv2.destroyAllWindows()
                    cv2.imwrite(filename=tmp_file, img=frame)
                    return tmp_file
        finally:
            webcam.release()
