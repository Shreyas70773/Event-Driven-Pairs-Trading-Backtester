# This is the entire content of mp_helpers.py

import statsmodels.tsa.stattools as ts

def run_coint_test(args):
    """
    Worker function for multiprocessing.
    Receives pre-aligned numpy arrays to minimize overhead.
    """
    # Unpack arguments
    series1_vals, series2_vals, ticker1, ticker2 = args
    
    # Run the Engle-Granger cointegration test
    # The [1] gets the p-value from the result tuple
    p_value = ts.coint(series1_vals, series2_vals)[1]
    
    # Return the pair if the p-value is below the threshold
    if p_value < 0.05:
        return (ticker1, ticker2, p_value)
    return None