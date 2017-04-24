class Person: # can put object as argument, assumed if omitted. set metaclass to ABCMeta if you want abstract
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
      
class Student(Person):
    def __init__ (self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores
    
    def __gradeFromAvg(self, avg): # not the best, now student has access to change its grade.. how to make functions private?
        if avg >= 90 and avg <= 100:
            return "O"
        elif avg >= 80 and avg < 90:
            return "E"
        elif avg >= 70 and avg < 80:
            return "A"
        elif avg >= 55 and avg < 70:
            return "P"
        elif avg >= 40 and avg < 55:
            return "D"
        else:
            return "T"
        
    def calculate(self):
        sum = 0
        for i in self.scores:
            sum += i
        
        # avg = sum / len(self.scores)
        # if avg >= 90 and avg <= 100:
        #     return "O"
        # elif avg >= 80 and avg < 90:
        #     return "E"
        # elif avg >= 70 and avg < 80:
        #     return "A"
        # elif avg >= 55 and avg < 70:
        #     return "P"
        # elif avg >= 40 and avg < 55:
        #     return "D"
        # else:
        #     return "T"
        
        return self.__gradeFromAvg (sum / len(self.scores))  

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
