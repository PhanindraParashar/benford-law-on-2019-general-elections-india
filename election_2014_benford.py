import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_excel('List of Successful Candidates.xlsx',skiprows=1)

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

Leading_Margin = []
for i in df['MARGIN']:
    Leading_Margin.append(leading_digit(i))


df['Leading Digits'] = Leading_Margin
total = df['Leading Digits'].value_counts().sum()


exp_dict = Make_dict(Digits,Expected)
c_dict = digit_counts()

def Create_DataFrame_Histogram():
    Adf = []
    Pdf = []
    for i in Digits:
        Adf.append(c_dict.get(i))
        Pdf.append(exp_dict.get(i))
    
    Df = pd.DataFrame()
    Df['Digits'] = Digits
    Df.set_index('Digits')
    Df['Actual'] = Adf
    Df['Expected'] = Pdf
    
    DF = Df.set_index('Digits')
    DF.plot.bar()

Create_DataFrame_Histogram()
