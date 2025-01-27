# Vibration Mod for The Sims 4

## Overview
The **Vibration Mod** is a custom extension for **The Sims 4**, designed to enhance gameplay by adding vibration feedback during WooHoo events. It communicates with an external server using a socket connection to send commands for starting and stopping vibration. The mod also integrates with the popular **WickedWhims** mod to provide additional functionality.

---

## Features
- **WickedWhims Detection**: Automatically checks if the **WickedWhims** mod is installed to enable additional interactions.
- **Vibration Activation**: Sends a command to activate vibration when a WooHoo event starts.
- **Vibration Deactivation**: Sends a command to stop vibration when the WooHoo event ends.
- **Custom Console Commands**:
  - `vibrationmod`: A command to test vibration activation and deactivation.
  - `checkwickedwhims`: A command to check if the **WickedWhims** mod is installed and display its attributes.

---

## Prerequisites
- **The Sims 4** with the modding framework enabled.
- **WickedWhims Mod** (optional, but recommended).
- A socket server listening on the specified `HOST` and `PORT`.
- Python 3.x environment to customize or extend the mod.

---

## Installation
1. **Download the Mod**: Clone or download the project files to your computer.
2. **Set Up the Server**: 
   - Ensure a socket server is running on `HOST` (default: `127.0.0.1`) and `PORT` (default: `65432`).
   - The server should handle commands `start_vibration` and `stop_vibration`.
3. **Add to Mods Folder**:
   - Place the Python script in the **Mods** folder of your **The Sims 4** directory.
   - Enable script mods in the game settings.

---

## Usage
1. **Activate the Mod**:
   - Launch **The Sims 4** and ensure the mod is loaded successfully.
   - Open the in-game cheat console (`Ctrl + Shift + C`).
   - Use the following commands:
     - `vibrationmod`: Test the vibration functionality.
     - `checkwickedwhims`: Check if the **WickedWhims** mod is installed.

2. **WooHoo Integration**:
   - If **WickedWhims** is installed, the mod will automatically start and stop vibration during WooHoo events.

---

## Configuration
To modify the connection settings:
1. Open the script file.
2. Update the `HOST` and `PORT` variables to match your server configuration.

Example:
```python
HOST = '192.168.1.100'  # Replace with your server's IP address
PORT = 12345            # Replace with your server's port
```

---

## Troubleshooting
- **Mod Not Working**:
  - Ensure that script mods are enabled in **The Sims 4** settings.
  - Check if the socket server is running and reachable at the specified `HOST` and `PORT`.
  
- **WickedWhims Not Detected**:
  - Verify that the **WickedWhims** mod is installed and active in the game.

- **Socket Connection Error**:
  - Confirm that the server is running and configured to handle `start_vibration` and `stop_vibration` commands.

---

## Contributing
Feel free to fork this project and submit pull requests for improvements or new features.

---

## Disclaimer
This mod is a fan-made project and is not affiliated with or endorsed by EA, Maxis, or the creators of the **WickedWhims** mod. Use at your own risk.

--- 

Enjoy the enhanced gameplay! 😊