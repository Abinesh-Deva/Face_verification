#import requied libraries for face detection and face recognition
import cv2
import face_recognition


#create a function and self call it until the selfie is detecting requied faces for recognition.
def run_process():
#using VideoCapture class available in cv2 package, we can capture video from images,videos or cameras. index 0 defines default camera attached in running desktop.
    webcam_stream=cv2.VideoCapture(0)
#create a array to store all face locations detected during capturing image.
    all_face_locations_in_stream=[]
#create a while loop to run each and every frame from streaming video
    while True:
#Get a single frame from the streaming video to detect.
        ret,current_frame=webcam_stream.read()
        ret2,captured_frame=webcam_stream.read()     
#resize the current_frame to process much faster
        current_frame_resized = cv2.resize(current_frame,(0,0),fx=0.25,fy=0.25)
#store all the locations detected in the array that we declared earlier
        all_face_locations_in_stream=face_recognition.face_locations(current_frame_resized,number_of_times_to_upsample=2,model="hog")
#create a for loop to run through each and every face detected in this current_frame
        for index,current_face_coords in enumerate(all_face_locations_in_stream):
#get the individual coordinates of each face using tuple unpacking
            top_coord,right_coord,bottom_coord,left_coord=current_face_coords
#resize the coordinates to match the orginial coords in the current frame.
            bottom_coord=bottom_coord*4
            top_coord=top_coord*4
            left_coord=left_coord*4
            right_coord=right_coord*4
#draw a rectangle around each face detected
            cv2.rectangle(current_frame,(left_coord,top_coord),(right_coord,bottom_coord),(0,0,225),2)
#declare font style and display text in live stream to inform users and get a input
            font_style1=cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(current_frame,"press q to capture",(200,450),font_style1,1,(225,225,225),2)
        cv2.imshow("Live video",current_frame)
#set code such that when user presses a key, while loop to end. else it is going to be a infinite loop. 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
#once the while loop is terminated, release the webcam and destroy all windows opened, using the below mentioned methods
    webcam_stream.release()
    cv2.destroyAllWindows()
    (h,w)=captured_frame.shape[:2]
#now the final image captured is stored as current_frame or, the final image 
#captured is the final frame that the while loop accepted and ran before the user pressed a key to end the loop.

#now store all the face locations in the image captured
    all_face_locations=face_recognition.face_locations(captured_frame,model="hog")
#set condtion such that, if exactly two faces are deteceted as what is required in our program, start encoding the face. 
#Else call the function again to capture a image again and again until the condition is met.
    if len(all_face_locations)<=1 or len(all_face_locations)>2:
        run_process() #call the function again
    else:
        #once the captured image has two faces to detect, display the captured image and ask for further input from user to start verification
        cv2.putText(captured_frame,"Press any key to verify",(200,450),font_style1,1,(225,225,225),2)
        cv2.imshow("Captured image",captured_frame)
        if cv2.waitKey():
            cv2.destroyAllWindows()
#start encoding the faces available in captured image and store it in a array for later comparison
            all_face_encodings=face_recognition.face_encodings(captured_frame,all_face_locations)
#beauty of python and the available packages. Compare the following faces in the captured image which are stored as encodings and store the result.
            m=face_recognition.compare_faces([all_face_encodings[0]],all_face_encodings[-1])
#display the verififcation result.
            if True in m:
                cv2.putText(captured_frame,"Identification Successfull",(200,h//2),font_style1,1,(0,225,0),4)
                cv2.imshow("Result",captured_frame)
            else:
                cv2.putText(captured_frame,"Identification Failure",(200,h//2),font_style1,1,(0,0,225),4)
                cv2.imshow("Result",captured_frame)

#this is a direct call method to start the fuction to run.
run_process()

 # This is a simple face recognition or face verification code to recognize two faces and display result.