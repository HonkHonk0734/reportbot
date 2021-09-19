from colorama.ansi import Fore
from reportstest2 import reportedUsers
import discord
import sqlite3
import datetime as dt
import time



client = discord.Client()

conn = sqlite3.connect('test2.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS reportusers(
            reported text,
            reason text,
            date text,
            report text
            )""")

print(Fore.GREEN+"Started")

TOKEN = 'ODg4MDYxNjQ4OTA3MTQ5MzMz.YUNN3A.ntnrbyefTq5sJvFidz5uFgbjQxg'

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

    async def on_message(self, message):
        args = message.content.split(" ")
        if args[0] == "!report":
            # print(len(args))
            if len(args) == 2:
                await message.channel.send('you need to specify a reason')
            else:
                await message.channel.send('Making a report...')
                messageauthor = message.mentions
                reportidunfinale = args[1]
                if len(reportidunfinale) != 22:
                    await message.channel.send('this is not a valid user')
                else:
                    report_id_finale = reportidunfinale[2:21]
                    length = len(args)
                reason_list = args[2:length]
                reason_string = ' '.join(reason_list)
                # print(type(messageauthor))
                # print(messageauthor)
                print(report_id_finale + "\n" + reason_string)
                current_date = dt.date.today()
                string_date = current_date.strftime('%Y-%m-%d')
                print(string_date)
                reported = 'reported'
                c.execute("INSERT INTO reportusers VALUES (?, ?, ?, ?)", (report_id_finale, reason_string, string_date, reported))
                conn.commit()

                async def on_message():
                    if args[0] == "!stop":
                        print('connection with database is closing')
                        conn.close()
                        print('3')
                        time.sleep(1)
                        print('2')
                        time.sleep(1)
                        print('1')
                        time.sleep(1)
                        print('0')
                        print("closing connection..")
                        print('connection closed')
                        time.sleep(1)
                        print('stopping program')
                        time.sleep(1)
                        print('program stopped')
                        exit()

conn.commit()

client = MyClient()
client.run(TOKEN)