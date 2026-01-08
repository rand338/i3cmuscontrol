#!/usr/bin/env python3
import sys
import subprocess
import os


# --- CONFIGURATION ---
# Icons (Font Awesome)
ICON_PREV    = "\uf048"  # 
ICON_NEXT    = "\uf051"  # 
ICON_PLAY    = "\uf04b"  # 
ICON_PAUSE   = "\uf04c"  # 
ICON_SHUFFLE = "\uf074"  #  (fa-random / fa-shuffle)


# Colors (Optional)
COLOR_ACTIVE = "#00FF00" # Green when shuffle is on
COLOR_DEFAULT = ""       # Use default bar color


def get_cmus_info():
    """Reads status and settings from cmus."""
    info = {
        "status": "stopped",
        "shuffle": False
    }
    try:
        output = subprocess.check_output(["cmus-remote", "-Q"], stderr=subprocess.DEVNULL)
        output = output.decode("utf-8")
        
        # Parse status
        if "status playing" in output:
            info["status"] = "playing"
        elif "status paused" in output:
            info["status"] = "paused"
            
        # Parse shuffle (can be 'true', 'tracks', or 'albums')
        if "set shuffle true" in output or "set shuffle tracks" in output or "set shuffle albums" in output:
            info["shuffle"] = True
            
    except (subprocess.CalledProcessError, FileNotFoundError):
        info["status"] = "not_running"
        
    return info


def run_cmus_command(cmd_arg):
    cmd_map = {
        "next":    ["-n"],
        "prev":    ["-r"],
        "toggle":  ["-u"],
        "shuffle": ["-S"], # Toggle shuffle
        "stop":    ["-s"]
    }
    
    if cmd_arg in cmd_map:
        try:
            subprocess.run(["cmus-remote"] + cmd_map[cmd_arg], check=False)
        except Exception:
            pass


def main():
    button_type = sys.argv[1] if len(sys.argv) > 1 else "status"
    block_button = os.environ.get("BLOCK_BUTTON", "")


    # Execute command on click
    if block_button in ["1", "2", "3"]:
        if button_type in ["next", "prev", "toggle", "shuffle"]:
            run_cmus_command(button_type)


    # Get status
    info = get_cmus_info()
    
    # Generate output
    if button_type == "prev":
        print(ICON_PREV)
        
    elif button_type == "next":
        print(ICON_NEXT)
        
    elif button_type == "toggle":
        if info["status"] == "playing":
            print(ICON_PAUSE)
        else:
            print(ICON_PLAY)
            
    elif button_type == "shuffle":
        print(ICON_SHUFFLE)     # Line 1: Full Text
        print(ICON_SHUFFLE)     # Line 2: Short Text
        # Line 3: Color (Only print if active)
        if info["shuffle"]:
            print(COLOR_ACTIVE)


if __name__ == "__main__":
    main()
