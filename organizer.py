import os
import shutil

def organize_folder():
    # 1. Jis folder mein ye script hai, uski saari files ki list nikaalo
    files = os.listdir('.')
    
    for file in files:
        # Script file ko khud ko move nahi karna hai
        if file == 'organizer.py':
            continue
            
        # 2. Agar file ke aakhir mein .txt hai
        if file.endswith('.txt'):
            if not os.path.exists('Text_Files'):
                os.makedirs('Text_Files') # Naya folder banao
            shutil.move(file, 'Text_Files') # File ko andar daal do
            print(f"Moved {file} to Text_Files/")
            
        # 3. Agar file ke aakhir mein .jpg ya .png hai
        elif file.endswith('.jpg') or file.endswith('.png'):
            if not os.path.exists('Image_Files'):
                os.makedirs('Image_Files')
            shutil.move(file, 'Image_Files')
            print(f"Moved {file} to Image_Files/")

        # 4. Agar file ke aakhir mein .pdf hai
        elif file.endswith('.pdf'):
            if not os.path.exists('PDF_Files'):
                os.makedirs('PDF_Files')
            shutil.move(file, 'PDF_Files')
            print(f"Moved {file} to PDF_Files/")

if __name__ == "__main__":
    print("Starting Directory Cleanup...")
    organize_folder()
    print("Folder is now organized! 😎")