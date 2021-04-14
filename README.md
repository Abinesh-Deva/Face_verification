# Face_verification
This is a basic project and raw code for face verification.

# Requirements
1. Python based IDE
2. Packages - 
  1. opencv
  2. face_recognition
3. Good webcam or camera
4. GPU is favoured than CPU for faster processing

# General steps in face recognition of a pre existing image
1. Import packages.
2. Load sample images  and extract face encodings : Returns a list of 128:D face encodings(one for each face in the image).
3. Create an array to save encodings, Cretae a array to save the names in same order of encodings.
4. Load an unknown image to identify faces.
5. Find all faces and face encodings in unknown image.
6. Loop through face_location and encodings.
7. Split the coordinates individually
8. Compare faces and get matches list(inside the loop):
9.  Initialize a name string(inside the loop):
10. Use first match and get name from respective index(inside loop) :
11. Draw rectangle around face(inside loop).
12. Write name below face(inside loop).
13. Display the immage with name.

# These steps can be further revamped to build a better, swfit processing and sophisticated face recognition system.

