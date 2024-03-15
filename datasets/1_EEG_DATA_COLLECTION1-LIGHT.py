# ############################## LON ############################################  
# import time
# from pylsl import StreamInlet, resolve_stream
# import csv
# import numpy as np
# import webbrowser

# streams = resolve_stream('type', 'EEG') 
# inlet = StreamInlet(streams[0])
# f = open('C:/EEG_DATA_COLLECTION/1_EEG_DATA_COLLECTION-LIGHT/Volunteer_7/lonc0.csv', 'w')   
# writer = csv.writer(f)
# img1 = "C:/EEG_DATA_COLLECTION/1_EEG_DATA_COLLECTION-LIGHT/as.gif"
# img2 = "C:/EEG_DATA_COLLECTION/1_EEG_DATA_COLLECTION-LIGHT/lox.gif"
# img3 = "C:/EEG_DATA_COLLECTION/1_EEG_DATA_COLLECTION-LIGHT/untar.gif"
# data=[]
# for i in range(10):
#     webbrowser.open(img1)
#     timeout = 6
#     timeout_start = time.time()
#     while time.time() < timeout_start + timeout:
#         sample, timestamp = inlet.pull_sample()
#         if timestamp != None:
#             data = np.array(sample[:])
#             y=1
#             data=np.append(data, y, axis=None)
#             writer.writerow(data)
# f.close()


# ############################### LOX ###########################################
# import time
# from pylsl import StreamInlet, resolve_stream
# import csv
# import numpy as np
# import webbrowser

# streams = resolve_stream('type', 'EEG') 
# inlet = StreamInlet(streams[0])
# f = open('C:/EEG_DATA_COLLECTION/1_EEG_DATA_COLLECTION-LIGHT/Volunteer_7/loxc0.csv', 'w')   
# writer = csv.writer(f)
# img1 = "C:/EEG_DATA_COLLECTION/1_EEG_DATA_COLLECTION-LIGHT/as.gif"
# img2 = "C:/EEG_DATA_COLLECTION/1_EEG_DATA_COLLECTION-LIGHT/lox.gif"
# img3 = "C:/EEG_DATA_COLLECTION/1_EEG_DATA_COLLECTION-LIGHT/untar.gif"
# data=[]
# for i in range(10):
#     webbrowser.open(img2)
#     timeout = 6
#     timeout_start = time.time()
#     while time.time() < timeout_start + timeout:
#         sample, timestamp = inlet.pull_sample()
#         if timestamp != None:
#             data = np.array(sample[:])
#             y=0
#             data=np.append(data, y, axis=None)
#             writer.writerow(data)
# f.close()


# ########################### LOF ###############################################
# import time
# from pylsl import StreamInlet, resolve_stream
# import csv
# import numpy as np
# import webbrowser

# streams = resolve_stream('type', 'EEG') 
# inlet = StreamInlet(streams[0])
# f = open('C:/EEG_DATA_COLLECTION/1_EEG_DATA_COLLECTION-LIGHT/Volunteer_7/lof0.csv', 'w')   # 
# writer = csv.writer(f)
# img1 = "C:/EEG_DATA_COLLECTION/1_EEG_DATA_COLLECTION-LIGHT/as.gif"
# img2 = "C:/EEG_DATA_COLLECTION/1_EEG_DATA_COLLECTION-LIGHT/lox.gif"
# img3 = "C:/EEG_DATA_COLLECTION/1_EEG_DATA_COLLECTION-LIGHT/untar.gif"
# data=[]
# for i in range(10):
#     webbrowser.open(img3)
#     timeout = 6
#     timeout_start = time.time()
#     while time.time() < timeout_start + timeout:
#         sample, timestamp = inlet.pull_sample()
#         if timestamp != None:
#             data = np.array(sample[:])
#             y=2
#             data=np.append(data, y, axis=None)
#             writer.writerow(data)
# f.close()








###########################LIGHT ON DATA ####################################
###############################################################################
import time
from pylsl import StreamInlet, resolve_stream
import csv
from PIL import Image
import numpy as np
import webbrowser



streams = resolve_stream('type', 'EEG') 
inlet = StreamInlet(streams[0])
f = open('C:/EEG_DATA_COLLECTION/1_EEG_DATA_COLLECTION-LIGHT/Volunteer_7/lon5.csv', 'w')   # SOLIH
writer = csv.writer(f)
img1 = "C:/EEG_DATA_COLLECTION/1_EEG_DATA_COLLECTION-LIGHT/as.gif"
img2 = "C:/EEG_DATA_COLLECTION/1_EEG_DATA_COLLECTION-LIGHT/lox.gif"

data=[]
for i in range(5):
    webbrowser.open(img1)
    timeout = 6
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        sample, timestamp = inlet.pull_sample()
        if timestamp != None:
            data = np.array(sample[:])
            y=1
            data=np.append(data, y, axis=None)
            writer.writerow(data)
    webbrowser.open(img2)
    timeout = 6
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        sample, timestamp = inlet.pull_sample()
        if timestamp != None:
            data = np.array(sample[:])
            y=0
            data=np.append(data, y, axis=None)
            writer.writerow(data)
f.close()

#############################LIGHT OFF DATA ####################################
###############################################################################

import time
from pylsl import StreamInlet, resolve_stream
import csv
from PIL import Image
import numpy as np
import webbrowser

streams = resolve_stream('type', 'EEG') 
inlet = StreamInlet(streams[0])
f = open('C:/EEG_DATA_COLLECTION/1_EEG_DATA_COLLECTION-LIGHT/Volunteer_7/lof5.csv', 'w')   # SOLIH
writer = csv.writer(f)
img2 = "C:\\EEG_DATA_COLLECTION\\1_EEG_DATA_COLLECTION-LIGHT\\lox.gif"
img3 = "C:\\EEG_DATA_COLLECTION\\1_EEG_DATA_COLLECTION-LIGHT\\untar.gif"



data=[]
for i in range(5):
    webbrowser.open(img3)
    timeout = 6
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        sample, timestamp = inlet.pull_sample()
        if timestamp != None:
            data = np.array(sample[:])
            y=2
            data=np.append(data, y, axis=None)
            writer.writerow(data)
    webbrowser.open(img2)
    timeout = 6
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        sample, timestamp = inlet.pull_sample()
        if timestamp != None:
            data = np.array(sample[:])
            y=0
            data=np.append(data, y, axis=None)
            writer.writerow(data)
f.close() 







