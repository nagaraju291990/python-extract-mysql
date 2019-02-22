#program to convert tab seperated file to tmx (Transaltion Memory Exchange format)

import sys
from argparse import ArgumentParser
import re
import MySQLdb
import datetime

import config   #custom configuration file

'''
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
					 user="root",         # your username
					 passwd="root123",  # your password
					 db="userdb-01Dec17");        # name of the data base'
'''
encoding = "utf-8" 
db = MySQLdb.connect(host=config.server['dbhost'],    # your host, usually localhost
					 user=config.server['dbuser'],         # your username
					 passwd=config.server['dbpassword'],  # your password
					 db=config.server['dbname'],
					 charset='utf8',
					    use_unicode=True);        # name of the data base



parser = ArgumentParser(description='Calculate time spent in a tool')

parser.add_argument("-message", "--message",
                    dest="message", help="Specify a message to be extracted from db",required=True)
parser.add_argument("-u", "--username", dest="username",
                    help=" for logs of a specific user, default is all",required=True)
#parser.add_argument("-details" "--details",
#					dest="detail", help ="Optional-Value is yes or no, default is no")

args = parser.parse_args()

#print(args.username);
#print(args.date);
#sys.exit(0)

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()


def getLogMessages(message):
	#print(curdate)
	#print(message)
	#query = "select * from logs where userid='rashid' AND DATE(datetime) = '2018-10-17' ORDER BY datetime ASC";
	query = "select * from logs where message LIKE '%"+message+"%' ORDER BY datetime ASC";
	#print(query);

	#sys.exit(0)

	# Use all the SQL you like
	#cur.execute("SELECT * FROM logs LIMIT 15");
	cur.execute(query);

	flag = 0
	e=0
	idle_time = 0
	inc = 0

	#cur.fetchall()
	tc = cur.rowcount
	#print(tc)
	# print all the first cell of all the rows
	for row in cur.fetchall():
		log_message = row[2]
		print (row[0],row[2])


username = args.username;
message = args.message

##get mongousername from User_Id
#name_query = "select username from Users where User_Id='"+username+"'"
#cur.execute(name_query)

#for row in cur.fetchall():
#	mongousername = row[0]

#if(args.username):
#	username = args.username
#else:
#	username='all'

#print(detail)
#sys.exit(0)

getLogMessages(message)
db.close()
