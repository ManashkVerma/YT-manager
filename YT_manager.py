import json

def load_data():
    try:
        with open("youtube.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print('\n')
    print("*" * 70)
    for idx, video in enumerate(videos, start=1):
        print(f"{idx}. {video['name']}, duration: {video['duration']}")
    print('\n')
    print("*" * 70)

def add_video(videos):
    name = input("Enter video name : ")
    duration = input("Enter time duration : ")
    videos.append({"name": name, "duration": duration})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("idx to Update : "))
    if 1 <= index <= len(videos):
        n = input("Enter name : ")
        d = input("Enter Duration : ")
        videos[index-1] = {"name": n, "duration": d}
        save_data_helper(videos)
    else:
        print("Enter valid input")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter idx to be deleted"))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Enter valid input")


def main():
    videos = load_data()
    while True:
        print('\n')
        print("YT Manager || Choose an option")
        print("1. List all YT video")
        print("2. add YT video")
        print("3. update YT video")
        print("4. delete YT video")
        print("5. exit")
        choice = input("Enter your Choice : ")

        match choice:
            case '1': 
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break

if __name__ == "__main__":
    main()
      