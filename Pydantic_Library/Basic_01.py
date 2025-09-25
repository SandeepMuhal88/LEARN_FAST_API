#There is a problem Data validation 
#Not write the boyler code


def insert_patient(name: str,age: int):
    if type(name) ==str and type(age)== int:
        if age < 0:
            raise ValueError("Age cannot be negative")
        else:
            print(f"Inserting patient {name} with age {age}")
            print("Data inserted successfully")
    else:
        raise ValueError("Invalid data type")

def update_patient(name: str,age: int):
    if type(name) ==str and type(age)== int:
        if age < 0:
            raise ValueError("Age cannot be negative")
        else:
            print(f"Updating patient {name} with age {age}")
            print("Data updated successfully")
    else:
        raise ValueError("Invalid data type")

insert_patient("John",30)
update_patient("Deepak",70)
