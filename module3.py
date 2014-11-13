import numpy as np

def exec_module():
    # Obtain closest elements to 0.5 in different rows of matrix A.
    print '\n\n***Question 3*** \n'
    A = np.random.random([10,3])
    D = abs(A - 0.5)
    arr1 = D.min(axis=1)
    print 'The original matrix:\n', A
    print 'Elements closest to 0.5 in each row:\n', arr1
    colInd = D.argsort(axis=1)[:,0]
    arr2 = D[range(len(D)),colInd]
    print 'Using argsort and fancy indexing:\n', arr2
    
if __name__ == '__main__':
    exec_module()