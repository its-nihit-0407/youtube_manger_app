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