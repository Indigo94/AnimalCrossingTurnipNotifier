import praw
import re
import datetime
import json
from playsound import playsound
import sys



f = open('credentials.json',)
data = json.load(f)
app_id = data['app_id']
app_secret = data['app_secret']

if(app_id == "" or app_secret == ""):
    print("Please update the values in credentials.json. Refer to the readme for more instructions")
    sys.exit()
sample_number = int(input("Please enter the minimum turnips selling value: "))
intervalSeconds = int(input("Please enter the amount of time in seconds that the program will check the reddit page: "))

reddit = praw.Reddit(client_id= app_id,
                     client_secret = app_secret,
                     user_agent = "Sample user agent")

previous_submission = None

for submission in reddit.subreddit("TurnipExchange").new(limit=1):
    previous_submission = submission

turnips_compiler = re.compile(r'\d\d\d')

# print(turnips_compiler.findall(previous_submission.title))
current_time = datetime.datetime.now()

flag = True
counter = 0
while flag:
    if(datetime.datetime.now() - current_time).seconds > intervalSeconds:
        temporary_submission = None
        for submission in reddit.subreddit("TurnipExchange").new(limit=1):
            temporary_submission = submission
        if(previous_submission == temporary_submission):
            current_time = datetime.datetime.now()
            counter += 1
            print("{}: Nothing new".format(counter))
            continue
        if(previous_submission != temporary_submission):
            turnips_list = turnips_compiler.findall(temporary_submission.title)
            if(len(turnips_list) > 0 and int(turnips_list[0]) >= sample_number):
                print("Looks like someone's island is offering {} for their turnips".format(turnips_list[0]))
                playsound('coin.wav')
                current_time = datetime.datetime.now()
                flag = False
            elif len(turnips_list) == 0:
                print(temporary_submission.title)
                print("Someone made a post without including the value for a turnip. Continuing to monitor posts")
                previous_submission = temporary_submission
                current_time = datetime.datetime.now()
            else:
                print(temporary_submission.title)
                print("Someone's turnip value is less than the threshold. Continuing to monitor posts")
                previous_submission = temporary_submission
                current_time = datetime.datetime.now()
