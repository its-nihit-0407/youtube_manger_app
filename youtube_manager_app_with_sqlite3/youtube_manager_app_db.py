import sqlite3

conn = sqlite3.connect("youtube_video.db")

cur = conn.cursor()

cur.execute('''
            CREATE TABLE IF NOT EXISTS VIDEOS (
                ID INTEGER PRIMARY KEY,
                VIDEO_NAME TEXT NOT NULL,
                VIDEO_TIME TEXT NOT NULL
            )                           
''')

conn.commit()

def list_videos():

    cur.execute("SELECT * FROM VIDEOS;")

    print("\n" + "*"*70)

    videos = cur.fetchall()

    if videos != []:

        for vid in videos:

            print(vid)
    else:

        print("EMPTY")


def add_video(name, time, idx):

    cur.execute("INSERT INTO VIDEOS (ID, VIDEO_NAME, VIDEO_TIME) VALUES (?, ?, ?)", (idx, name, time))

    conn.commit()
    
def update_video(new_name, new_time, idx):

    cur.execute("UPDATE VIDEOS SET VIDEO_NAME = ?, VIDEO_TIME = ? WHERE ID = ?", (new_name, new_time, idx))

    conn.commit()
    
def delete_video(idx):

    cur.execute("DELETE FROM VIDEOS WHERE ID = ?", (idx,))

def main():
    
    while True:
    
        print("\n Youtube Manager App using sqlite3")
        print("1. list all videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. exit")
        
        choice = input("Enter your choice: ")
        
        if (choice == "1"):
            list_videos()
    
        elif (choice == "2"):
    
            idx = int(input("Enter video ID: "))
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time, idx)
    
        elif (choice == "3"):
    
            idx = int(input("Enter video ID: "))
            new_name = input("Enter the video new_name: ")
            new_time = input("Enter the video new_time: ")
            update_video(new_name, new_time, idx)
    
        elif (choice == "4"):
    
            idx = int(input("Enter video ID to delete: "))
            delete_video(idx)
    
        elif (choice == "5"):
    
            break
    
        else:
    
            print("Invalid Choice")
            

if (__name__ == "__main__"):
    main()