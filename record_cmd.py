import pyperclip
from functions import build_ffmpeg_command

def main():
    preset_name = input("Enter preset name: ")
    
    try:
        command = build_ffmpeg_command(preset_name)
        print(f"Generated FFmpeg command: {command}")
        
        pyperclip.copy(command)
        print("Command copied to clipboard.")
        
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
