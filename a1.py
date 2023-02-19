class Spreadsheet:
    def __init__(self):
        '''
        Predefined member variables. 
        
        WARNING:DO NOT MODIFY THE FOLLOWING VARIABLES
        '''
        self.sheet = None   # 2D array of values
        self.rows = 0       
        self.cols = 0
        self.cursor=[0,0]   # cursor's current position
        self.selction = [None, None, None, None]
        
        #======================
        # Insert your Member
        #   variables here (if any):
        #----------------------
        
        
        #======================
        
#======================
    def CreateSheet(self, rows, cols):
        '''
        Creates a new 2 dimensional array assigned
          to the self.sheet member variable.
        Initialize the 2D array with 'None' type.
 
        Parameters:
            rows --> total number of rows in this spreadsheet
            cols --> total number of cols in this spreadsheet
        
        Return value:
            None
        '''
        self.rows = rows
        self.cols = cols
        self.sheet = [[" " for i in range(cols)] for j in range(rows)]
        
        
        #raise NotImplementedError
#======================
#======================
    def Goto(self, row, col):
        '''
        Moves the cursor to the location indicated by the 
          row and col parameters
 
        Parameters:
            row --> row number to move to
            col --> column number to move to
        
        Return value:
            None
        '''
        self.row = row
        self.col = col
        self.cursor = self.row, self.col
        
       
        #raise NotImplementedError
#======================

#======================        
    def Insert(self, val):
        '''
        Inserts value at the position indicated by the cursor.
 
        Parameters:
            val --> value to be inserted at the cursor location
        
        Return value:
            None
        '''
        self.val = val
       
        a = self.cursor[0]
        b = self.cursor[1]
      
        self.sheet[a][b] = self.val
        
        
        #raise NotImplementedError
#======================

#======================        
    def Delete(self):
        '''
        Deletes a value from the position indicated by the cursor.
 
        Parameters:
            None
        
        Return value:
            None
        '''
        x = self.cursor[0]
        y = self.cursor[1]
        self.sheet[x][y] = " "
        #raise NotImplementedError
#======================

#======================    
    def ReadVal(self):
        '''
        Prints the value from the position indicated by the cursor.
 
        Parameters:
            None
        
        Return value:
            value stored at the cursor location 

        '''
        x = self.cursor[0]
        y = self.cursor[1]
        self.value = self.sheet[x][y] 
        
        return self.value
        
        #raise NotImplementedError
#======================

#======================    
    def Select(self,row, col):   
        '''
        Selects values between the position indicated in arguments with row and col and the position indicated by the cursor
 
        Parameters:
            row --> Row number to be selected 
            col --> Column number to be selected
        
        Return value:
            None
        '''
        x = self.cursor[0]
        y = self.cursor[1]

        selected_row = row
        selected_col = col

        self.selction = (x,y,selected_row,selected_col)
        
        #raise NotImplementedError
#======================

#======================        
    def GetSelection(self):
        '''
        Returns a tuple with current selecion cooridnates
        Parameters:
            None
        
        Return value:
            Returns a tuple with row and column of the selection:
                position 1 of the tuple indicates the stating row of the selection
                position 2 of the tuple indicates the stating col of the selection
                position 3 of the tuple indicates the ending row of the selection
                position 4 of the tuple indicates the ending col of the selection
            
            Example: (1,1,3,4)
        '''
        getselected = (self.selction[0],self.selction[1],self.selction[2], self.selction[3])
        return getselected
        #raise NotImplementedError
#======================

#======================        
    def Sum(self,row,col):
        '''
        Stores the sum of the values in the current selection at the position indicated in arguments
        Parameters:
            row --> Row number to store the sum
            col --> Column number to store the sum
        
        Return value:
            None
        '''
        sum = 0
        for i in range (self.selction[0],self.selction[2]+1):
            for j in range(self.selction[0],self.selction[3]+1):
                if self.sheet[i][j] != " " :
                    sum = self.sheet[i][j]
        self.sheet[row][col] = sum
        return sum
       
        
        #raise NotImplementedError
#======================

#======================    
    def Mul(self,row,col):
        '''
        Stores the product of the values in the current selection at the position indicated in arguments
        Parameters:
            row --> Row number to store the product
            col --> Column number to store the product
        
        Return value:
            None
        '''
        multiply = 0
        for i in range (self.selction[0],self.selction[2]+1):
            for j in range(self.selction[0],self.selction[3]+1):
                if self.sheet[i][j] != " " :
                    multiply = self.sheet[i][j] * multiply
        self.sheet[row][col] = multiply
        return multiply
             
        #raise NotImplementedError
#======================

#======================        
    def Avg(self,row,col):
        '''
        Stores the average of the values in the current selection at the position indicated in arguments
        Parameters:
            row --> Row number to store the average
            col --> Column number to store the average
        
        Return value:
            None
        '''
 
        sum=0
        count = 0
        sum = 0
        for i in range (self.selction[0],self.selction[2]+1):
            for j in range(self.selction[0],self.selction[3]+1):
                if self.sheet[i][j] != " " :
                    sum = self.sheet[i][j]
        self.sheet[row][col] = sum
        
        average = sums/count 
        self.sheet[row][col] = average
        return avg
        #raise NotImplementedError
