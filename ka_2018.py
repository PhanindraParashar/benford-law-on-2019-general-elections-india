import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_excel('KA 2018 Detailed Resulsts.xlsx',skiprows=1)

def leading_digit(z):
    zs = str(z)
    return int(zs[0])

def Benford_digits():
    Expected = []
    Digits = []
    
    for i in range(9):
        d = i+1
        Digits.append(d)
        theory = int(total*np.log10(1 + (1/d)))
        Expected.append(theory)
    return Expected,Digits

def Make_dict(A,B):
    return dict(zip(A,B))

def digit_counts():
    cv = []
    ci = []
    for i in range(9):
        ci.append(df['Leading Digits'].value_counts().index[i])
        cv.append(df['Leading Digits'].value_counts().iloc[i])
    
    c_dict = dict(zip(ci,cv))
    return c_dict



Expected,Digits = Benford_digits()