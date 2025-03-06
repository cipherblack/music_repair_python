
# Audio File Processing Script

This Python script processes audio files in various formats and standardizes their parameters (e.g., bit rate, sample rate, channels) using `ffmpeg`. It supports formats like `.mp3`, `.wav`, `.aac`, `.flac`, and `.ogg`. The script can process individual files or entire folders of audio files. It replaces the original files with the processed versions once completed.

## Features

- Supports multiple audio formats (`.mp3`, `.wav`, `.aac`, `.flac`, `.ogg`).
- Converts audio files to a consistent format with the following properties:
  - 2 audio channels (stereo).
  - Sample rate of 44100 Hz.
  - Bitrate of 192k (where applicable).
- Processes both individual files and entire directories.
- Uses `ffmpeg` for audio processing.
- Automatically deletes the original file and renames the processed file to the original name.

## Requirements

Before running the script, you need to have the following installed:

1. **Python 3**: Make sure Python 3 is installed on your machine. You can download it from [here](https://www.python.org/downloads/).
2. **FFmpeg**: The script relies on `ffmpeg` to process the audio files. You can install `ffmpeg` from [FFmpeg.org](https://ffmpeg.org/download.html).
   - On **Windows**, you can download the executable and add the folder to the system's PATH.
   - On **MacOS**, you can use Homebrew: `brew install ffmpeg`.
   - On **Linux**, you can install it via your package manager: `sudo apt install ffmpeg`.

## How It Works

The script works by reading audio files from a specified directory or from an individual file. It then processes each file using `ffmpeg` and converts it to the target audio format with consistent settings. After processing, it deletes the original file and renames the temporary processed file to the original file's name.

The supported audio formats and their respective conversion settings are as follows:

- **.mp3**: Converts to stereo, 44100 Hz sample rate, 192k bitrate, in `mp3` format.
- **.wav**: Converts to stereo, 44100 Hz sample rate, in `wav` format.
- **.aac**: Converts to stereo, 44100 Hz sample rate, 192k bitrate, in `adts` format.
- **.flac**: Converts to stereo, 44100 Hz sample rate, in `flac` format.
- **.ogg**: Converts to stereo, 44100 Hz sample rate, 192k bitrate, in `ogg` format.

## How to Use

### Step 1: Clone or Download the Script

Clone or download this repository to your local machine.

### Step 2: Run the Script

Run the script using the following command:

```bash
python ffmpeg.py
```

### Step 3: Enter the Path

The script will prompt you to enter the path of the file or folder you want to process. You can provide either:

- **A specific file path** (e.g., `C:/music/song.mp3`).
- **A folder path** (e.g., `C:/music/`).

If you provide a folder path, the script will process all the supported audio files within the folder.

### Example Usage

**Processing a Single File:**

```bash
C:/music/song.mp3
```

**Processing an Entire Folder:**

```bash
C:/music/
```

## How the Code Works

### Libraries Used:

1. **os**: 
   - Used for handling file paths, checking file existence, and renaming/deleting files.
   
2. **subprocess**: 
   - Used to run the `ffmpeg` command-line tool for processing audio files.

### Core Functions:

- **process_music_file(file_path)**:
  - Takes a file path, checks if the file extension is supported, and processes the file using `ffmpeg`.
  - If the conversion is successful, the original file is replaced with the processed file.

- **process_music_folder(folder_path)**:
  - Loops through all files in the specified folder and processes each one that has a supported audio file extension.

- **main()**:
  - Prompts the user for a file or folder path and processes the specified path accordingly.
  
## Error Handling

The script handles errors related to:
- Unsupported file formats.
- Missing `ffmpeg` tool.
- Files that cannot be processed for any other reason.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This script uses `ffmpeg`, a powerful multimedia framework for handling audio and video files.
- `ffmpeg` can be downloaded from [FFmpeg.org](https://ffmpeg.org/).
