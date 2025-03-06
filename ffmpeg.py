import os
import subprocess

SUPPORTED_FORMATS = {
    '.mp3': ['-vn', '-ac', '2', '-ar', '44100', '-ab', '192k', '-f', 'mp3'],
    '.wav': ['-vn', '-ac', '2', '-ar', '44100', '-f', 'wav'],
    '.aac': ['-vn', '-ac', '2', '-ar', '44100', '-ab', '192k', '-f', 'adts'],
    '.flac': ['-vn', '-ac', '2', '-ar', '44100', '-f', 'flac'],
    '.ogg': ['-vn', '-ac', '2', '-ar', '44100', '-ab', '192k', '-f', 'ogg']
}

def process_music_file(file_path):
    file_ext = os.path.splitext(file_path)[1].lower()
    if file_ext not in SUPPORTED_FORMATS:
        print(f"The file {file_path} is not a supported audio format.")
        return
    
    temp_file = f"{file_path}.temp"
    try:
        subprocess.run([
            'ffmpeg', '-i', file_path, *SUPPORTED_FORMATS[file_ext], temp_file
        ], check=True)
        os.remove(file_path)
        os.rename(temp_file, file_path)
        print(f"Processed and replaced: {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error processing {file_path}: {e}")
        if os.path.exists(temp_file):
            os.remove(temp_file)
    except Exception as e:
        print(f"An unexpected error occurred with {file_path}: {e}")
        if os.path.exists(temp_file):
            os.remove(temp_file)

def process_music_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and any(filename.lower().endswith(ext) for ext in SUPPORTED_FORMATS):
            process_music_file(file_path)

def main():
    path = input("Enter file or folder path: ").strip()
    
    if os.path.exists(path):
        if os.path.isdir(path):
            process_music_folder(path)
        elif os.path.isfile(path):
            process_music_file(path)
        else:
            print("Invalid path.")
    else:
        print("Path does not exist.")

if __name__ == "__main__":
    main()
