import pymongo

#connection
client = pymongo.MongoClient()
db = client["pytech"]
students = db["students"]

#all docs via students
print("Before deleting documents:")
for student in students.find():
    print(student)

#new docs for student collection
new_student = {
    "student_id": 1010,
    "first_name": "Teen",
    "last_name": "Agers",
    "email": "teenagers@bellevue.edu",
}
students.insert_one(new_student)

#find specific students
print("\nAfter inserting a new document:")
document = students.find_one({"student_id": 1010})
print(document)

#delete them
students.delete_one({"student_id": 1010})

#find students again
print("\nAfter deleting a document:")
for student in students.find():
    print(student)