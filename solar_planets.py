import cv2

sistemaSolar = cv2.imread("solar-system.jpg")
cv2.imshow("Resultado", sistemaSolar)
cv2.waitKey(0)

Sol = "Sol"
cv2.putText(sistemaSolar, Sol,(100,80),fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1.0, color =  (248, 248, 255))

cv2.imshow("Solar_systemwithname", sistemaSolar)
cv2.waitKey(0)