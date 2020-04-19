import os
import cv2
import time

# requires system packages libx264-dev, libx265-dev, x264, x265
OPENCV_PY_MP4_CODEC = 0x7634706d

def video_to_frames(input_video, output_folder):
    '''
    Splits the Input Video to Frames
    :param input_video: The path of the input video (Should be 30fps as an apriori check)
    '''

    # If the output folders for visualization and processing do not exist, create them
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Initialize the Object for Frame Extraction
    vidcap = cv2.VideoCapture(input_video)

    # Get frame rate
    FRAME_RATE = vidcap.get(cv2.CAP_PROP_FPS)

    count = 0
    success = True
    while success:
        try:
            # Read frame and get the shape
            success, image = vidcap.read()

            if image is not None:
                # Write the image
                cv2.imwrite(os.path.join(output_folder, "{}.jpg".format(count)), image)

            # Increment the count
            count = count + 1

        except Exception as exc:
            print('error extracting frame {}. error: {}'.format(count, exc))

    vidcap.release()

    return FRAME_RATE


def frames_to_video(frames_folder, output_video_path, frame_rate):

    frame_list = os.listdir(frames_folder)

    img = cv2.imread(frame_list[0])
    height, width, layers = img.shape
    size = (width, height)

    out = cv2.VideoWriter(
        output_video_path, OPENCV_PY_MP4_CODEC, frame_rate, size)

    for img_name in frame_list:
        try:
            img = cv2.imread(img_name)
            out.write(img)

        except Exception as exc:
            print('error stitching. error {}'.format(exc))
            break

    out.release()