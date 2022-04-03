import cv2 
import face_recognition
import pickle

class Add_Classmate:
    def __init__(self):
        pass

    def captureImages(self, embed_dict : dict, ref_id):
        for i in range(5):
            key = cv2. waitKey(1)
            webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            exitCapture = False
            while True:
                check, frame = webcam.read()
                cv2.imshow("Capturing", frame)
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
                rgb_frame = small_frame[:, :, ::-1]
        
                key = cv2.waitKey(1)
                if key == ord('s') : 
                    face_locations = face_recognition.face_locations(rgb_frame)
                    if face_locations != []:
                        face_encoding = face_recognition.face_encodings(frame)[0]
                        if ref_id in embed_dict:
                            embed_dict[ref_id]+=[face_encoding]
                        else:
                            embed_dict[ref_id]=[face_encoding]
                        webcam.release()
                        cv2.waitKey(1)
                        cv2.destroyAllWindows()     
                        break
                elif key == ord('q'):
                    print("Turning off camera.")
                    webcam.release()
                    print("Camera off.")
                    print("Program ended.")
                    cv2.destroyAllWindows()
                    break
                elif key == ord('x'):
                    print("Program terminated.")
                    cv2.destroyAllWindows()
                    exitCapture = True
                    break
            if exitCapture:
                webcam.release() 
                break
    def start(self):
        try:
            f=open("names.pkl","rb")
            ref_dict=pickle.load(f)
            f.close()
        except:
            ref_dict={}

        print("Class List:")
        i = 1
        for key, value in ref_dict.items():
            print(f'{i}: {value}')
            i += 1

        name=input("Enter name of classmate: ")
        if name in ref_dict.values():
            for key, temp in ref_dict.items():
                if (name == temp):
                    ref_id = key
                    break
        else:
            ref_id = i

        ref_dict[ref_id]=name
        f=open("names.pkl","wb")
        pickle.dump(ref_dict,f)
        f.close()

        try:
            f=open("embed.pkl","rb")
            embed_dict=pickle.load(f)
            f.close()
        except:
            embed_dict={}

        self.captureImages(embed_dict, ref_id)

        f=open("embed.pkl","wb")
        pickle.dump(embed_dict,f)
        f.close()