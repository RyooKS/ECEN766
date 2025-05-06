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

[1] Chaparro, C. M., \& Suchdev, P. S. (2019) {\it Anemia epidemiology, pathophysiology, and etiology in low- and middle-income countries.} The American Journal of Clinical Nutrition, 111(6), 1499S-1506S.

[2] Chen, Z., Qin, H., Ge, W., Li, S., \& Liang, Y. (2023) {\it Research on a Non-Invasive Hemoglobin Measurement System Based on Four-Wavelength Photoplethysmography.} Electronics, 12(6), 1346.

[3] Abuzairi, T., Vinia, E., Yudhistira, M. A., Rizkinia, M., \& Eriska, W. (2023) {\it A dataset of hemoglobin blood value and photoplethysmography signal for machine learning-based non-invasive hemoglobin measurement.} Data in Brief, 46, 108756. 

[4] Fine, J., Branan, K. L., Rodriguez, A. J., Boonya-ananta, T., Ajmal, Ramella-Roman, J. C., McShane, M. J., \& Coté, G. L. (2020) {\it Sources of inaccuracy in photoplethysmography for continuous cardiovascular monitoring.} Journal of Clinical Monitoring and Computing, 34(6), 1191-1205. 

[5] Billett, H. H. (1990). Hemoglobin and hematocrit. In Clinical methods: The history, physical, and laboratory examinations (3rd ed., pp. 1200–1205). Butterworths.

[6] Chen Y, Zhong K, Zhu Y, Sun Q. Two-stage hemoglobin prediction based on prior causality. Front Public Health. 2022 Nov 30;10:1079389. doi: 10.3389/fpubh.2022.1079389. PMID: 36530714; PMCID: PMC9748421.

[7] Virtanen, P., Gommers, R., Oliphant, T. E., Haberland, M., Reddy, T., Cournapeau, D., ... SciPy 1.0 Contributors. (2020). SciPy 1.0: Fundamental algorithms for scientific computing in Python. Nature Methods, 17(3), 261–272. https://doi.org/10.1038/s41592-019-0686-2

[8] Goda, M. A., Charlton, P. H., \& Behar, J. A. (2023). pyPPG: A Python toolbox for comprehensive photoplethysmography signal analysis. Physiological Measurement. https://doi.org/10.1088/1361-6579/ad33a2

[9] Liu, L., Wang, Z., Zhang, X., Zhuang, Y., \& Liang, Y. (2023). A novel model for noninvasive haemoglobin detection based on visibility network and clustering network for multi-wavelength PPG signals. Algorithms, 18(2), 75. https://doi.org/10.3390/a18020075

[10] Huang, G., Liu, Z., van der Maaten, L., \& Weinberger, K. Q. (2016) {\it Densely Connected Convolutional Networks.} arXiv preprint 

[11] Ige, A. O., \& Sibiya, M. (2024) {\it State-of-the-Art in 1D Convolutional Neural Networks: A Survey.} IEEE Access, 12, 144082-144105. 

[12] Taşdelen, A., \& Sen, B. (2021) {\it A hybrid CNN-LSTM model for pre-miRNA classification.} Scientific Reports, 11, 14125. 

[13] Winny, A., \& Jurmo, N. (2024, July 8). The problem with pulse oximeters: A long history of racial bias. Johns Hopkins Bloomberg School of Public Health. https://publichealth.jhu.edu/2024/pulse-oximeters-racial-bias
bias


  
