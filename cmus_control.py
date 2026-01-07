#!/usr/bin/env python3
import sys
import subprocess
import os

# Konfiguration der Icons
ICON_PREV  = "\uf048"  #  (fa-step-backward)
ICON_NEXT  = "\uf051"  #  (fa-step-forward)
ICON_PLAY  = "\uf04b"  #  (fa-play)
ICON_PAUSE = "\uf04c"  #  (fa-pause)
ICON_STOP  = "\uf04d"  #  (fa-stop)

def get_cmus_status():
    """Prüft, ob cmus läuft und gibt den Status zurück."""
    try:
        output = subprocess.check_output(["cmus-remote", "-Q"], stderr=subprocess.DEVNULL)
        output = output.decode("utf-8")
        
        if "status playing" in output:
            return "playing"
        elif "status paused" in output:
            return "paused"
        elif "status stopped" in output:
            return "stopped"
        return "unknown"
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "not_running"

def run_cmus_command(cmd_arg):
    """Führt cmus-remote Befehle aus."""
    cmd_map = {
        "next": ["-n"],
        "prev": ["-r"],
        "toggle": ["-u"],
        "stop": ["-s"]
    }
    
    if cmd_arg in cmd_map:
        try:
            subprocess.run(["cmus-remote"] + cmd_map[cmd_arg], check=False)
        except Exception:
            pass

def main():
    button_type = sys.argv[1] if len(sys.argv) > 1 else "status"

    # --- WICHTIGE ÄNDERUNG ---
    # Wir lesen BLOCK_BUTTON aus. Wenn das Skript durch das Intervall aufgerufen wird,
    # ist diese Variable meist leer ("") oder gar nicht gesetzt.
    # Wir führen den Befehl NUR aus, wenn es explizit "1" (Links), "2" (Mitte) oder "3" (Rechts) ist.
    block_button = os.environ.get("BLOCK_BUTTON", "")
    
    # Prüfen, ob es wirklich ein Mausklick war (Button 1-3 sind üblich)
    if block_button in ["1", "2", "3"]:
        if button_type in ["next", "prev", "toggle"]:
            run_cmus_command(button_type)

    # --- STATUS AUSGABE ---
    # Dieser Teil läuft IMMER, um das richtige Icon anzuzeigen
    status = get_cmus_status()
    
    if button_type == "prev":
        print(ICON_PREV)
    elif button_type == "next":
        print(ICON_NEXT)
    elif button_type == "toggle":
        if status == "playing":
            print(ICON_PAUSE)
        else:
            print(ICON_PLAY)

if __name__ == "__main__":
    main()

