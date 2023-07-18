import cv2
import face_recognition
import pickle
from datetime import datetime

cap = cv2.VideoCapture(0)

# Set the  image width and height
width, height = 320, 240

cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

face_cascade = cv2.CascadeClassifiter("haar_cascade_files/haarcascade_frontalface_default.xml")

name = input("Entere your name: ")
access_input = input("Enter room access (comma-separated): ")
access_list = access_input.split(",")


face_data = []
capture_count = 0


while True:
	
	ret, frame = cap.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BRG2GRAY)

	faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.3, minNeighbors = 5, minSize = (30,30))
	

	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x,y), (x + w, y + w), (0, 255, 0), 2)
		
		rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGE2RGB)
		face_encodings = face_recognition.face_encodings(rgb_frame, [(y,x + w, y + w + x)]

		for face_encoding in face_encodings:
			face_data.append({
				"name" : name,
				"face" : frame[y:y + h, x:x + w], 
				"face_encoding": face_encoding,
				"access": access_list
				})

	#display the frame
	cv2.imshow("Register Face", frame)

	if cv2.waitKey(1) & 0xFF == ord('s'):
		capture_count += 1
		print(f"Capture {capture_count} complete!")
	

	if capture_count >= 5:
		break




cap.release()
cv2.destroyAllWindows()

now = datetime.now()
file_name = f"faces/{now.strftime('%Y-%m-%d-%H-%s')} - {name.pickle}"
with open(file_name, "wb") as f:
	pickle.dump(face_data, f)

print(f"Face data for '{name}' saved successfully!")




	


