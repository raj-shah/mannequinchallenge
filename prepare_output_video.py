import os
import glob
import cv2
import argparse

# requires system packages libx264-dev, libx265-dev, x264, x265
OPENCV_PY_MP4_CODEC = 0x7634706d

def frames_to_video(frames_folder, output_video_path, frame_rate):

    frame_list = glob.glob(os.path.join(frames_folder, '*'))

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

RESULTS_FOLDER = 'viz_predictions'

parser = argparse.ArgumentParser()
parser.add_argument('--out_frames', type=str, help='output frames')
parser.add_argument('--frame_rate', type=int, help='frame rate')
args = parser.parse_args()

VIDEO_NAME = args.out_frames.split('/')[1]
VIDEO_PATH = os.path.join(RESULTS_FOLDER, VIDEO_NAME, '{}.mp4'.format(VIDEO_NAME))

print('Processing {}'.format(VIDEO_NAME))
print('\toutput video: {}'.format(VIDEO_PATH))

frames_to_video(args.out_frames, VIDEO_PATH, args.frame_rate)
