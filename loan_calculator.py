#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 21:22:31 2018

@author: zhuyue
"""

# HouseLoanCalculator/Unit: Ten Thousand

import numpy as np

Loan_year = 30

Price_house = 278   

Price_agency = 1.3

Price_DownPayment = 200

Area = 94

Rate_NotOnyOne = 1/100

Rate_loan =  4.9/100

Price_totally = Price_house * (1 + Rate_NotOnyOne) + Price_agency

# Monthoy loan calculation 

loan_monthly = (Price_totally - Price_DownPayment) * Rate_loan / 12

base_monthly = (Price_totally - Price_DownPayment) / Loan_year / 12

pay_monthly = loan_monthly + base_monthly

print('Total price is',Price_totally)
print('Monthly, you pay for',pay_monthly)