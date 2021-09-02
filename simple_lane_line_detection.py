import cv2
import numpy as np

def region_of_interest(image, vertices, channel_num=1):
    mask = np.zeros_like(image)
    match = (255, ) * channel_num  # make a mask color
    cv2.fillPoly(mask, vertices, match)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image


captured = cv2.VideoCapture('media/autobahn02.avi')
assert captured.isOpened(), f'something went wrong, the video can not be opened'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = captured.get(cv2.CAP_PROP_FPS)
print(fps)
width = captured.get(cv2.CAP_PROP_FRAME_WIDTH)  # for more info search 'cv2.CAP_PROP' in OpenCV Document
height = captured.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(width, height)

#  out is an instance of VideoWriter
out = cv2.VideoWriter('media/roadLaneLineDetectionOutput.avi', fourcc, fps, (int(width), int(height)))

#  remmeber that region of interest is differ case by case, so we should customize it to gain a better results.
region_of_interest_vertices = [(0, height),  (width / 2, height / 2), (width, height)]



while captured.isOpened():
    ret, frame = captured.read()
    if ret:
        cv2.imshow('origin', frame)
        width = frame.shape[1]
        height = frame.shape[0]
        # print(frame.shape)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        canny = cv2.Canny(gray, 100, 200)
        masked_img = region_of_interest(canny, np.array([region_of_interest_vertices], np.int32))
        lines = cv2.HoughLinesP(masked_img, 6, np.pi / 60, 100, lines=np.array([]), minLineLength=30, maxLineGap=5)
        result = np.copy(frame)
        if isinstance(lines, np.ndarray):
            for line in lines:
                x1, y1, x2, y2 = line[0]
                cv2.line(result, (x1, y1), (x2, y2), (00, 50, 200), 2)

        cv2.imshow('HoughLine Transform Probabilistic method with the region of interest', result)
        out.write(result)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
    else:
        break

captured.release()
cv2.destroyAllWindows()
