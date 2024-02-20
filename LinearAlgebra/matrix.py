"""
    this class will handle all kind of
    matrix related operation
    such as -- addition , subtraction,multiplication,inverse , minor,orthogonality,orthonormality,adjoint,mod,
    flatten and norm etc.

"""
import cmath
import os
import sys
sys.path.insert(0, '/home/endless/Documents/Mathematics/venv/script/error')
from error_handling import ErrorHandler

class Matrix(ErrorHandler):

    def __init__(self):
        super().__init__()
        print("in class Matrix")

    def pretty_print(self,mat,label=None):
        if label != None:
            print(label , end='')
        print("[ ")
        for item in mat: 
            print('\t',end='')
            print(item,',')
        print("]")


    """
        this method returns addition of two matrix
    """
    def sum(self,mat1,mat2):
        if super().same_shape(mat1, mat2):
            mat3 = [[] for i in range(len(mat1))]
            for i in range(0,len(mat1)):
                for j in range(0,len(mat1)):
                    mat3[i].append(0)
            for i in range(0,len(mat1)):
                for j in range(0,len(mat1)): 
                    mat3[i][j] = mat1[i][j] + mat2[i][j]
            return mat3
    """
        this method returns subtraction of two matrix
    """

    def sub(self,mat1,mat2):
        if super().same_shape(mat1, mat2):
            mat3 = [[] for i in range(len(mat1))]
            for i in range(0,len(mat1)):
                for j in range(0,len(mat1)):
                    mat3[i].append(0)
            for i in range(0,len(mat1)): 
                for j in range(0,len(mat1)): 
                    mat3[i][j] = mat1[i][j] - mat2[i][j]
            return mat3

    def prod(self,mat1,mat2):
        mat3 = [[] for i in range(len(mat1))]
        for it in range(0,len(mat3)):
            for j in range(0,len(mat2[0])):
                mat3[it].append(0)
        for i in range(0,len(mat1)):
            for j in range(0,len(mat2[0])):
                for k in range(0,len(mat1[0])):
                    mat3[i][j] += mat1[i][k] * mat2[k][j]
        return mat3
    """
        this method returns multiplication of two matrix
    """

    def mul(self,mat1,mat2):

        if super().same_shape(mat1, mat2):
            mat3 = self.prod(mat1,mat2)
            return mat3

        elif len(mat1[0]) == len(mat2) :  
            mat3 = self.prod(mat1, mat2)
            return mat3
    """
        this function returns the maximum element present in a specific column
    """

    def maxIncolumn(self,mat1,col):

        maxi = 0
        for i in range(0,len(mat1)):
            for j in range(0,len(mat1[0])):
                if j==col:
                    maxi = max(mat1[i][j], maxi)
        return maxi

    """
        this function will returns the maximum element present in a specific row
    """
    def maxInRow(self,mat1,row):

        maxi = 0
        for i in range(0,len(mat1)):
            for j in range(0,len(mat1[0])):
                if i==row:
                    maxi = max(maxi, mat1[i][j])
        return maxi

    def determinanthelper(self,mat) :

        if len(mat)==1:
            return mat[0][0]

        determinant = 0
        sign = 1
        row = len(mat)
        for i in range(0,row):

            submatrix = list()
            for actual in range(0,row-1):
                local = list()
                for p in range(0,row-1):
                    local.append(0)
                submatrix.append(local)

            for j in range(1,row):

                for k in range(0,row):
                    if k<i:
                        submatrix[j-1][k] = mat[j][k]
                    elif (k>i):
                        submatrix[j-1][k-1] = mat[j][k]

            determinant += sign * mat[0][i] * self.determinanthelper(submatrix)
            sign = -sign
        return determinant

    """
        this function returns the determinant of a given matrix
    """

    def determinant(self,mat):
        if super().check_square_matrix(mat):
            det = self.determinanthelper(mat)
            return det

    """
        this function returns the trace of a square matrix
    """

    def trace(self,mat):
        if super().check_square_matrix(mat):
            trac = 0
            for i in range(0,len(mat)):
                for j in range(0,len(mat[0])):
                    if i==j:
                        trac = trac + mat[i][j]
            return trac
    """
        this function returs the dot product of two given matrix
    """

    def dot(self,mat1,mat2): 
        if super().same_shape(mat1, mat2): 
            res = 0
            for i in range(0,len(mat1)):
                for j in range(0,len(mat1[0])):
                    res = res + (mat1[i][j] * mat2[i][j])
            return res
    """
        this function return the transpose of a matrix
    """
    def transpose(self,mat):
        res = [[] for i in range(len(mat[0]))  ]
        for i in range(0,len(res)):
            for j in range(0,len(mat)):
                res[i].append(0)
        for i in range(len(res)):
            for j in range(0,len(res[0])):
                res[i][j] = mat[j][i]
        return res

    """
        this function finds minor about a given row and column
    """
    def minor(self,mat,rowToIgnore,colToIgnore):
        if super().check_square_matrix(mat):
            if rowToIgnore<len(mat) and colToIgnore < len(mat):
                minor_ = [[] for i in range(len(mat)-1)]
                for i in range(0,len(minor_)):
                    for j in range(0,len(minor_)):
                        minor_[i].append(0)

                row = 0
                col = 0
                for i in range(0,len(mat)):
                    if i==rowToIgnore:
                        continue
                    col = 0
                    for j in range(0,len(mat)):
                        if j == colToIgnore:
                            continue
                        minor_[row][col] = mat[i][j]
                        col = col+1
                    row = row+1
                return minor_
            else: 
                raise Exception("row or col must not exceed the length of matrix")
    """
        this method returns the adjoint of a metrix
    """

    def adjoint (self,mat): 
        if super().check_square_matrix(mat):
            row = len(mat)
            col = len(mat)
            adj = [[] for i in range(len(mat))]
            for i in range(row):
                for j in range(col):
                    adj[i].append(0)

            for i in range(row):
                for j in range(col):
                    x = (i+j) %2
                    sign = 1
                    if x ==1:
                        sign = 1
                    else : 
                        sign = -1

                    minor = self.minor(mat, i, j)
                    det = self.determinant(minor)
                    adj[i][j] = sign*det
            adj = self.transpose(adj)
            return adj
    """
        this methid performs scalar multiplication over a matrix
    """
    def scalar_mul(self,mat,scal):
        res = [[] for i in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                res[i].append(0)
        for i in range(len(res)):
            for j in range(len(mat[0])):
                res[i][j] = scal*mat[i][j]
        return res

    """
        this function returns the inverse of a matrix
    """
    def inverse(self,mat):
        if super().check_square_matrix(mat):
            det = self.determinant(mat)
            if det == 0.0:
                print("non invertible matrix")
                return
            else: 
                adj = self.adjoint(mat)
                inv = self.scalar_mul(mat, det)
                return inv

    """
        this function convert matrix into one dimension vector
    """

    def flatten(self,mat):
        sparse = [1 for i in range(len(mat)*len(mat[0]))]
        cnt = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                sparse[cnt] = mat[i][j]
                cnt += 1
        return sparse
    """
        this function returns n*n size of identity metrix
    """
    def identity(self,n):
        iden = [[] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i==j:
                    iden[i].append(1)
                else: 
                    iden[i].append(0)
        return iden

    """
        this function checks whether a matrix is symmetric or not
    """
    def isIdentity(self,mat):
        if super().check_square_matrix(mat):
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    if i==j: 
                        if mat[i][j] != 1:
                            return False
                    else: 
                        if mat[i][j] != 0: 
                            return False
            return True

    """
        this function checks whether a matrix is symmetric or not
    """
    def isSymmetric(self,mat):
        if super().check_square_matrix(mat):
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    if i==j: 
                        continue
                    else:
                        if mat[i][j] != mat[j][i] :
                            return False
            return True

    """
        this function checks whether a matrix is skrew symmetric or not
    """
    def isSkrewSymmetric(self,mat):
        if super().check_square_matrix(mat):
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    if i==j: 
                        if mat[i][j] != 0:
                            return False
                    else:  
                        if mat[i][j] != -mat[j][i]:
                            return False
            return True


    """
        this function return magnitude of a vector
    """
    def mod(self,mat):
        res = 0
        for i in range(len(mat)):
            res = res + mat[i]*mat[i]
        res = cmath.sqrt(res)
        return res

    """
        this function checks orthogonality condition
    """
    def isOrthogonal(self,mat):
        if super().check_square_matrix(mat):
            tps = self.transpose(mat)
            det = self.determinant(mat)
            if self.isIdentity(self.mul(mat, tps)) and(det == -1 or det == 1):
                return True
            else:
                return False

    """
        this function checks ortho normality condition
    """

    def isOrthogonormal(self,mat):
        if super().check_square_matrix(mat):
            if self.isOrthogonal(mat):
                for i in mat: 
                    mode = self.mod(i)
                    if mode != 1.0:
                        return False
                return True

            else: 
                return False

    """
     * finding the norms of the matrix 
     *  01. Frobenius norm
     * 02. 1 - norm
     * 03. 2 - norm
     * 04. inf - norm
    """

    def Frobenius(self,mat):
        norm = 0;
        for i in range(0,len(mat)):
            for j in range(0,len(mat[0])):
                norm += mat[i][j] * mat[i][j]
    
        norm = cmath.sqrt(norm);
        return norm

    def infNorm(self,mat):
        inf = -sys.maxsize - 1
        for i in range(0,len(mat)):
            sum = 0
            for j in range(len(mat[0])):
                sum += mat[i][j]
            inf = max(inf, sum)
        return inf

    def l2Norm(self,mat):
        inf = -sys.maxsize - 1
        for i in range(0,len(mat)):
            sum = 0
            for j in range(len(mat[0])):
                sum += mat[j][i]
            inf = max(inf, sum)
        return inf



if __name__ == '__main__':
    
    print("let us start")
    mat1 = [
        [1,2,5],
        [6,9,12],
        [10,20,20]
    ]
    mat2 = [
        [0,2,5],
        [6,1,12],
        [8,4,12]
    ]
    obj = Matrix()
    obj.pretty_print(obj.identity(5),label='identity matrix is : ')
    obj.pretty_print(mat1,label='mat1 is ')

