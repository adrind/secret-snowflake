##Created by Adrienne Dreyfus 11/22/12
##Free to use/edit however you'd like

import os
import random
import smtplib
import sys
from email.mime.text import MIMEText

gmail_user = ##YOUR E-MAIL HERE
pwd = ##YOUR PASSWORD HERE

def send_email(email, msg):
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(gmail_user, pwd)
    s.sendmail(gmail_user, [email], msg.as_string())
    s.quit()

#returns a shuffled paralell array of names
#corresponding to secret snowflake matches
def shuffle(names, shuffled_names):
    reshuffle = True
    while reshuffle:
        random.shuffle(shuffled_names)
        zipped = zip(names, shuffled_names)
        reshuffle = False
        #quick check to make sure no one has herself
        for (x, y) in zipped:
            if x == y:
                reshuffle = True
    return shuffled_names

if len(sys.argv) < 3:
    print("REQUIRED: ssnowflake.py [list-of-names-and-emails] [path-of-dir]\n")
else:
    name_file = sys.argv[1]
    dir_path = sys.argv[2]
    f = open(name_file, 'r')
    person_list = f.read().strip().split(',')
    person_list = [person.strip().split(' ') for person in person_list]
    names = [person[0] for person in person_list]
    shuffled_names = [person[0] for person in person_list]
    shuffled_names = shuffle(names, shuffled_names)
    for index in range(len(person_list)):
        (name, email) = person_list[index]
        snowflake = shuffled_names[index]
        msg = MIMEText(" Hey " + str(name) + "!\n Your Secret "
                "Snowflake is " + str(snowflake) + "\n Get them something "
                "good!!\n ")
        msg['Subject'] = "Secret Snowflake!"
        msg['From'] = gmail_user
        msg['To'] = email
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        f = open(str(dir_path) + "/" + str(name), 'w+')
        f.write(snowflake)
        send_email(email, msg)
    sys.exit()
