import cv2
import numpy as np


def nothing(x):
    pass


cap = cv2.VideoCapture(0)
cv2.namedWindow("TrackbarsR")
cv2.createTrackbar("L - H", "TrackbarsR", 0, 255, nothing)
cv2.createTrackbar("L - S", "TrackbarsR", 0, 179, nothing)
cv2.createTrackbar("L - V", "TrackbarsR", 0, 255, nothing)
cv2.createTrackbar("U - H", "TrackbarsR", 255, 255, nothing)
cv2.createTrackbar("U - S", "TrackbarsR", 255, 179, nothing)
cv2.createTrackbar("U - V", "TrackbarsR", 255, 255, nothing)
cv2.namedWindow("TrackbarsG")
cv2.createTrackbar("L - H", "TrackbarsG", 0, 255, nothing)
cv2.createTrackbar("L - S", "TrackbarsG", 0, 255, nothing)
cv2.createTrackbar("L - V", "TrackbarsG", 0, 179, nothing)
cv2.createTrackbar("U - H", "TrackbarsG", 255, 255, nothing)
cv2.createTrackbar("U - S", "TrackbarsG", 255, 255, nothing)
cv2.createTrackbar("U - V", "TrackbarsG", 255, 179, nothing)
cv2.namedWindow("TrackbarsB")
cv2.createTrackbar("L - H", "TrackbarsB", 0, 179, nothing)
cv2.createTrackbar("L - S", "TrackbarsB", 0, 255, nothing)
cv2.createTrackbar("L - V", "TrackbarsB", 0, 255, nothing)
cv2.createTrackbar("U - H", "TrackbarsB", 255, 255, nothing)
cv2.createTrackbar("U - S", "TrackbarsB", 255, 255, nothing)
cv2.createTrackbar("U - V", "TrackbarsB", 255, 255, nothing)


while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_hR = cv2.getTrackbarPos("L - H", "TrackbarsR")
    l_sR = cv2.getTrackbarPos("L - S", "TrackbarsR")
    l_vR = cv2.getTrackbarPos("L - V", "TrackbarsR")
    u_hR = cv2.getTrackbarPos("U - H", "TrackbarsR")
    u_sR = cv2.getTrackbarPos("U - S", "TrackbarsR")
    u_vR = cv2.getTrackbarPos("U - V", "TrackbarsR")
    l_hG = cv2.getTrackbarPos("L - H", "TrackbarsG")
    l_sG = cv2.getTrackbarPos("L - S", "TrackbarsG")
    l_vG = cv2.getTrackbarPos("L - V", "TrackbarsG")
    u_hG = cv2.getTrackbarPos("U - H", "TrackbarsG")
    u_sG = cv2.getTrackbarPos("U - S", "TrackbarsG")
    u_vG = cv2.getTrackbarPos("U - V", "TrackbarsG")
    l_hB = cv2.getTrackbarPos("L - H", "TrackbarsB")
    l_sB = cv2.getTrackbarPos("L - S", "TrackbarsB")
    l_vB = cv2.getTrackbarPos("L - V", "TrackbarsB")
    u_hB = cv2.getTrackbarPos("U - H", "TrackbarsB")
    u_sB = cv2.getTrackbarPos("U - S", "TrackbarsB")
    u_vB = cv2.getTrackbarPos("U - V", "TrackbarsB")

    lowerR = np.array([l_hR, l_sR, l_vR])
    upperR = np.array([u_hR, u_sR, u_vR])
    maskR = cv2.inRange(hsv, lowerR, upperR)
    lowerG = np.array([l_hG, l_sG, l_vG])
    upperG = np.array([u_hG, u_sG, u_vG])
    maskG = cv2.inRange(hsv, lowerG, upperG)
    lowerB = np.array([l_hB, l_sB, l_vB])
    upperB = np.array([u_hB, u_sB, u_vB])
    maskB = cv2.inRange(hsv, lowerB, upperB)
    maskF = 255*(maskR//255|maskG//255|maskB//255)

    resultR = cv2.bitwise_and(frame, frame, mask=maskR)
    resultG = cv2.bitwise_and(frame, frame, mask=maskG)
    resultB = cv2.bitwise_and(frame, frame, mask=maskB)
    resultF = cv2.bitwise_and(frame, frame, mask=maskF)


    cv2.imshow("frame", frame)
    cv2.imshow("maskR", maskR)
    cv2.imshow("resultR", resultR)
    cv2.imshow("maskG", maskG)
    cv2.imshow("resultG", resultG)
    cv2.imshow("maskB", maskB)
    cv2.imshow("resultB", resultB)
    cv2.imshow("resultF", resultF)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
