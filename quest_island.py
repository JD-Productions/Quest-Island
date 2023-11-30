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
post = tp.Trading_Post(user)
data = db.get_file()
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
            print("[2] Job Stars") #TODO: Create Function and Logic.
        print("[3] Quit")
        answer = intinput()
        if answer == 3:
            quit()
        elif answer == 1:
            post.main()
        elif answer == 2 and not data['job']:
            get_job()
        elif answer == 0 and data['job']:
            work()
        elif answer == 0 and not data['job']:
            beg()
	db.save_file(data)

def beg():
    money = random.randint(0,5)
    data['money'] += money
    db.save_file(data)
    print(f"You got {money} from begging")
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
    db.save_file(data)
    print(f"You worked as a {data['job']} and got {earned} dollars. You now go home.")
    return

def get_job():
        print("[0] Blacksmith")
        print("[1] Carpenter")
        answer = intinput()
        if answer == 0:
            data["job"] = "Blacksmith"
            print("Your job is now Blacksmith")
        elif answer == 1:
            data["job"] = "Carpenter"
            print("your job is now Carpenter")
        return

if __name__=='__main__':
    main()

