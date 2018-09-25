import serial
import time
from model import session, registerDB
ser = serial.Serial('/dev/ttyACM1', 9600)


if __name__ == "__main__":
    ser.write(b'1')
    print("Please put your finger")
    while 1:
        if(ser.readline().decode() == '1\r\n'):
            ID = ser.readline().decode().strip()

            print(ID)
            if session.query(registerDB).filter_by(sid=ID).first():
                print("let's vote")
                voteID = input("enter your vote no.")
                session.query(registerDB).filter_by(
                    sid=ID).first().vote = voteID

                session.commit()
                print('Thanks for your vote')
                exit(0)
            else:
                print('no ID found')

        elif(ser.readline().decode() == '4\r\n'):
            print("You are not a registered voter")
