import glob
import cv2

video_list = glob.glob('../test_videos/covid19/*')

for video in video_list:
    VIDEO_NAME = video.split('/')[-1].split('.')[0]

    vidcap = cv2.VideoCapture(video)
    FRAME_RATE = vidcap.get(cv2.CAP_PROP_FPS)
    vidcap.release()

    print('{}'.format(VIDEO_NAME))
    print('\t\tfps: {}'.format(FRAME_RATE))

