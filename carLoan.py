import streamlit as st 
import numpy as np 
import pandas as pd

#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import classification_report

st.title("Welcome to the RBA Car Loan Calculator")

while True:

    totalAmount = st.write("Please enter the total amount")
    try:
        totalAmount = int(totalAmount)
        break

    except ValueError:
        st.write("Please enter a number")

# Part2 : Store the downPayment

while True:

    downPayment = st.write("Please enter the down payment")
    try:
        downPayment = int(downPayment)
        break
    
    except ValueError:
        st.write("Please enter a number")
    


# Part3 : Store the interestRate
# guna float sbb ada decimal point

while True:

    interestRate = st.write("Please enter the interest rate")
    try:
        interestRate = float(interestRate)
        break
    
    except ValueError:
        st.write("Please enter a number")
      
    
# Part4 : Store the loanPeriod

while True:

    loanPeriod = st.write("Please enter the loan period")
    try:
        loanPeriod = float(loanPeriod)
        break
    
    except ValueError:
        st.write("Please enter a number")
