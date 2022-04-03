import face_recognition
import cv2
import numpy as np
import pickle
import time

class Scan:
    def __init__(self):
        self.classRoster = {}

    def getFontScale(self, text, width):
        for scale in reversed(range(0, 60, 1)):
            textSize = cv2.getTextSize(text, fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=scale/10, thickness=2)
            newScale = textSize[0][0]
            if (newScale <= width):
                return scale/10

    def scan(self, video_capture, known_face_encodings, known_face_names, ref_dict):
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True

        start = time.time()
        prevName = ''
        while True  :   
            ret, frame = video_capture.read()
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]
            if process_this_frame:
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
                face_names = []
                for face_encoding in face_encodings:
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "Unknown"
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    print(f"len of face distances {len(face_distances)}")
                    best_match_index = np.argmin(face_distances)
                    #print(best_match_index)
                    if matches[best_match_index]:
                        name = known_face_names[best_match_index]
                    face_names.append(name)
            process_this_frame = not process_this_frame
            
            padding = 15
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4
                cv2.rectangle(frame, (left - padding, top - padding), (right + padding, bottom + padding), (0, 255, 0), 2)
                cv2.rectangle(frame, (left - 15, bottom - 10), (right + 15, bottom + 35), (0, 255, 0), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                if name == "Unknown":
                    cv2.putText(frame, name, (left + 6, bottom + 15), font, 0.7, (255, 255, 255), 1)
                    start = time.time() #resets the timer
                else:
                    if name != prevName:
                        start = time.time()
                    prevName = name
                    cv2.putText(frame, ref_dict[name], (left + 6, bottom + 20), font, self.getFontScale(ref_dict[name], right - left), (255, 255, 255), 1)
                    end = time.time() #end of timer
                    print(end - start)
                    if (end - start >= 2):
                        print(ref_dict[name])
                        self.classRoster[ref_dict[name]] = True

            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.imshow('Live Video', frame)
            
            if cv2.waitKey(1) == ord('q'):
                break
    def showClassRoster(self):
        print(self.classRoster)

    def start(self):
        f=open("names.pkl","rb")
        ref_dict=pickle.load(f)        
        f.close()
        f=open("embed.pkl","rb")
        embed_dict=pickle.load(f)      
        f.close()

        for key, name in ref_dict.items():
            self.classRoster[name] = False #False means absent; True means present
        print(ref_dict)
        self.showClassRoster()
        known_face_encodings = []  
        known_face_names = []  
        for ref_id , embed_list in embed_dict.items():
            for my_embed in embed_list:
                known_face_encodings +=[my_embed]
                known_face_names += [ref_id]
        # print(len(known_face_encodings))
        # print(len(known_face_names))

        video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.scan(video_capture, known_face_encodings, known_face_names, ref_dict)
        video_capture.release()
        self.showClassRoster()
        cv2.destroyAllWindows()