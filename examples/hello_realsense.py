import logging
import realsense2 as rs

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

pipeline = rs.pipeline()
pipeline.start()


def main():
    while True:
        # This is a blocking call poll_for_frames can be used for async
        frame_set = pipeline.wait_for_frames()
        depth_frame = frame_set.get_depth_frame()
        width, height = depth_frame.get_width(), depth_frame.get_heigt()
        dist_to_center = depth_frame.get_distance(width / 2, height / 2)
        logger.info("The camera is facing an object {} meters away.".format(dist_to_center))


if __name__ == "__main__":
    main()
