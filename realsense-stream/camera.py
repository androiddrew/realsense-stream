import logging

import cv2
import numpy as np
import pyrealsense2 as rs

logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

COLORIZER = rs.colorizer()


def config_cam_pipeline():
    logger.info("Configuring Camera Pipeline")
    config = rs.config()
    pipeline = rs.pipeline()
    config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 30)
    logger.info("Enabling depth stream")
    pipeline.start(config)
    return pipeline


def save_frame(pipeline, path=None):
    _path = path if not None else '.'
    logger.info("Saving Frame")
    frames = pipeline.wait_for_frames()
    depth_frame = frames.get_depth_frame()
    colorized = COLORIZER.process(depth_frame)
    depth_image = np.asanyarray(colorized.get_data())
    cv2.imwrite("Testingimage.png", depth_image)
    logger.info("Image Saved")


def main():
    pipeline = config_cam_pipeline()
    save_frame(pipeline)
    pipeline.stop()


if __name__ == "__main__":
    main()


