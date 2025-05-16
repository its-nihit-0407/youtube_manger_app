# youtube_manger_app

```python
import json

def load_data():
    
    try:
    
        with open("youtube.txt", "r") as file:
    
            data = json.load(file)
    
            return data
    
    except FileNotFoundError:
    
        return []

def save_data_helper(videos):
    
    with open("youtube.txt", "w") as file:
    
        json.dump(videos, file)
        
def list_all_videos(videos):
    
    for index, vid in enumerate(videos, start=1):
    
        print(f"{index}. {vid}")
        
def add_youtube_video(videos):
    
    name = input("Enter video name: ")
    
    time = input("Enter video time: ")
    
    videos.append({"name": name, "time": time})
    
    save_data_helper(videos)

def update_video_details(videos):
    
    list_all_videos(videos)
    
    index = int(input("Enter the video index: "))
    
    if 1 <= index <= len(videos):
    
        name = input("Enter video name: ")
    
        time = input("Enter video time: ")
    
        videos[index -1] = {"name": name, "time": time}
    
        save_data_helper(videos)

def delete_video(videos):
    
    list_all_videos(videos)
    
    index = int(input("Enter the number of video: "))
    
    
    if 1 <= index <= len(videos):
    
        del videos[index - 1]
    
        save_data_helper(videos)
    
    else:
    
        print("Invalid Index")  


def main():
    
    videos = load_data()
    
    while True:
    
        print("\n Youtube Manager | choose an option")
        print("1. list all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        
        choice = input("Enter your choice: ")
        
        match (choice):
    
            case "1":
                list_all_videos(videos)
            case "2":
                add_youtube_video(videos)
            case "3":
                update_video_details(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid choice")
                
if __name__ == "__main__":
    main()
```

## YOUTUBE MANAGER APP USING SQLITE3
```python
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
```