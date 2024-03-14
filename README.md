# EEG-Datasets
STUDY ON PROCESSING BRAIN SIGNALS USING EEG SENSOR BY MACHINE LEARNING

Collecting brain signal data

The brain dataset was supported by the Foundation for Science and Technology of Mongolia and implemented and collected by colleagues from the Electronics Department of the School of Information and Communication Technology at the Mongolian University of Science and Technology.
This dataset consists of more than 3294 minutes of EEG recording files from 122 volunteers participating in 4 types of exercises as described below. Each participant performed 4 different tasks during EEG recording using a 14-channel EMOTIV EPOC X system. During the experiment, the data consisted of one- and two-minute recordings, which were manipulated to exclude both eyes-open and eyes-closed cases. Additionally, instructions on how to make measurements have been developed. These tasks include the following 4 types of exercises:

1.	Lights on, lights off and normal thoughts – EEG_DATA_COLLECTION-LIGHT
2.	Thinking about moving the box on the screen left, right, up, down or not moving at all -EEG_DATA_COLLECTION-BOX
3.	Thoughts of moving the left arm, right arm, left leg, right leg or not moving at all – EEG_DATA_COLLECTION-MI
4.	Display video - VIDEO– EEG_DATA_COLLECTION-VIDEO

Data during each of the above exercises were recorded by reading the EEG signals at 128 sampling steps per second in a 14-channel system. Each recording was saved as a *.CSV file using Emotiv software and Python libraries. According to the international 10-20 system shown in Figure 1 (AF3, F7, F3, FC5, T7, P7, O1, O2, P8, T8, FC6, F4, F8, AF4, and additional 2 CMS/DRL references at P3/P4 electrodes) for EEG recording from 16 electrodes, each participant was presented with the developed instructions, and their consent was obtained.

<`img width="117" alt="image" src="https://github.com/munkh0724/EEG-Datasets/assets/161277762/6bfbf48c-f47a-4e0d-b3f2-55188924cfb6">
Figure 1. Connection points of the brain

The numbers below each electrode name indicate the order in which they appear in the recording. The signals on the record are numbered from 1 to 14, and columns 4-17 of the resulting table when opening the *.CSV file contain the values of the electrodes, while column 20 contains the label values. The total uncompressed file size is 6.84 GB.
 
Measurement instructions

1.	Make the participant sit still
2.	Turn off the phone and keep electrical appliances away from the body
3.	Sterilize and moisten the electrodes and wear them properly
4.	Go to the EEG_DATA_COLLECTION-LIGHT folder and create a VOLUNTEER folder
	a.	LON- thoughts are taken 5 times. In this case, change the number of the Lonx.csv file
	b.	LOF- thoughts are taken 5 times. In this case, change the number of the Lofx.csv file
