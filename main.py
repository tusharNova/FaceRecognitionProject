import cv2
print(cv2.__version__)  # Check OpenCV version

# Check if face module is available
if hasattr(cv2, 'face'):
    print("cv2.face module is available!")
else:
    print("cv2.face module is missing!")
