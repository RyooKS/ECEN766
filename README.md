# ECEN766

# GANTT Chart for Project Schedule
![image](https://github.com/user-attachments/assets/2ceaee98-9c02-4a3e-8a7f-f93d6222c0e6)


Repository for final project for ECEN 766

  Anemia, or low hemoglobin concentration, is estimated to affect nearly a third of the world's population. While current methods of screening for anemia are invasive and slow, photoplethysmography (PPG), which is an optical technique that can monitor blood volume changes in the circulatory system, could provide a noninvasive, inexpensive method of anemia screening. Current research has focused on combining PPG with traditional machine-learning methodologies. While these studies have obtained successful results, they require time-consuming and complicated feature engineering. In this project, we seek to develop the first deep-learning models for hemoglobin concentration estimation from PPG. Our goal is to obtain similar levels of effectiveness with less hardware requirements and without feature engineering.

## Overview

### Processed_data 
- Contains the orginal PPG values of "Research on a Non-Invasive Hemoglobin Measurement System Based on Four-Wavelength Photoplethysmography" in a csv format, as it was originally in a matlab format.     
    
### Procedded_2Wavelengths
- Contain PPG data of 660nm and 940nm, the initial wavelengths we used to train the model. 

### Filtered Wavelengths 
- Contain filtered PPG data,

### split_down_processed_data
- Contains data that has been split at each individual pulse wave and down sampled to be the same length (100 samples)

### Subject_info.csv 
- Contains the meta information of the subjects[age, gender, height, weight, Hemodlobin density]

### LSTM tests.ipynb
- Code for testing an LSTM model.

### ECEN_766_Hemoglobin_Data_Processing.ipynb
- Code for processing Data

### ECEN_766_Hemoglobin_ML.ipynb
- Basic 2D CNN for testing the split and downsampled data

### XGBoost.ipynb
- Code for using XGBoost Average intensity

### ECEN766_Hemoglobin_LSTM.ipynb
- LSTM for testing the split and downsampled data





## References

[1] Alexander, J.A.\ \& Mozer, M.C.\ (1995) Template-based algorithms for
connectionist rule extraction. In G.\ Tesauro, D.S.\ Touretzky and T.K.\ Leen
(eds.), {\it Advances in Neural Information Processing Systems 7},
pp.\ 609--616. Cambridge, MA: MIT Press.

[2] Bower, J.M.\ \& Beeman, D.\ (1995) {\it The Book of GENESIS: Exploring
  Realistic Neural Models with the GEneral NEural SImulation System.}  New York:
TELOS/Springer--Verlag.

[3] Hasselmo, M.E., Schnell, E.\ \& Barkai, E.\ (1995) Dynamics of learning and
recall at excitatory recurrent synapses and cholinergic modulation in rat
hippocampal region CA3. {\it Journal of Neuroscience} {\bf 15}(7):5249-5262.

[4] Chaparro, C. M., \& Suchdev, P. S. (2019) {\it Anemia epidemiology, pathophysiology, and etiology in low- and middle-income countries.} The American Journal of Clinical Nutrition, 111(6), 1499S-1506S.

[5] Chen, Z., Qin, H., Ge, W., Li, S., \& Liang, Y. (2023) {\it Research on a Non-Invasive Hemoglobin Measurement System Based on Four-Wavelength Photoplethysmography.} Electronics, 12(6), 1346.

[6] Abuzairi, T., Vinia, E., Yudhistira, M. A., Rizkinia, M., \& Eriska, W. (2023) {\it A dataset of hemoglobin blood value and photoplethysmography signal for machine learning-based non-invasive hemoglobin measurement.} Data in Brief, 46, 108756. 

[7] He, K., Zhang, X., Ren, S., \& Sun, J. (2016) {\it Deep Residual Learning for Image Recognition.} 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), pp. 770-778. 

[8] Huang, G., Liu, Z., van der Maaten, L., \& Weinberger, K. Q. (2016) {\it Densely Connected Convolutional Networks.} arXiv preprint 

[9] Ige, A. O., \& Sibiya, M. (2024) {\it State-of-the-Art in 1D Convolutional Neural Networks: A Survey.} IEEE Access, 12, 144082-144105. 

[10] Taşdelen, A., \& Sen, B. (2021) {\it A hybrid CNN-LSTM model for pre-miRNA classification.} Scientific Reports, 11, 14125. 

[11] Shenfield, A., \& Howarth, M. (2020) {\it A Novel Deep Learning Model for the Detection and Identification of Rolling Element-Bearing Faults.} Sensors (Basel, Switzerland), 20. 

[12] Fine, J., Branan, K. L., Rodriguez, A. J., Boonya-ananta, T., Ajmal, Ramella-Roman, J. C., McShane, M. J., \& Coté, G. L. (2020) {\it Sources of inaccuracy in photoplethysmography for continuous cardiovascular monitoring.} Journal of Clinical Monitoring and Computing, 34(6), 1191-1205. 

[13] Billett, H. H. (1990). Hemoglobin and hematocrit. In Clinical methods: The history, physical, and laboratory examinations (3rd ed., pp. 1200–1205). Butterworths.

[14] Chen Y, Zhong K, Zhu Y, Sun Q. Two-stage hemoglobin prediction based on prior causality. Front Public Health. 2022 Nov 30;10:1079389. doi: 10.3389/fpubh.2022.1079389. PMID: 36530714; PMCID: PMC9748421.


  
