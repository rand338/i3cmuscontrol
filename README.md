# i3blocks-cmus-controls

Lightweight Python blocklets for i3blocks to control **cmus** via three clickable buttons in your i3bar (Previous, Play/Pause Toggle, Next) – including a dynamic play/pause icon. [conversation_history:1]

## Features

- Three separate i3blocks modules: `prev`, `toggle`, `next`.
- Play/Pause button dynamically updates its icon based on the current cmus status.
- Actions are only triggered on actual clicks (prevents accidental toggling during interval updates).
- Uses Font Awesome (Unicode) icons instead of standard ASCII/Emoji.

## Requirements

- `python3` (Script).
- `cmus` incl. `cmus-remote` (Control/Status check).
- `i3` + `i3blocks` (Status bar/Click handling).
- Font Awesome or Nerd Font for icon rendering (e.g., "Font Awesome" must be included in your i3bar font list).

## Installation

1. Save the script and make it executable:
   ```bash
   mkdir -p ~/.config/i3blocks/scripts
   nano ~/.config/i3blocks/scripts/cmus_control.py
   chmod +x ~/.config/i3blocks/scripts/cmus_control.py

# Add the following to your i3blocks configuration (~/.config/i3blocks/config):
[cmus-prev]
command=python3 ~/.config/i3blocks/scripts/cmus_control.py prev
interval=0

[cmus-toggle]
command=python3 ~/.config/i3blocks/scripts/cmus_control.py toggle
interval=5

[cmus-next]
command=python3 ~/.config/i3blocks/scripts/cmus_control.py next
interval=0

Ensure the font is defined in ~/.config/i3/config (Example):

- Reload or restart i3 (e.g., Mod+Shift+R).

# Usage & Notes

- Left-clicking the respective icons triggers prev, toggle, or next.
- If icons appear as "tofu" boxes (□), you are missing the required font or it is not configured in your i3bar.
- Optionally, you can increase the toggle interval if you rarely control playback outside of i3blocks (e.g., interval=10).
