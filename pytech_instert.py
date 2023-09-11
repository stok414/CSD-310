client = MongoClient("localhost", 27017)

db = client["mydb"]

pytech = db["PyTech"]

records = [
    {
        "student_id": "1007",
        "first_name": "Sitha",
        "last_name": "Ok"
    },
    {
        "student_id": "1008",
        "first_name": "Ketch",
        "last_name": "Up"
    },
    {
        "student_id": "1009",
        "first_name": "Pizza",
        "last_name": "Pinapple"
    }
]