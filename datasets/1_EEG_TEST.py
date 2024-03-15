import tensorflow as tf
from glob import glob
import numpy as np
import pandas as pd
import mne

n_channels = 14
sampling_freq = 128
n_fft = 128

def convertmat2mne(data):
    ch_names =['AF3', 'F7', 'F3', 'FC5', 'T7', 'P7', 'O1', 'O2', 'P8', 'T8', 'FC6', 'F4', 'F8', 'AF4'] 
    ch_types = ['eeg']*14
    info = mne.create_info(ch_names, ch_types=ch_types, sfreq=sampling_freq)
    info.set_montage('standard_1020')
    data = mne.io.RawArray(np.transpose(data), info)
    data.set_eeg_reference()
    data.filter(l_freq= 1, h_freq=49)
    epochs=mne.make_fixed_length_epochs(data, duration=6,overlap=5, preload=True)
    return epochs

# LON = glob('C:/Users/tengis/Desktop/BLON14D.csv')
# LOF = glob('C:/Users/tengis/Desktop/BLOF14D.csv')
# LOX = glob('C:/Users/tengis/Desktop//BLOX14D.csv')

# data_on=[]
# for lon in LON:
#     data = pd.read_csv(lon)
#     data = np.array(data)
#     data = data[:, 3:17]
#     data_on.append(data)
#     lon_mne = convertmat2mne(data)
    
    
# data_of=[]
# for lof in LOF:
#     data = pd.read_csv(lof)
#     data = np.array(data)
#     data = data[:, 3:17]
#     data_of.append(data)
#     lof_mne = convertmat2mne(data)
    
# data_ox=[]
# for lox in LOX:
#     data = pd.read_csv(lox)
#     data = np.array(data)
#     data = data[:, 3:17]
#     data_ox.append(data)
#     lox_mne = convertmat2mne(data)
    
    
all_files_path = glob('C:/EEG_DATA_COLLECTION/1_EEG_DATA_COLLECTION-LIGHT/Volunteer_7/*.csv')
LON = [i for i in all_files_path if 'lon' in i.split('\\')[1]]
LOF = [i for i in all_files_path if 'lof' in i.split('\\')[1]]
LOX = [i for i in all_files_path if 'lox' in i.split('\\')[1]]

data_on=[]
data_of=[]
data_ox=[]

for lon in LON:
    data = pd.read_csv(lon)
    data = np.array(data)
    for i in range(0,len(data)):
        x = data[i,19]
        if x == 1:
            data_on.append(data[i, 3:17])
        else:
            data_ox.append(data[i,3:17])
 
for lof in LOF:
    data = pd.read_csv(lof)
    data = np.array(data)
    for i in range(0,len(data)):
        x = data[i,19]
        if x == 2:
            data_of.append(data[i, 3:17])
        else:
            data_ox.append(data[i, 3:17])

for lox in LOX:
    data = pd.read_csv(lox)
    data = np.array(data)
    for i in range(0,len(data)):
        x = data[i,19]
        if x == 0:
            data_ox.append(data[i, 3:17])
        else:
            data_ox.append(data[i, 3:17])
            

lon_data =[]
lon_mne=[]
lon_mne = convertmat2mne(data_on)                       
lon_data = lon_mne.get_data()

lof_data=[]
lof_mne=[]
lof_mne = convertmat2mne(data_of)                     
lof_data = lof_mne.get_data() 

lox_data=[]
lox_mne=[]
lox_mne = convertmat2mne(data_ox)                        
lox_data = lox_mne.get_data()

from mne.time_frequency import tfr_morlet
freqs = list(range(2, 48))

wlon_target = []  
for i in range(lon_mne.get_data().shape[0]):
    lon_trial = lon_mne[i]  
    wlon_trial = tfr_morlet(lon_trial, freqs, 3, return_itc=False)
    wlon_target.append(wlon_trial.data)
lon_subject = np.array(wlon_target)

