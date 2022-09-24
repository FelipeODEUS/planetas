import cv2

sistemaSolar = cv2.imread("solar-system.jpg")
cv2.imshow("Resultado", sistemaSolar)


Sol = "Sol"
cv2.putText(sistemaSolar, Sol,(100,80),fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1.0, color =  (248, 248, 255))
planet1 = "Mercurio"
cv2.putText(sistemaSolar, planet1,(100,190),fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 0.5, color =  (248, 248, 255))
planet2 = "Venus"
cv2.putText(sistemaSolar, planet2,(190,250),fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 0.5, color =  (248, 248, 255))
planet3 = "Terra"
cv2.putText(sistemaSolar, planet3,(290,255),fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 0.5, color =  (248, 248, 255))
planet4 = "Marte"
cv2.putText(sistemaSolar, planet4,(390,250),fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 0.5, color =  (248, 248, 255))
planet5 = "Jupiter"
cv2.putText(sistemaSolar, planet5,(490,80),fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 0.5, color =  (248, 248, 255))
planet6 = "Saturno"
cv2.putText(sistemaSolar, planet6,(690,110),fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 0.5, color =  (248, 248, 255))
planet7 = "Urano"
cv2.putText(sistemaSolar, planet7,(950,130),fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 0.5, color =  (248, 248, 255))
planet8 = "Neturno"
cv2.putText(sistemaSolar, planet8,(1100,130),fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 0.5, color =  (248, 248, 255))
cv2.imshow("Solar_systemwithname", sistemaSolar)
cv2.waitKey(0)