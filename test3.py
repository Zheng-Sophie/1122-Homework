import cv2
def image_process(src):
    dstx = cv2.Sobel(src, cv2.CV_32F, 1, 0)
    dsty = cv2.Sobel(src, cv2.CV_32F, 0, 1)
    dstx = cv2.convertScaleAbs(dstx)
    dsty = cv2.convertScaleAbs(dsty)
    dst = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)
    cv2.imwrite('sobel_processing.jpg', dst)