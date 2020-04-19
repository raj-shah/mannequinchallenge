import os
import glob
import cv2
import frame_processing

BASE_FOLDER = 'test_videos'
VIZ_FOLDER = 'viz_predictions'
RESULTS_FOLDER = os.path.join(BASE_FOLDER, VIZ_FOLDER)

video_list = glob.glob('test_videos/viz_predictions/*')

total_videos = len(video_list)

for idx, video in enumerate(video_list):
    VIDEO_NAME = video.split('/')[-1].split('.')[0]
    vidcap = cv2.VideoCapture(os.path.join('../test_videos/covid19', '{}.mp4'.format(VIDEO_NAME)))
    FRAME_RATE = vidcap.get(cv2.CAP_PROP_FPS)
    vidcap.release()

    print('Processing [{:02d}/{:02d}]: {} | FPS: {}'.format((idx + 1), total_videos, video, FRAME_RATE))

    OUTPUT_FRAME_FOLDER = os.path.join(RESULTS_FOLDER, VIDEO_NAME, 'output_frames')
    OUTPUT_VIDEO = os.path.join(RESULTS_FOLDER, VIDEO_NAME, '{}.mp4'.format(VIDEO_NAME))

    frame_processing.frames_to_video(OUTPUT_FRAME_FOLDER, OUTPUT_VIDEO, FRAME_RATE)