#======================

#======================
    def Max(self,row, col):
        '''
        Stores the maximum of the values in the current selection at the position indicated in arguments
        Parameters:
            row --> Row number to store the maximum
            col --> Column number to store the maximum
        
        Return value:
            None
        '''        
          
        n = 0
        for i in range(self.selction[0],self.selction[2]+1):    
            for j in range(self.selction[0],self.selction[3]+1):   
                if n == 0 :
                    maximun_no = self.sheet[i][j]
                    n = 1   
                if self.sheet[i][j] != " " :
                    if maximun_no<self.sheet[i][j]:
                        maximun_no = self.sheet[i][j]
        self.sheet[row][col] = maximun_no


        #raise NotImplementedError
#======================

#======================
    def PrintSheet(self):
        '''
        Prints the sheet in a human readable from
        Parameters:
            None
        Return value:
            None    

        Note: This is an example output your values will differ
        PrintSheet()
        row/col:    0   1   2   3   4
            0       
            1   
            2           10               
            3                   12
            4 
        '''
        row_cols = 0
        print("row/col:  ",end="")
        for i in range(self.cols):
            print('{0: <10}'.format(i),end="")
        print()
        for i in self.sheet:    
            print("\n\n",row_cols,end="        ")
            row_cols+=1
            for j in i:
                print('{0: <10}'.format(j),end="")
        print()        
       
       # raise NotImplementedError
#======================

            
#======================
#======================
#    BONUS
#======================
    def Undo(self):
        '''
        Undoes the previous action by user.
 
        Parameters:
            None
        
        Return value:
            None 

        '''
        
        raise NotImplementedError

#----------------------

    def Redo(self):
        '''
        Redoes the previous action undone by user.
 
        Parameters:
            None
        
        Return value:
            None 

        '''
        
        raise NotImplementedError

#----------------------

    def Save(self, fileName):
        '''
        Saves the spreadsheet to a file with name given as Parameter
 
        Parameters:
            fileName
        
        Return value:
            None 

        '''
        for data in self.sheet:
            return data
        with open(fileName, "w") as f:
            f.write(str(data))
        f.close()
                
        #raise NotImplementedError

#----------------------

    def Load(self, fileName):
        '''
        Loads the spreadsheet from a file with name given as Parameter
 
        Parameters:
            fileName
        
        Return value:
            None 

        '''
        ins = open( fileName, "r" )
        array = []
        for line in ins:
            line = line.rstrip('\n')
            array.append( line )
        ins.close()
        length = len(array)
        row_cols = 0
        print("row/col:  ",end="")
        for i in range(len(array)):
            print('{0: <10}'.format(i),end="")
        print()
        for i in array:    
            print("\n\n",row_cols,end="      ")
            row_cols+=1
            for j in i:
                print('{0: <10}'.format(j),end="")
        #raise NotImplementedError
                
#======================


#======================
#======================
#
#    DRIVER FUNCTION
#
#======================

def main():
    # -----------------------------
    # Implement your own logic here:
    # -----------------------------
    sheet = Spreadsheet()
    # sheet.CreateSheet(5,5)
    #
    # while True:
    #     sheet.Goto(2,2)
    #     sheet.insert(4)
    #     sheet.Print()
    print("Welcome to DS SpreadSheet Program")
    print("Enter commands at the prompt")
    print("Enter the command in the following pattern like: Goto 1 2")
    while True:
        user_input = input(">> ")
        if user_input == "Quit":
            break
        else:
            user_input = user_input.split()
            if user_input[0]== "CreateSheet":
                sheet.CreateSheet(int(user_input[1]),int(user_input[2]))
                print("Sheet is successfully created !")
            elif user_input[0] == "Goto":
                sheet.Goto(int(user_input[1]),int(user_input[2]))
            elif user_input[0]== "Insert":
                sheet.Insert(int(user_input[1]))
            elif user_input[0]== "Delete":
                sheet.Delete()
            elif user_input[0]=="ReadVal":
                print(sheet.ReadVal())
            elif user_input[0]== "Select":
                sheet.Select(int(user_input[1]),int(user_input[2]))
            elif user_input[0] == "GetSelection":
                print(sheet.GetSelection())
            elif user_input[0] == "Sum":
                sheet.Sum(int(user_input[1]),int(user_input[2]))
            elif user_input[0]== "Mul":
                sheet.Mul(int(user_input[1]),int(user_input[2]))
            elif user_input[0]== "Avg":
                sheet.Avg(int(user_input[1]),int(user_input[2]))
            elif user_input[0] == "Max":
                sheet.Max(int(user_input[1]),int(user_input[2]))
            elif user_input[0]== "PrintSheet":
                    sheet.PrintSheet()
            elif user_input[0]== "Save":
                    x =input("Enter the file name to store")
                    sheet.Save(x)
            elif user_input[0]== "Load":
                    x =input("Enter the file name to load")
                    sheet.Load(x)

if __name__ == '__main__':
    main()
    
#======================


