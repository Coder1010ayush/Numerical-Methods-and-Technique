"""
    this class will handle all the kind of error related to
        -- data types
        -- value error
        -- shape error
"""

class ShapeError(Exception):
    pass

class ErrorHandler(Exception):

    def __init__(self):
        super().__init__(self)

    def check_data_types(self,*args):
        for var in args:
            if type(var) != int and type(var) != float:
                raise TypeError(f"value must be either interger or floating point values {type(var)}")

        return True

    def same_shape(self,mat1,mat2):
        if len(mat1) !=len(mat2):
            raise ShapeError(f'shape of both matrix is not same.')
        elif len(mat2) == len(mat1):
            for i in range(0,len(mat1)):
                if len(mat1[i]) != len(mat2) :
                    raise ShapeError(f"shape is not consistant.")
            return True
        return True

    def check_square_matrix(self,mat):
        if len(mat) != len(mat[0]):
            raise ShapeError("matrix must be square matrix.")
        return True



if __name__ == '__main__':
    print("let us start")