
#this is a list
courses = ["BSIT","BSBA","BSAE","BLIS","BSHM","BSHM"]

print(courses)
print(courses[0])

print("Start and End")
print(courses[1:3])

print("choose start and automatcally end")
print(courses[3:])

print("choosing end")
print(courses[:3])

print("start index")
print(courses[1])

print("Assigning list items")
courses[0] = "IDOL"

print("lenght")
print(len(courses))

print("Paulit ulit")
print(courses.count("BSHM"))

print("Add new Item")
courses.append("POGS")
print(courses)

print("Insert an item at the specified index")
courses.insert(1,"HUMAN")
print(courses)

print("Delete an item based on their value")
courses.remove("HUMAN")
print(courses)

print("POP Deletes an item based on their index but if index is not specified it deletes the last item")
courses.pop(0)
courses.pop()
print(courses)

print("DEL Deletes an item based on their index but if index is not specified it deletes the whole item")
del courses[0]
print(courses)

print("CLEAR deletes all the value in a list")
courses.clear()
print(courses)

print("copy the whole list which can be assigned to a new list")
coursesTwo = courses.copy()
print(courses)

print("COmbining Lists by adding")
coursesHEhe = ["bsffj","shdf","jzhdsgf"]
combine = coursesHEhe + courses
print(combine)

print("extend Combines lists by appending the specified list ti the end of the first list")
name1 = ["George","Albert","Jonathan"]
name2 = ["Robert","Jimboy","Paul"]
name1.extend(name2)
print(name1)
name1.append(name2)
print(name1)


print("Sorting ")
alphabet = ["A","B","L","E","F","Z","U","I","G","K"]
alphabet.sort()
print(alphabet)
alphabet.reverse()
print(alphabet)



