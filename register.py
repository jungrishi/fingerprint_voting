
import serial
import time
from model import session, registerDB
ser = serial.Serial('/dev/COM4', 9600)

# %%


def fingerprint():

    id = session.query(registerDB).count()
    ser.write(b'1')
    for i in range(2):
        print(ser.readline().decode())
    print("ID {}".format(id))
    ser.write(str(id).encode())
    while 1:
        data = ser.readline().decode()
        print(data)
        if data == '1\r\n':
            session.query(registerDB).filter_by(
                sid=id).first().fingerprinted = 1

            session.commit()
            print("done")
            exit(0)
        elif data == '0\r\n':
            print("error taking fingerprint")


if __name__ == "__main__":
    Firstname = input("Enter your firstname ")
    Lastname = input("Enter your Lastname ")
    Nationality = input("Enter your Nationality ")
    DOB = input("Enter your DOB ")

    registerOBJ = registerDB(firstname=Firstname, lastname=Lastname,
                             DOB=DOB, nationality=Nationality)

    session.add(registerOBJ)
    session.commit()
    fingerprint()
