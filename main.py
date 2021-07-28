import sys
from pprint import pprint

import numpy as np
import pandas as pd

if __name__ == '__main__':
    # print(sys.version)

    np.set_printoptions(suppress=True)

    # deci_value = np.array([[1.0151, -3.1124], [-5.1585, 12.235], [-1.1412, 42.133]])
    # rounded_value = np.round(deci_value, 2)
    # arounded_value = np.around(deci_value, 2)
    # print("Array Size {} \nArray Shape {} \nBefore Round Off:- \n{} \nAfter Round Off (Using round):- \n{} "
    #       "\nAfter Round Off (Using around):- \n{}"
    #       .format(deci_value.size, deci_value.shape, deci_value, rounded_value, arounded_value))

    df = pd.DataFrame(np.random.random([3, 3]), columns=["A", "B", "C"])
    print("DataFrame before Round-Off:- \n{} ".format(df))
    print("\nDataFrame after round-off:- \n{} ".format(df.round(2)))
    print("\nDataFrame after round-off on different decimal places:- \n{} ".format(df.round({'A':2, 'B':3, 'C':4})))