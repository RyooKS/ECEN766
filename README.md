# ECEN766

Repository for final project for ECEN 766

  Anemia, or low hemoglobin concentration, is estimated to affect nearly a third of the world's population. While current methods of screening for anemia are invasive and slow, photoplethysmography (PPG), which is an optical technique that can monitor blood volume changes in the circulatory system, could provide a noninvasive, inexpensive method of anemia screening. Current research has focused on combining PPG with traditional machine-learning methodologies. While these studies have obtained successful results, they require time-consuming and complicated feature engineering. In this project, we seek to develop the first deep-learning models for hemoglobin concentration estimation from PPG. Our goal is to obtain similar levels of effectiveness with less hardware requirements and without feature engineering.

## Overview

### Processed_data 
- contains the orginal PPG values of "Research on a Non-Invasive Hemoglobin Measurement System Based on Four-Wavelength Photoplethysmography" in a csv format, as it was originally in a matlab format.     
    
### Procedded_2Wavelengths
- contain PPG data of 660nm and 940nm, the initial wavelengths we used to train the model. 

### Filtered Wavelengths 
- contain filtered PPG data, 

### Subject_info.csv 
- contatins the meta information of the subjects[age, gender, height, weight, Hemodlobin density]

### LSTM tests.ipynb
- Code for testing an LSTM model.

### ECEN_766_Hemoglobin_Data_Processing.ipynb
- Code for processing Data

## References

    Chen, Z.; Qin, H.; Ge, W.; Li, S.; Liang, Y. Research on a Non-Invasive Hemoglobin Measurement System Based on Four-Wavelength Photoplethysmography. Electronics 2023, 12, 1346. https://doi.org/10.3390/electronics12061346


  
