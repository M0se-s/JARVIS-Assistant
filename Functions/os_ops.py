import os
import subprocess as sp


def get_discord_path():
    # Grab the dynamic AppData path
    local_app_data = os.environ.get("LOCALAPPDATA")

    # SAFETY CHECK: Shuts up the "join" error
    if not local_app_data:
        return None

    discord_dir = os.path.join(local_app_data, "Discord")

    # If Discord isn't installed on this PC, bail out safely
    if not os.path.exists(discord_dir):
        return None

    # Scan the Discord folder for the current version update
    for folder in os.listdir(discord_dir):
        if folder.startswith("app-"):
            return os.path.join(discord_dir, folder, "Discord.exe")

    return None


# The dictionary
paths = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "discord": get_discord_path(),
    "cmd": "cmd.exe"
}


def open_app(app_name):
    # 1. Grab the path from the dictionary
    app_path = paths.get(app_name)

    # 2. Safety check to ensure a valid path has been found
    if not app_path:
        print(f"Error: Could not find path for {app_name}")
        return False

    # 3. Launching the app
    try:
        sp.Popen(app_path)
        return True
    except Exception as e:
        print(f"Crash log: Failed to open {app_name}. Error {e}")
        return False
    
def open_camera():
    try:
        sp.run("start microsoft.windows.camera:", shell = True)
        return True
    
    except Exception as e:
        print(f'Crash Log: Failed to open camera. Error {e}')
        return False
