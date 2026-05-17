# Smart Directory Organizer 📂✨

A lightweight and efficient Command-Line automation tool built in Python to tackle the hassle of cluttered folders. The script scans the current working directory, dynamically creates separate folders based on file extensions (like `.txt`, `.jpg`, `.png`), and automatically moves the files into their respective homes.

## 🛠️ Features
- **Auto-Detection:** Reads all files in the execution directory.
- **Dynamic Folder Creation:** Automatically creates `Text_Files/` and `Image_Files/` folders if they don't exist.
- **Safety Lock:** Explicitly ignores the script file (`organizer.py`) itself to prevent self-displacement.

## 💻 Technologies Used
- **Python 3**
- **OS Module** (for file-system interaction)
- **Shutil Module** (for high-level file operations)

## 🚀 How to Run
1. Place `organizer.py` inside the cluttered folder.
2. Open your terminal/PowerShell in that directory.
3. Run the following command:
   ```bash
   python organizer.py