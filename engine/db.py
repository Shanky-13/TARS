import csv
import sqlite3

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'zoom', 'C:\\Users\\supriya\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'rave', 'C:\\Users\\supriya\\AppData\\Local\\Programs\\rave-desktop\\Rave.exe')"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'uTorrent', 'C:\\Users\\supriya\\AppData\\Roaming\\uTorrent Web\\utweb.exe')"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'Sejda PDF', 'C:\\Program Files\\Sejda PDF Desktop\\Sejda PDF Desktop.exe')"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'any desk', 'C:\\Program Files (x86)\\AnyDesk\\AnyDesk.exe')"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'Solidworks', 'C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\SLDWORKS.exe')"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'vs code', 'C:\\Users\\supriya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'Adobe Premier Pro', 'C:\\Program Files\\Adobe\\Adobe Premiere Pro 2024\\Adobe Premiere Pro.exe')"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'spotify', 'C:\\Program Files\\WindowsApps\\SpotifyAB.SpotifyMusic_1.265.255.0_x64__zpdnekdrzrea0\\Spotify.exe')"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'whatsapp', 'C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2523.1.0_x64__cv1g1gvanyjgm\\WhatsApp.exe')"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'armory crate', 'C:\\Program Files\\WindowsApps\\B9ECED6F.ArmouryCrate_6.1.13.0_x64__qmba6cd70vzyy\\ArmouryCrate.exe')"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'clipchamp', 'C:\\Program Files\\WindowsApps\\Clipchamp.Clipchamp_4.2.10220.0_x64__yxz26nhyzhsrt\\Clipchamp\\Clipchamp.exe')"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'telegram', 'C:\\Program Files\\WindowsApps\\TelegramMessengerLLP.TelegramDesktop_5.15.2.0_x64__t4vj0pshhgkwm\\Telegram.exe')"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'copilot', 'C:\\Program Files\\WindowsApps\\Microsoft.Copilot_1.25053.93.0_x64__8wekyb3d8bbwe\\Copilot.exe')"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'paint', 'C:\\Program Files\\WindowsApps\\Microsoft.Paint_11.2503.381.0_x64__8wekyb3d8bbwe\\PaintApp\\mspaint.exe')"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'prime video', 'C:\\Program Files\\WindowsApps\\AmazonVideo.PrimeVideo_1.0.174.0_x64__pwbj9vvecjh7j\\PrimeVideo.exe')"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'VLC', 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe')"
# cursor.execute(query)

# con.commit()


query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'youtube', 'https://www.youtube.com/')"
# cursor.execute(query)
# con.commit()

# query = "INSERT INTO web_command VALUES (null,'youtube', 'https://www.youtube.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'google', 'https://www.google.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'gmail', 'https://mail.google.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'facebook', 'https://www.facebook.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'instagram', 'https://www.instagram.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'whatsapp web', 'https://web.whatsapp.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'amazon', 'https://www.amazon.in/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'flipkart', 'https://www.flipkart.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'stackoverflow', 'https://stackoverflow.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'github', 'https://github.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'linkedin', 'https://www.linkedin.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'twitter', 'https://twitter.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'netflix', 'https://www.netflix.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'chatgpt', 'https://chat.openai.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'canva', 'https://www.canva.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'wikipedia', 'https://www.wikipedia.org/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'notion', 'https://www.notion.so/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'zoom', 'https://zoom.us/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'google drive', 'https://drive.google.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'google docs', 'https://docs.google.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'google meet', 'https://meet.google.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'one drive', 'https://onedrive.live.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'dropbox', 'https://www.dropbox.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'trello', 'https://trello.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'figma', 'https://www.figma.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'replit', 'https://replit.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'geeksforgeeks', 'https://www.geeksforgeeks.org/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'w3schools', 'https://www.w3schools.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'khan academy', 'https://www.khanacademy.org/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'coursera', 'https://www.coursera.org/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'udemy', 'https://www.udemy.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'edx', 'https://www.edx.org/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'openai', 'https://platform.openai.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'hugging face', 'https://huggingface.co/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'kaggle', 'https://www.kaggle.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'colab', 'https://colab.research.google.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'aws console', 'https://console.aws.amazon.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'azure portal', 'https://portal.azure.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'vercel', 'https://vercel.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'render', 'https://render.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'cloudflare', 'https://www.cloudflare.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'figma community', 'https://www.figma.com/community')"
# cursor.execute(query)

# con.commit()


# testing module
# app_name = "android studio"
# cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
# results = cursor.fetchall()
# print(results[0][0])

# Create a table with the desired columns
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')


# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
# desired_columns_indices = [0, 1]

# # Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# # # Commit changes and close connection
# con.commit()
# con.close()

# query = "INSERT INTO contacts VALUES (null,'raghav', '1234567890', 'null')"
# cursor.execute(query)
# con.commit()

# query = 's'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])