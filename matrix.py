import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I
    
def get_row(matrix, row): # in case we dont want transpose 
    return matrix[row]

def get_column(matrix, column_number): # in case we dont want transpose 
    column = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j== column_number:
                column.append(matrix[i][j])
                
    return column

def dot_product(vector_one, vector_two): # added to return dot product of two vectors
    vector_dot=0
    
    for i in range(len(vector_one)):
        vector_dot += vector_one[i]*vector_two[i]
#     print("Dot Prod=", vector_dot)
    return vector_dot

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        determinant = 0
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        elif self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        elif self.h == 1:
            determinant =self.g[0][0]
        elif self.h == 2:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            determinant = (a * d - b * c) 
        return determinant

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        trace1 = 0
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        elif self.h == 1:
            return self.g[0][0]
        elif self.h == self.w:
            for i in range(self.h):
                for j in range(self.w):
                    if i == j:
                        trace1 = trace1 + self.g[i][j]
        return trace1
    
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        inverse = zeroes(self.h,self.w)
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        elif self.h == 1:
            #inverse.append([1/self.g[0][0]])
            inverse[0][0] = 1/self.g[0][0]
            
        elif self.h == 2:
            # If the matrix is 2x2, check that the matrix is invertible
            if self.g[0][0] * self.g[1][1] == self.g[0][1] * self.g[1][0]:
                raise ValueError('The matrix is not invertible.')
            else:
                # Calculate the inverse of the square 1x1 or 2x2 matrix.
                a = self.g[0][0]
                b = self.g[0][1]
                c = self.g[1][0]
                d = self.g[1][1]
            
                factor = 1 / (a * d - b * c)
            
                #inverse[0][0] = [[d, -b],[-c, a]]
                inverse[0][0] = d
                inverse[0][1] = -b
                inverse[1][0] = -c 
                inverse[1][1] = a
            
                for i in range(self.h):
                    for j in range(self.w):
                        inverse[i][j] = factor * inverse[i][j]
        return inverse  

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix_transpose = zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                matrix_transpose[i][j]=self.g[j][i] 
#             row=[]
#             for i in range(self.h):
#                 row.append(self.g[i][j])
#             matrix_transpose.append(row)
            
        return matrix_transpose

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        new = zeroes(self.h,self.w)
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        for i in range(self.h):
            #row = []
            for j in range(self.w):
                new[i][j] = self.g[i][j]+other.g[i][j]
#                 row.append(self.g[i][j]+other.g[i][j])
#             new.append(row)
        return new

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        new = zeroes(self.h,self.w)
        for i in range(self.h):
#             row = []
            for j in range(self.w):
                new[i][j] = -1*self.g[i][j]
#                 row.append(-1*self.g[i][j])
#             new.append(row)
        return new

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        new = zeroes(self.h,self.w)
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        for i in range(self.h):
#             row = []
            for j in range(self.w):
                new[i][j] = self.g[i][j]-other.g[i][j]
#                 row.append(self.g[i][j]-other.g[i][j])
#             new.append(row)
        return new

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        transpose_list = []
        for j in range(other.w):                                 
            row=[]
            for i in range(other.h):
                row.append(other.g[i][j])
            transpose_list.append(row) 
            
        transpose_other = zeroes(other.w, other.h)
        for i in range(other.w):                                  
            for j in range(other.h):
                transpose_other[i][j] = transpose_list[i][j]  
                
        product_mat = []        
        for i in range(self.h):                                  
            row2= []
            for j in range(transpose_other.h):
                row2.append(dot_product(self.g[i], transpose_other[j]))
            product_mat.append(row2)
        
        product_list = zeroes(self.h, other.w)
        for i in range(self.h):
            for j in range(other.w):
                product_list[i][j] = product_mat[i][j]
        return product_list
        

    
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            grid = self
            for r in range(self.h):
                for c in range(self.w):
                    grid[r][c] *= other
            return grid        
            
            
            

            
