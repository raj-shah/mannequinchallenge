import os
import glob
from util import frame_processing

BASE_FOLDER = 'test_videos'
if not os.path.exists(BASE_FOLDER):
    os.makedirs(BASE_FOLDER)

video_list = glob.glob('../test_videos/covid19/*')

for video in video_list:
    VIDEO_NAME = output_frame_folder = video.split('/')[-1].split('.')[0]
    FRAME_FOLDER = os.path.join(BASE_FOLDER, VIDEO_NAME)

    if not os.path.exists(FRAME_FOLDER):
        os.makedirs(FRAME_FOLDER)

    frame_rate = frame_processing.video_to_frames(video, FRAME_FOLDER)

    break