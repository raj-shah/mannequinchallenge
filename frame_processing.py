import os
import cv2

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
    FRAME_RATE = int(vidcap.get(cv2.CAP_PROP_FPS))

    # count = 0
    # success = True
    # while success:
    #     try:
    #         # Read frame and get the shape
    #         success, image = vidcap.read()
    #
    #         if image is not None:
    #             # Write the image
    #             cv2.imwrite(os.path.join(output_folder, "{}.jpg".format(count)), image)
    #
    #         # Increment the count
    #         count = count + 1
    #
    #     except Exception as exc:
    #         print('error extracting frame {}. error: {}'.format(count, exc))

    vidcap.release()

    return FRAME_RATE
