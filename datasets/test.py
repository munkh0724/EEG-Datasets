import webbrowser
import time 
# Specify the path to your GIF image
image_path1 = "C://EEG_DATA_COLLECTION//1_EEG_DATA_COLLECTION-LIGHT//lon.gif"
image_path2 = "C://EEG_DATA_COLLECTION//1_EEG_DATA_COLLECTION-LIGHT//lox.gif"

# Open the GIF image in the default web browser
webbrowser.open(image_path1)
time.sleep(6);
webbrowser.open(image_path2)
time.sleep(6);