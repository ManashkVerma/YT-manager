# YT Manager

A simple command-line YouTube video manager written in Python. This tool allows you to keep track of your YouTube videos (or any list of videos) by adding, updating, deleting, and listing them. All data is stored in a local JSON file (`youtube.txt`).

---

## Features

- **List all videos:** View all saved videos with their names and durations.
- **Add a video:** Add a new video by entering its name and duration.
- **Update a video:** Update the name and duration of an existing video by selecting its index.
- **Delete a video:** Remove a video from the list by selecting its index.
- **Persistent storage:** All changes are saved to `youtube.txt` in JSON format.

---

## How It Works

1. **Startup:**

   - On running the script, it loads the video list from `youtube.txt` (if it exists). If not, it starts with an empty list.

2. **Menu Options:**

   - The program displays a menu with options to list, add, update, delete videos, or exit.
   - The user selects an option by entering the corresponding number.

3. **List Videos:**

   - Displays all videos with their index, name, and duration.

4. **Add Video:**

   - Prompts the user to enter the name and duration of a new video.
   - The new video is added to the list and saved.

5. **Update Video:**

   - Shows the current list of videos.
   - Prompts the user to enter the index of the video to update.
   - Asks for the new name and duration, then updates and saves the video.

6. **Delete Video:**

   - Shows the current list of videos.
   - Prompts the user to enter the index of the video to delete.
   - Removes the selected video and saves the updated list.

7. **Exit:**
   - Exits the program.

---

## Usage

1. **Run the script:**
   ```bash
   python YT_manager.py
   ```
2. **Follow the on-screen menu:**
   - Enter the number for the action you want to perform.
   - Provide the required information when prompted.

---

## File Structure

- `YT_manager.py` : Main Python script containing all logic.
- `youtube.txt` : Data file (auto-created) storing the list of videos in JSON format.
- `README.md` : This documentation file.

---

## Example

```
YT Manager || Choose an option
1. List all YT video
2. add YT video
3. update YT video
4. delete YT video
5. exit
Enter your Choice : 2
Enter video name : Python Tutorial
Enter time duration : 15:30
```

---

## Requirements

- Python 3.x

No external libraries are required (uses only Python's built-in `json` module).

---

## Author

- [Your Name Here]

---

## License

This project is for educational purposes.
