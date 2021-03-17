# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 03:13:44 2021

@author: TaeKen

Source: https://www.irs.gov/newsroom/irs-provides-tax-inflation-adjustments-for-tax-year-2021
"""
import numpy as np

def tax_bracket(inc, state=None):
    
    income = np.array(inc)
    
    deductable = 12550
    thresholds = [0,9950,40525,86375,164925,209425,523600,np.inf]
    rates = [0.10,0.12,0.22,0.24,0.32,0.35,0.37]
    steps = [8955,26906,35763,59698,30260,204213.75]
    
    
    taxable = income-deductable
    takehome = np.zeros(income.shape)
    
    for ii in range(income.size):
        for i in range(1,len(thresholds)):
    
            if taxable[ii] < thresholds[i]:
                takehome[ii] += (taxable[ii]-thresholds[i-1])*(1-rates[i-1])
                break
            else:
                takehome[ii] += steps[i-1]
        
        # if taxable>thresholds[-1]:
        #     takehome += (taxable-thresholds[-1])*(1-rates[-1])
    
    if income.size==1:
        return takehome[0]+deductable
    else:
        return takehome+deductable
 