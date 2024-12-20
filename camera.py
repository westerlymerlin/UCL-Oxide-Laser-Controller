
"""
Camera module, configures the webcam if it is avaialbe uses the
cv2 library from opencv-python-headless
Author: Gary Twinn
"""


import cv2
from logmanager import logger
from app_control import settings


class VideoCamera():
    """
    Initializes the VideoCamera class.

    The constructor creates a VideoCapture object, which represents the video source. It sets the video source
    properties, such as frame rate, width, height, brightness, and contrast. If no video camera is found, an
    error message is logged.

    """
    def __init__(self):
        self.video = cv2.VideoCapture(settings['cameraID'])
        if not self.video.isOpened():
            logger.error('VideoCameraClass: No video camera found')
        else:
            logger.info('VideoCameraClass: Starting video camera')
            self.video.set(cv2.CAP_PROP_FPS, settings['cameraFPS'])
            self.video.set(cv2.CAP_PROP_FRAME_WIDTH, settings['cameraWidth'])
            self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, settings['cameraHeight'])
            self.video.set(cv2.CAP_PROP_BRIGHTNESS, settings['cameraBrightness'])
            self.video.set(cv2.CAP_PROP_CONTRAST, settings['cameraContrast'])
            logger.info('Video FPS %s', self.video.get(cv2.CAP_PROP_FPS))
            logger.info('Video Width %s', self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
            logger.info('Video Height %s', self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))
            logger.info('Video Backend %i', self.video.get(cv2.CAP_PROP_BACKEND))
            logger.info('Video Brightness %i', self.video.get(cv2.CAP_PROP_BRIGHTNESS))
            logger.info('Video Contrast %i', self.video.get(cv2.CAP_PROP_CONTRAST))

    def __del__(self):
        """Releases resources when app is closed down"""
        self.video.release()

    def get_frame(self):
        """Get a stream of raw images and encode asjpg files"""
        ret, frame = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
