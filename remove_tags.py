import eyed3
import os

folder_path = input("Enter path :")

def remove_metadata(folder_path):
    for file in os.listdir(folder_path):
        if file.endswith(".mp3"):
            file_path = os.path.join(folder_path, file)
            try:
                audio = eyed3.load(file_path)
                if audio and audio.tag:
                    audio.tag.clear()
                    audio.tag.save()
                    print(f"Metadata removed: {file}")
                else:
                    print(f"No metadata found: {file}")
            except Exception as e:
                print(f"Error processing {file}: {e}")

remove_metadata(folder_path)
