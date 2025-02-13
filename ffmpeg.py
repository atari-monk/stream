import json
import subprocess
import os

def build_ffmpeg_command(preset_name, file='config.json', presets_name='presets'):
    # Check if file exists
    if not os.path.isfile(file):
        raise FileNotFoundError(f"The file '{file}' was not found.")
    
    with open(file, 'r') as f:
        presets_data = json.load(f)
    
    presets = presets_data.get(presets_name)
    
    if not presets:
        raise ValueError(f"'{presets_name}' not found in the JSON file!")
    
    preset = presets.get(preset_name)

    if not preset:
        raise ValueError(f"Preset '{preset_name}' not found!")

    # Ensure the preset is a list
    if not isinstance(preset, list):
        raise ValueError(f"Preset '{preset_name}' should be a list of parts, not a {type(preset)}.")
    
    command = []
    for part in preset:
        if isinstance(part, dict):
            if 'flag' in part:
                command.append(part['flag'])
            if 'value' in part:
                command.append(part['value'])
    
    return command

def run_ffmpeg_command(command):
    try:
        ffmpeg_command = ['ffmpeg'] + command
        result = subprocess.run(ffmpeg_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("FFmpeg command executed successfully.")
        
        # Only decode if there is output
        if result.stdout:
            print(result.stdout.decode())
        if result.stderr:
            print(result.stderr.decode())
            
    except subprocess.CalledProcessError as e:
        print(f"Error during FFmpeg execution: {e}")
        
        # Print the output even if there's an error
        if e.stdout:
            print(e.stdout.decode())
        if e.stderr:
            print(e.stderr.decode())
