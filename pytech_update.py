import pymongo

#connect to database
client = pymongo.MongoClient()
db = client["Pytech"]
students = db["students"]

#finds students
print("Displaying all students:")
for student in students.find():
    print(student)

#update the last name of the student
print("Updating the last name of student with ID 1007 to 'Ok'...")
students.update_one({"student_id": 1007}, {"$set": {"last_name": "Ok"}})

#find specific student for this example 1007
print("Displaying the updated student document:")
student = students.find_one({"student_id": 1007})
print(student)