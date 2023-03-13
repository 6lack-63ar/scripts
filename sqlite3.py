import sqlite3


phone_number= '0704907862'

try :
    data = sqlite3.connect("washwash.db")
    cur = data.cursor()

    create = "CREATE TABLE IF NOT EXISTS DETAILS (PHONE_NO VARCHAR(30))"

    cur.execute(create)
    add=f"INSERT INTO DETAILS VALUES('{phone_number}')"
    cur.execute(add)
    data.commit()
    data.close()
    print("data added successfully")
except:
    print("error Occured")

