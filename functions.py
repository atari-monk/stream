import json

def build_ffmpeg_command(preset_name, file='config.json',  presets_name = 'presets'):
    with open(file, 'r') as f:
        presets_data = json.load(f)
    
    presets = presets_data[presets_name]
    
    if not presets:
        raise ValueError(f"'{presets_name}' not found in the JSON file!")
    
    preset = presets.get(preset_name)

    if not preset:
        raise ValueError(f"Preset '{preset_name}' not found!")
    
    return " ".join([f"{part['flag']} {part['value']}" for part in preset])