wlof_target = []  
for i in range(lof_mne.get_data().shape[0]):
    lof_trial = lof_mne[i]  
    wlof_trial = tfr_morlet(lof_trial, freqs, 3, return_itc=False)
    wlof_target.append(wlof_trial.data)
lof_subject = np.array(wlof_target)

wlox_target = []  
for i in range(lox_mne.get_data().shape[0]):
    lox_trial = lox_mne[i]  
    wlox_trial = tfr_morlet(lox_trial, freqs, 3, return_itc=False)
    wlox_target.append(wlox_trial.data)
lox_subject = np.array(wlox_target)

len(lon_data),len(lof_data)
lon_subject=np.array_split(lon_subject, 10)
lof_subject=np.array_split(lof_subject, 10)
lox_subject=np.array_split(lox_subject, 10)

len(lon_subject),len(lof_subject)
lof_epochs_labels = [len(i)*[0] for i in lof_subject]
lon_epochs_labels = [len(i)*[1] for i in lon_subject]
lox_epochs_labels = [len(i)*[2] for i in lox_subject]

data_list = lon_subject+lof_subject +lox_subject
label_list = lon_epochs_labels + lof_epochs_labels + lox_epochs_labels
groups_list = [[i]*len(j) for i,j in enumerate(data_list)]

epochs_array =  np.vstack(data_list)
epochs_labels = np.hstack(label_list)
group_array = np.hstack(groups_list)

from sklearn.preprocessing import OneHotEncoder
input_values = np.array(epochs_labels)
onehot_encoder = OneHotEncoder(categories='auto')
onehot_values = onehot_encoder.fit_transform(input_values.reshape(-1, 1))
epochs_labels=onehot_values.toarray()

from sklearn.model_selection import GroupKFold
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
gkf = GroupKFold()
 
def cnnmodel():
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(14, 46, 768)))    
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dense(3, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model
model = cnnmodel()
model.summary()

epochs_array = np.reshape(epochs_array, (538,14,46,768))
accuracy=[]
true_labels = []
predicted_labels = []
for train_index, val_index in gkf.split(epochs_array, epochs_labels, groups=group_array):
    train_features, train_labels = epochs_array[train_index], epochs_labels[train_index]
    val_features, val_labels = epochs_array[val_index], epochs_labels[val_index]
    scaler=StandardScaler()
    #break
    train_features=scaler.fit_transform(train_features.reshape(-1, train_features.shape[-1])).reshape(train_features.shape)
    val_features=scaler.transform(val_features.reshape(-1, val_features.shape[-1])).reshape(val_features.shape)
    model=cnnmodel()
    history=model.fit(train_features, train_labels, epochs=80, batch_size=5, validation_data=(val_features, val_labels))
    accuracy.append(model.evaluate(val_features, val_labels)[1])

####################Confusion Matrix###############################
labels = np.argmax(val_labels, axis=1)
true_labels = labels.reshape(-1, 1)
predicted_labels = model.predict(val_features)
predicted_labels = np.argmax(predicted_labels, axis=1)
predicted_labels = predicted_labels.reshape(-1, 1)
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
confusion_mat = confusion_matrix(true_labels, predicted_labels)
#class_names = ['Class 1', 'Class 2', 'Class 3']  # Replace with your actual class names
class_names = ['Light on', 'Light off', 'Normal']
sns.heatmap(confusion_mat, annot=True, cmap='Blues', xticklabels=class_names, yticklabels=class_names)
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('Confusion Matrix')
plt.show()

####################### Accuracy ###############################
train_accuracy = history.history['accuracy']
val_accuracy = history.history['val_accuracy']
import matplotlib.pyplot as plt
# Plot the accuracy
epochs = range(1, len(train_accuracy) + 1)
plt.plot(epochs, train_accuracy, 'bo', label='Training Accuracy')
plt.plot(epochs, val_accuracy, 'b', label='Validation Accuracy')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()


np.mean(accuracy)
yp = model.predict(val_features)
