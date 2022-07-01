# converting coloured image to gray scale image(black and white) using Open CV library!!!
import cv2
from tkinter.filedialog import askopenfilename
import datetime as dt
img = cv2.imread(askopenfilename(), 0)
current_dt = dt.datetime.now().strftime('%d-%m-%Y %I-%M-%S')   # this line is used to the img name in the format of date and time.
file_name = current_dt + '.jpg'
cv2.imwrite(file_name, img)

# here, the name of the saved image is in this format ('%d-%m-%Y %I-%M-%S').
cv2.destroyAllWindows()
