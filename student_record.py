def to_grade_point(grade):
  if (grade >= 0 and grade <= 59):
    return ("'F'", 0.0)
  elif (grade >= 60 and grade <= 64):
    return ("'C+'", 2.3)
  elif (grade >= 65 and grade <= 69):
    return ("'B-'", 2.7)
  elif (grade >= 70 and grade <= 74):
    return ("'B'", 3.0)
  elif (grade >= 75 and grade <= 79):
    return ("'B+'", 3.3)
  elif (grade >= 80 and grade <= 84):
    return ("'A-'", 3.7)
  else:
    if (grade >= 85 and grade <= 100):
      return ("'A'", 4.0)

class GradeRecords:
  term = ""
  grades = list()
  num_courses = 0;

  def __init__(self, term):
    self.term = term

  def add_course(self, courseCode, grade, numCredits): #string, int, int
    tuple = (courseCode, grade, numCredits)
    self.grades.append(tuple)
    self.num_courses += 1

  def get_best_courses(self):
    bestGrades = list()
    bestLetterGrade = ""
    currentGrade = 0
    for element in self.grades:
      if (to_grade_point(currentGrade)[1] < element[1]):
        currentGrade = element[1]

    bestLetterGrade = to_grade_point(currentGrade)[0]
    
    for element in self.grades:
      if (to_grade_point(element[1])[0] == bestLetterGrade):
        bestGrades.append(element[0])
    return bestGrades

  def get_GPA(self):
    total = 0
    totalCredits = 0
    for element in self.grades:
      total += (to_grade_point(element[1])[1] * element[2])
      totalCredits += element[2]
    return round(total/totalCredits, 1)

  def to_dict(self):
    dictionary = dict()
    for element in self.grades:
      dictionary[element[0]] = to_grade_point(element[1])[0]
    return dictionary



gr = GradeRecords("Fall 2019")
print("First batch")
print("Term: {}".format(gr.term))

gr.add_course("COMP 202", 83, 3)
gr.add_course("CLAS 203", 75, 3)
gr.add_course("LING 360", 81, 3)

print("Number of courses: {}".format(gr.num_courses))
print("Best courses: {}".format(gr.get_best_courses()))
print("GPA: {}".format(gr.get_GPA()))
print("Dictionary: {}".format(gr.to_dict()))

print()

print("Second batch")
print("Term: {}".format(gr.term))

gr.add_course("COMP 551", 67, 4)
gr.add_course("HIST 318", 88, 3)

print("Number of courses: {}".format(gr.num_courses))
print("Best courses: {}".format(gr.get_best_courses()))
print("GPA: {}".format(gr.get_GPA()))
print("Dictionary: {}".format(gr.to_dict()))






