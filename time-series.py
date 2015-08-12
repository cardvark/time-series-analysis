import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

loanData = pd.read_csv('LoanStats3d.csv', header=1, low_memory=False)

loanData['issue_d_format'] = pd.to_datetime(loanData['issue_d'])

loanDataTs = loanData.set_index('issue_d_format')
print loanDataTs

year_month_summary = loanDataTs.groupby(lambda x: x.year * 100 + x.month).count()
print year_month_summary

loan_count_summary = year_month_summary['issue_d']