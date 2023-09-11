for record in records:
    new_student_Id = pytech.insert_one(record).inserted_id
    print(new_student_Id)
    
docs = pytech.find()

for doc in docs:
    print(doc)
    
print(pytech.find_one({"student_id": "1008"}))