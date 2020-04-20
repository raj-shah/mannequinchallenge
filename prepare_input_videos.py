import os
import glob
import frame_processing

BASE_FOLDER = 'test_videos'
if not os.path.exists(BASE_FOLDER):
    os.makedirs(BASE_FOLDER)

FRAME_LISTS = 'frame_lists'
if not os.path.exists(FRAME_LISTS):
    os.makedirs(FRAME_LISTS)

video_list = glob.glob('../test_videos/covid19/*')
total_videos = len(video_list)

for idx, video in enumerate(video_list):
    VIDEO_NAME = output_frame_folder = video.split('/')[-1].split('.')[0]

    FRAME_FOLDER = os.path.join(BASE_FOLDER, VIDEO_NAME)
    if not os.path.exists(FRAME_FOLDER):
        os.makedirs(FRAME_FOLDER)

    FRAME_FOLDER_SUB = os.path.join(FRAME_FOLDER, 'frames')

    frame_rate = frame_processing.video_to_frames(video, FRAME_FOLDER_SUB)

    print('Processing [{:02d}/{:02d}]: {}'.format((idx + 1), total_videos, VIDEO_NAME))
    print('\tframe rate: {}'.format(frame_rate))

    fw = open(os.path.join(FRAME_LISTS, '{}.txt'.format(VIDEO_NAME)), 'w')
    frames = glob.glob("{}/*.*".format(FRAME_FOLDER_SUB))
    frames_sorted = sorted(frames, key=lambda x: int(os.path.splitext(x.split('/')[-1])[0]))
    [fw.write(x + '\n') for x in frames_sorted]
    fw.close()