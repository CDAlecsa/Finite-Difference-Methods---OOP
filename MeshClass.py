#%%%%
'''
                                A basic mesh class for Finite Difference Methods (it is based upon the Vector class) 
'''

from VectorClass import Vector

class Mesh() :
    
    def __init__(self,a = 0,b = 1, h = 10**(-1), x0 = 0) :
        self.InitialValue = x0
        self.StepSize = h 
        self.InitialTime = a
        self.FinalTime = b
        self.Length = 1 + round(( self.FinalTime - self.InitialTime ) / self.StepSize)
        timeList = [self.StepSize * i for i in range(self.Length)]        
        self.Grid = Vector._CreateVectorWithValues(self.Length,timeList)
        
        
    def __getitem__(self, IndexVector) :
        return self.Grid.__getitem__(IndexVector) 


    def __setitem__(self, IndexVector, itemVector) :
        self.Grid.__setitem__(IndexVector, itemVector)
        

    def SaveMesh(self,strNameFile,optionFile) :
         self.Grid.SaveVector(strNameFile,optionFile)
         

    def printMesh(self) :
        print('Mesh List ... ',self.Grid.printVector(),'\n')
        print('Mesh Length ... ',self.Grid.printLengthVector(),'\n')
        print('Interval : [ ',self.InitialTime,', ',self.FinalTime,'] \n')
        print('Step-size : h = ',self.StepSize,'\n')
        print('Initial Value : x0 = ',self.InitialValue,'\n')
    

    def InsertElementsMesh(self,ListElements) :
        self.Grid.ElementsVector(ListElements)

    
    def returnInitialValue(self) :
        return self.InitialValue
    
    
    def returnTimeMesh(self) :
        return self.Grid.ReturnElementsVector()

    
    def returnTimeLength(self) :
        return self.Length
    
    
    def returnTimeStepSize(self) :
        return self.StepSize

    
    @classmethod
    def _CreateMeshWithValues(cls, a, b, h) :
        newMesh = Mesh(a, b, h)
        return newMesh

    
    
    @classmethod
    def _returnLengthMesh(cls, a, b, h) :
        newMesh = Mesh(a, b, h)
        return newMesh.Length
    

    @classmethod
    def _CreateMeshInput(cls) :
        newStepSize = input('StepSize Value : ')
        newStepSize = float(newStepSize)
        
        newInitialTime = input('Initial Time : ')
        newInitialTime = float(newInitialTime)
        
        newFinalTime = input('Final Time : ')
        newFinalTime = float(newFinalTime)
        
        newInitialValue = input('Initial Value : ')
        newInitialValue = float(newInitialValue)
        
        newMesh = Mesh(newInitialTime, newFinalTime, newStepSize, newInitialValue)
        return newMesh

