import numpy as np

def exec_module():
    # Divide i-th column of matrix 'A' by the i-th element of array 'b'.
    print '\n\n***Question 2*** \n'
    A = np.arange(25).reshape(5, 5)
    b = np.array([1., 5, 10, 15, 20])
    c = A / b[:,None]
    print 'Matrix A:\n', A
    print 'Vector b:\n', b
    print 'Each column in A divided by b:\n', c
    
if __name__ == '__main__':
    exec_module()