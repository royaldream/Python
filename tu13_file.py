from tu10_class import Student1
import os
fin = open("file1.txt", "w")
# fin.write("Hi I am Parth Roy ")
stu = Student1()
stu.name = "Parth Roy"
stu.age = 20
# print fin.read()
fin.write("Parth Roy")
fin.close()
# os.mkdir("tu13_file", "a")