import numpy as np

def exec_module():
    # Different matrix slicing operations
    print '\n\n***Question 1*** \n'
    mat = np.arange(15).reshape((5,3))
    arr1 = mat[(1,3),]
    arr2 = mat[:,1]
    arr3 = mat[1:4,]
    arr4 = mat[(mat>3) & (mat<11)]
    print 'The original matrix:\n', mat
    print '2nd and 4th rows:\n', arr1
    print '2nd column:\n', arr2
    print 'Elements between coordinates [1,0] to [3,2]:\n', arr3
    print 'Elements between 3 and 11:\n', arr4
    
if __name__ == '__main__':
    exec_module()