from pyPPG import PPG, Fiducials, Biomarkers
from pyPPG.datahandling import load_data, plot_fiducials, save_data
import pyPPG.preproc as PP
import pyPPG.fiducials as FP
import pyPPG.biomarkers as BM
import pyPPG.ppg_sqi as SQI
import numpy as np
import sys
import json
import pandas as pd
from matplotlib import pyplot as plt

wavelengths = ["660nm","730nm","850nm","940nm"]
for i in range(58):
    id = str(i + 1)
    for wavelength in wavelengths:
        data_path = wavelength + "_waveforms/content/" + wavelength + "/_/" + id + ".csv" # the path of the file containing the PPG signal to be analysed
        start_sig = 0 # the first sample of the signal to be analysed
        end_sig = -1 # the last sample of the signal to be analysed (here a value of '-1' indicates the last sample)
        savingfolder = wavelength + "_features/" + id 
        savingformat = 'csv'
        
        # Load the raw PPG signal
        signal = load_data(data_path=data_path, start_sig=start_sig, end_sig=end_sig, use_tk=False, fs=200)
        
        signal.filtering = True # whether or not to filter the PPG signal
        signal.fL=0.5000001 # Lower cutoff frequency (Hz)
        signal.fH=12 # Upper cutoff frequency (Hz)
        signal.order=4 # Filter order
        signal.sm_wins={'ppg':50,'vpg':10,'apg':10,'jpg':10} # smoothing windows in millisecond for the PPG, PPG', PPG", and PPG'"

        prep = PP.Preprocess(fL=signal.fL, fH=signal.fH, order=signal.order, sm_wins=signal.sm_wins)
        signal.ppg, signal.vpg, signal.apg, signal.jpg = prep.get_signals(s=signal)
        
        # Initialise the correction for fiducial points
        corr_on = ['on', 'dn', 'dp', 'v', 'w', 'f']
        correction=pd.DataFrame()
        correction.loc[0, corr_on] = True
        signal.correction=correction

        # Create a PPG class
        s = PPG(signal)
        
        fpex = FP.FpCollection(s=s)
        
        fiducials = fpex.get_fiducials(s=s)
        # here the starting sample is added so that the results are relative to the start of the original signal (rather than the start of the analysed segment)
        print("Fiducial points:\n",fiducials + s.start_sig) 
        
        # Create a fiducials class
        fp = Fiducials(fp=fiducials)
        
        # Get PPG SQI
        ppgSQI = round(np.mean(SQI.get_ppgSQI(ppg=s.ppg, fs=s.fs, annotation=fp.sp)) * 100, 2)
        print('Mean PPG SQI: ', ppgSQI, '%')
        
        # Init the biomarkers package
        bmex = BM.BmCollection(s=s, fp=fp)

        # Extract biomarkers
        bm_defs, bm_vals, bm_stats = bmex.get_biomarkers()
        tmp_keys=bm_stats.keys()
        print('Statistics of the biomarkers:')
        for i in tmp_keys: print(i,'\n',bm_stats[i])

        # Create a biomarkers class
        bm = Biomarkers(bm_defs=bm_defs, bm_vals=bm_vals, bm_stats=bm_stats)
        fp_new = Fiducials(fp.get_fp() + s.start_sig) # here the starting sample is added so that the results are relative to the start of the original signal (rather than the start of the analysed segment)
        save_data(s=s, fp=fp_new, bm=bm, savingformat=savingformat, savingfolder=savingfolder)
        
        

print("Features Successfully Extracted...")