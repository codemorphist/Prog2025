from datetime import datetime                                       
from models import Student, StudentList

sl = StudentList.random_students(103)

# __import__('pprint').pprint(sl)
__import__('pprint').pprint(sl.calculate_scholarship())


