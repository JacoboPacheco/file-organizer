import os
import shutil

images = {"jpg", "png", "jpeg"}
videos = {"mp4", "mkv"}
documents = {"pdf", "txt", "docx"}
code = {"py", "js", "html", "css"}

folder_path = input("Please enter a folder path: ")

for i in os.listdir(folder_path):
    full_path = os.path.join(folder_path, i)

    if os.path.isfile(full_path):
        name, extension = os.path.splitext(i)
        extension = extension[1:].lower()

        if extension in images:
            category = "images"
        elif extension in videos:
            category = "videos"
        elif extension in documents:
            category = "documents"
        elif extension in code:
            category = "code"
        else:
            category = "other"

        destination_folder = os.path.join(folder_path, category)

        if not os.path.exists(destination_folder):
            os.mkdir(destination_folder)

        destination_path = os.path.join(destination_folder, i)
        shutil.move(full_path, destination_path)
