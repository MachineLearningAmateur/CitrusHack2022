import sys
import cv2
import face_recognition
import pickle
import uuid

def CaptureImage(ref_id : str, embed_dict : dict):
    for i in range(5):
        key = cv2.waitKey(1)
        webCam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        temp = False 

        while True:
            success, frame = webCam.read() #stores check and frame with the returns of .read() 
            #print(success)
            cv2.imshow("Capturing", frame) #shows the image
            small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]

            key = cv2.waitKey(1)
        
            if key == ord('s'):
                face_locations = face_recognition.face_locations(rgb_small_frame)
                if face_locations != []:
                    face_encoding = face_recognition.face_encodings(frame)
                    if ref_id in embed_dict:
                        embed_dict[ref_id] += [face_encoding]
                    else:
                        embed_dict[ref_id] = [face_encoding]
                    webCam.release()
                    cv2.waitKey(1)
                    cv2.destroyAllWindows()
                    break
            elif key == ord('q'):
                print("Turning off camera.")
                webCam.release()
                print("Camera off.")
                print("Data collection has been terminated.")
                cv2.destroyAllWindows()
                break
            elif key == ord('x'):
                print("Early Termination")
                temp = True
                cv2.destroyAllWindows()
                break
        if (temp):
            break
            
                    
name = input('Enter name of Subject: ')
ref_id = str(uuid.uuid1()) #do I need a unique id

f = open("references.txt", "w")
f.write(f'{ref_id}, {name}')
f.close()


try: #checks to see if an instance of references.pk1 exists
    f = open("references.pkl", "rb")
    ref_dict = pickle.load(f)
    f.close()
except:
    ref_dict={} #if not create the dict
print(type(ref_id))
print(type(ref_dict))
#ref_dict[ref_id] = name

f = open("references.pkl", "wb")
pickle.dump(ref_dict, f)
f.close()

try:
    f = open("{name}_embed.pkl", "rb")
    embed_dict = pickle.load(f)
    f.close()
except:
    embed_dict = {}

CaptureImage(ref_id, embed_dict)

f = open("ref_embed.pkl","wb") 
pickle.dump(embed_dict, f) #dumps the collected embed data from the loop into the embed_dict
print(embed_dict)
f.close()


