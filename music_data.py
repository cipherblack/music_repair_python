import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TDRC
from mutagen.mp4 import MP4

path = input("Enter file or folder path: ").strip()

def add_metadata_to_mp3(file_path):
    try:
        audio = MP3(file_path, ID3=ID3)
        bitrate = getattr(audio.info, 'bitrate', 'Unknown')
        duration = getattr(audio.info, 'length', 'Unknown')
        
        if audio.tags is None:
            audio.tags = ID3()
            audio.tags.add(TIT2(encoding=3, text="Unknown Title"))
            audio.tags.add(TPE1(encoding=3, text="Unknown Artist"))
            audio.tags.add(TALB(encoding=3, text="Unknown Album"))
            audio.tags.add(TDRC(encoding=3, text="Unknown Year"))
            audio.save()

        print(f"Metadata updated for: {file_path} | Bitrate: {bitrate} | Duration: {duration} seconds")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def add_metadata_to_mp4(file_path):
    try:
        audio = MP4(file_path)
        bitrate = getattr(audio.info, 'bitrate', 'Unknown')
        duration = getattr(audio.info, 'length', 'Unknown')
        
        if not audio.tags:
            audio.tags["\xa9nam"] = "Unknown Title"
            audio.tags["\xa9ART"] = "Unknown Artist"
            audio.tags["\xa9alb"] = "Unknown Album"
            audio.save()

        print(f"Metadata updated for: {file_path} | Bitrate: {bitrate} | Duration: {duration} seconds")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def process_music_file(file_path):
    if file_path.lower().endswith(".mp3"):
        add_metadata_to_mp3(file_path)
    elif file_path.lower().endswith((".m4a", ".mp4")):
        add_metadata_to_mp4(file_path)
    else:
        print(f"Unsupported file format: {file_path}")

def process_music_folder(folder_path):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            process_music_file(file_path)

if os.path.exists(path):
    if os.path.isdir(path):
        process_music_folder(path)
    elif os.path.isfile(path):
        process_music_file(path)
    else:
        print("Invalid path.")
else:
    print("Path does not exist.")
