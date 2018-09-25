from model import session, registerDB

for r in session.query(registerDB.vote).distinct():
    print("Total vote for {} is {}".format(
        r[0], session.query(registerDB).filter_by(vote=r[0]).count()))
