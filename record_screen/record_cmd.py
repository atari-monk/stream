from ffmpeg import build_ffmpeg_command, run_ffmpeg_command

def main():
    preset_name = input("Enter preset name (press Enter for default 'desktop_screen_capture_1'): ")
    
    if not preset_name:
        preset_name = 'desktop_screen_capture_1'

    try:
        command = build_ffmpeg_command(preset_name)
        print(f"Generated FFmpeg command: {command}")
        run_ffmpeg_command(command)
    except ValueError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()
