from dataclasses import dataclass
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import sqlite3
import os


# Creates a connection between the database and python
def create_connection():
    global con, cur
    con = sqlite3.connect("Linuxhotd.db")
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS commands (id integer primary key, command text NOT NULL, description text NOT NULL);''')
    con.commit()

# Closes the database connection
def close_connection():
    con.close()

create_connection()

# decides what elements can be in the email
def message(subject="Linux Hint of the day", 
            text="", img=None, attachment=None):

    msg = MIMEMultipart()

    msg["Subject"] = subject

    msg.attach(MIMEText(text))

    # check if there is img
    if img is not None:

        # check if img is list
        if type(img) is not list:
            
            # make img list
            img = [img]
        
        for one_img in img:

            img_data = open(one_img, "rb").read()


            msg.attach(MIMEImage(img_data,
                                name=os.path.basename(one_img)))
    return msg

# Fetches linux command from database (needs work)
hotd = cur.execute("""SELECT commands.command, 
            commands.description 
            from commands
            ORDER BY id
            LIMIT 1""").fetchall()


# handles composition and sending of the email
def mail():

    # initialize connection to the gmail server
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.ehlo()
    smtp.starttls()

    #login with email and password
    # smtp.login("linuxhotd@gmail.com", "liniiuxhotdu06")
    smtp.login("abdimalik.omar@chasacademy.se", "kroo202222")

    # This is where you decide what is in the actual mail
    msg = message("Linux Hint of the day!", "Thank you for subscribing to the daily Hint!! Todays useful command is: '" + hotd[0][0]+ "',  " + hotd[0][1],
                    r"Linux-Logo-1996-present.png")
    # print(hotd)
    # Who is receiving the email
    to = ["abdimalik.omar@chasacademy.se"]

    smtp.sendmail(from_addr="linuxhotd@gmail.com",
                 to_addrs=to, msg=msg.as_string())

    smtp.quit()

message()
mail()
