#This is Quest Island.
#A game of randomness...

import random, math
import database
import tp

def intinput(question=""):
	answer = input(question).strip()
	try:
		int(answer)
		return int(answer)
	except:
		pass

print("""\n\n\n!!!!!!!!!!WARNING!!!!!!!!!!
THIS IS A DEMO!\n\n\n""")

print("\n\n\nWelcome To Quest Island!")
user = database.choose_user()
db = database.Db(user)
data = db.get_file()
post = tp.Trading_Post(user)
def main():
    while True:
        stats = """User: {user}
Money: ${money}
Job:   {job}""".format(user=db.user, money=data['money'], job=('None' if not data['job'] else data['job']))
        print("\nStats:")
        print(stats)
        print("=============================")
        print("Options:")
        if not data['job']:
            print("[0] Beg for Money")
        else:
            print("[0] Work")
        print("[1] Trading Post")
        if not data['job']:
            print("[2] Get a job")
        else:
            work()
        answer = intinput()
        if answer == 1:
            post.main()
        if answer == 2 and not data['job']:
            get_job()
        db.save_file(data)

def beg():
    print("Sorry! This feature is unavailiable on the demo version.")
    return

def work():
    # Blacksmiths average $15-22/hour
    # Carpenter average   $16-36/hour
    # 
    earned = 0
    if data['job'] == "Blacksmith":
        wage = random.randint(15, 22)
    if data['job'] == "Carpenter":
        wage = random.randint(16, 36)
    earned = 8 * wage
    data['money'] += earned
    print(f"You worked as a {data['job']} and got {earned} dollars. You now go home.")
    return

def get_job():
    print("Sorry! This feature is unavailiable on the demo version.")
    return

if __name__=='__main__':
    main()

