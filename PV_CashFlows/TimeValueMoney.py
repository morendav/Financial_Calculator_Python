#######################################
# Discount a future cash flow back by periods
#
#
#######################################
###     CodeBlock: Modules & Init Variables
#######################################
import numpy as np
from argparse import ArgumentParser
import matplotlib.pyplot as plt



#######################################
###     Functions for PV Cashflows
#######################################

def discount_fc (periods, effective_rate, FV):
    # Present value is discounted by n periods
    PV = FV / (1+ effective_rate) ** periods
    return PV

def compound_fc (periods, effective_rate, PV):
    # Present value is discounted by n periods
    FV = PV * (1+ effective_rate) ** periods
    return FV
