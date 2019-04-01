#%%%%
'''
                                A basic vector class 
'''

class Vector() :
           
    def __init__(self,N) :
        self.VectorLength = N
        self.rows = [0 for x in range(N)]
        
        
    def __getitem__(self, IndexVector) :
        return self.rows[IndexVector]
        
    
    def __setitem__(self, IndexVector, itemVector) :
        self.rows[IndexVector] = itemVector
    
    
    def ElementsVector(self,ListElements) :
        self.rows = [ListElements[i] for i in range(self.VectorLength)]
    
    
    def ReturnElementsVector(self) :
        return self.rows
    
    
    def printLengthVector(self) :
        print(self.VectorLength,'\n')

   
    def printVector(self) :
        print(self.rows,'\n')

    
    def resetValuesVector(self) :
        self.rows = [0 for x in range(self.VectorLength)]

        
    def transposeVector(self) :
        self.rows = [self.rows[self.VectorLength - i - 1] for i in range(self.VectorLength)]

    
    def getTranposeVector(self) :
        transposeVector = Vector(self.VectorLength)
        transposeVector.rows = [self.rows[self.VectorLength - i - 1] for i in range(self.VectorLength)]
        return transposeVector

    
    def ModifyAddVectors(self,NewVect) :
        self.rows = [self.rows[i] + NewVect.rows[i] for i in range(min(self.VectorLength,NewVect.VectorLength))]


    def ModifyCopyVectors(self, NewVect) :
        self.rows = [NewVect.rows[i] for i in range(min(self.VectorLength,NewVect.VectorLength))]
    
    
    def ModifyConcatenateVectors(self,NewVect) :
        self.rows = self.rows + NewVect.rows

    
    def SaveVector(self,strNameFile,optionFile) :
        open(strNameFile, optionFile).write(str(self.rows))
        

    
    @classmethod
    def _CreateVectorWithValues(cls, lengthValue, rowsValues) :
        newVect = Vector(lengthValue)
        newVect.ElementsVector(rowsValues) 
        return newVect
    
        
    def ReplaceVector(self, newVect) :
        self.ModifyCopyVectors(Vector._CreateVectorWithValues(newVect.VectorLength,newVect.rows))
    

    @classmethod
    def _CreateVectorInput(cls) :
        newLength = input('Length Value : ')
        newLength = int(newLength)
        
        print('New List ... ')
        newElements = [int(i) for i in input().split()]
        
        newVect = Vector(newLength)
        newVect.ElementsVector(newElements) 
        return newVect










