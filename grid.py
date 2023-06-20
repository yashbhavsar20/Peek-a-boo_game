import os
import random


global value
value=64
def random_select_twice(start, end):
    elements = list(range(start, end + 1))  # Create a list of elements in the range
    selected_elements = elements + elements  # Duplicate the elements in the list
    random.shuffle(selected_elements)  # Randomly shuffle the list
    return selected_elements

# Example usage: Randomly selecting each element from 1 to 10 twice
class shuffle_elements:
    def shufflelements(size):
        start_range = 1
        end_range =int((size*size)/2) 
        selected_elements1 = random_select_twice(start_range, end_range)
        return selected_elements1
   

class grid:
  revealed_count=0
  guessed_count=0
  proper_count=0

  global size
  global matrix
  global matrix1
  global check_matrix
  global list_elements
  uncover_elements=[]
  covered_elements=[]
  list_elements=[]
  matrix=[]
  matrix1=[]
  check_matrix=[]
  x=1
  def Initialize(self,size):
      self.matrix=[]
      self.matrix1=[]
      self.check_matrix=[]
      count=0
      self.size=int(size)
      self.proper_count=int(int(size*size)/2)
      self.list_elements=shuffle_elements.shufflelements(size=int(size))
      for _ in range(self.size+1):
            row = [0] * (self.size+1)
            self.matrix.append(row)
      for _ in range(self.size):
            row = [0] * (self.size)
            self.matrix1.append(row)
      for _ in range(self.size):
            row = [0] * (self.size)
            self.check_matrix.append(row)
      for i in range(self.size):
          for j in range(self.size):
              self.matrix1[i][j]=self.list_elements[count]
              count=count+1
              
            


  def make_grid(self,size):
   
    size=int(size)
    for i in range(size+1):
        for j in range(size+1):
            if(i==0 and j==0):
                self.matrix[i][j]=" "
                continue
            elif(i==0):
                self.matrix[i][j]="[%c]"%(chr(value+j))
            elif(j==0):
                self.matrix[i][j]="[%d]"%(i-1)
            else:
                 if(self.check_matrix[i-1][j-1]==0):
                    self.matrix[i][j]="x"
                 else:
                    self.matrix[i][j]=self.matrix1[i-1][j-1]
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.matrix]))
    all_elements_not_x = all(all(element != 'x' for element in row) for row in self.matrix)
    if(all_elements_not_x):
        self.predict_score()
    else:
        pass
  def values_grid(self,c1,c2,c3,c4):
      self.guessed_count=self.guessed_count+1
      if(self.matrix1[c2][c1-97]==self.matrix1[c4][c3-97]):
          self.check_matrix[c2][c1-97]=1
          self.check_matrix[c4][c3-97]=1
      for i in range(self.size+1):
        for j in range(self.size+1):
            if(i==0 and j==0):
                self.matrix[i][j]=" "
                continue
            elif(i==0):
                self.matrix[i][j]="[%c]"%(chr(value+j))
            elif(j==0):
                self.matrix[i][j]="[%d]"%(i-1)
            else:
                 if(self.check_matrix[i-1][j-1]==1):
                    self.matrix[i][j]=self.matrix1[i-1][j-1]
                 elif((i==c2+1 and j==c1-96) or (i==c4+1 and j==c3-96)):
                     self.matrix[i][j]=self.matrix1[i-1][j-1]   
                 else:
                    self.matrix[i][j]="x" 
      
             
      print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.matrix]))
  def give_up(self):
      for i in range(self.size+1):
        for j in range(self.size+1):
            if(i==0 and j==0):
                self.matrix[i][j]=" "
                continue
            elif(i==0):
                self.matrix[i][j]="[%c]"%(chr(value+j))
            elif(j==0):
                self.matrix[i][j]="[%d]"%(i-1)
            else:
                self.matrix[i][j]=self.matrix1[i-1][j-1]
                
      
             
      print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.matrix]))
  def uncover_one_element(self,c1,c2):
      
      if(self.check_matrix[c2][c1-97]==0):
          self.check_matrix[c2][c1-97]=1
          self.revealed_count=self.revealed_count+2
      else:
          print("number is already revealed")
      for i in range(self.size+1):
        for j in range(self.size+1):
            if(i==0 and j==0):
                self.matrix[i][j]=" "
                continue
            elif(i==0):
                self.matrix[i][j]="[%c]"%(chr(value+j))
            elif(j==0):
                self.matrix[i][j]="[%d]"%(i-1)
            else:
                 if(self.check_matrix[i-1][j-1]==1):
                    self.matrix[i][j]=self.matrix1[i-1][j-1]
                 else:
                    self.matrix[i][j]="x" 
           
      print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.matrix]))
  def predict_score(self):
    if(self.guessed_count==0):
        print("You Cheated-Loser!! Your Score is 0!")
    else:
        score=(self.proper_count/(self.guessed_count+self.revealed_count)*100)
        print("Oh Happy Day. You've won!! Your score is %d"%score)
   
      
    

    
               


    
