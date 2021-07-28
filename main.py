import sys
import numpy as np

if __name__ == '__main__':
    # print(sys.version)

    np.set_printoptions(suppress=True)

    deci_value = np.array([[1.0151, -3.1124], [-0.0215, 12.235], [-1.1412, 42.133]])
    rounded_value = np.round(deci_value, 2)

    print("Array Size {} \nArray Shape {} \nAfter Round Off {} \nBefore Round Off {}\n"
          .format(deci_value.size, deci_value.shape, rounded_value, deci_value))
