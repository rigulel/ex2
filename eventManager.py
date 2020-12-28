#### IMPORTS ####
import event_manager as EM

#### PART 1 ####
# Filters a file of students' subscription to specific event:
#   orig_file_path: The path to the unfiltered subscription file
#   filtered_file_path: The path to the new filtered file
def fileCorrect(orig_file_path: str, filtered_file_path: str):
    input_file = open(orig_file_path, "r")
    input_file_content = input_file.read()
    input_file.close()
    student_list = input_file_content.split('\n')
    student_list = [student_data.split(',') for student_data in student_list]
    student_list = [[strip_string(data) for data in student_data] for student_data in student_list]
    valid_students = [student for student in student_list if isStudentEntryValid(student)]
    out_file = open(filtered_file_path,"w")
    out_file.write('\n'.join([', '.join(student_entry) for student_entry in valid_students]))
    out_file.close()

def strip_string(string: str) -> str:
    word_list = string.split()
    return " ".join(word_list)

def validStudentsList(input_string: str)->list:
    student_list = input_string.split('\n')
    student_list = [student_data.split(',') for student_data in student_list]
    student_list = [[strip_string(data) for data in student_data] for student_data in student_list]
    valid_students = [student for student in student_list if isStudentEntryValid(student)]
    return valid_students

def isStudentEntryValid(student_entry: list) -> bool:
    if student_entry[0].startswith('0') or not len(student_entry[0]) == 8:
        return False
    if not all([(char.isalpha() or char.isspace()) for char in student_entry[1]]):
        return False
    if not (int(student_entry[2]) > 16 and int(student_entry[2]) < 120):
        return False
    if not (2020 - int(student_entry[2])) == int(student_entry[3]):
        return False
    if int(student_entry[4]) < 1:
        return False
    return True


# Writes the names of the K youngest students which subscribed 
# to the event correctly.
#   in_file_path: The path to the unfiltered subscription file
#   out_file_path: file path of the output file
def printYoungestStudents(in_file_path: str, out_file_path: str, k: int) -> int:
    if k < 0:
        return -1
    student_list = validStudentsList(in_file_path)
    student_list.sort(key=lambda student_entry: student_entry[2] + student_entry[0])
    out_file = open(out_file_path, "w")
    for i in range(min(k, len(student_list))):
        out_file.write(", ".join(student_list[i]))
        out_file.write("\n")
    out_file.close()
    return min(k, len(student_list))


    
# Calculates the avg age for a given semester
#   in_file_path: The path to the unfiltered subscription file
#   retuns the avg, else error codes defined.
def correctAgeAvg(in_file_path: str, semester: int) -> float:
    if semester < 1:
        return -1
    student_list = validStudentsList(in_file_path)
    if len(student_list) == 0:
        return 0
    age_list = ([student_entry[2] for student_entry in student_list if student_entry[4] == semester])
    return sum(age_list) / len(age_list)
    
    

#### PART 2 ####
# Use SWIG :)
# print the events in the list "events" using the functions from hw1
#   events: list of dictionaries
#   file_path: file path of the output file
def printEventsList(events :list,file_path :str): #em, event_names: list, event_id_list: list, day: int, month: int, year: int):
    pass
    #TODO   
    
    
def testPrintEventsList(file_path :str):
    events_lists=[{"name":"New Year's Eve","id":1,"date": EM.dateCreate(30, 12, 2020)},\
                    {"name" : "annual Rock & Metal party","id":2,"date":  EM.dateCreate(21, 4, 2021)}, \
                                 {"name" : "Improv","id":3,"date": EM.dateCreate(13, 3, 2021)}, \
                                     {"name" : "Student Festival","id":4,"date": EM.dateCreate(13, 5, 2021)},    ]
    em = printEventsList(events_lists,file_path)
    for event in events_lists:
        EM.dateDestroy(event["date"])
    EM.destroyEventManager(em)

#### Main #### 
# feel free to add more tests and change that section. 
# sys.argv - list of the arguments passed to the python script
if __name__ == "__main__":
    import sys
    if len(sys.argv)>1:
        testPrintEventsList(sys.argv[1])
