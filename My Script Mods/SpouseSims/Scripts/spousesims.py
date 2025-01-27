import sims4.commands
from sims4.commands import CheatOutput
import socket

# Socket settings for connecting to the server
HOST = '127.0.0.1'  # Local host
PORT = 65432        # Port for socket connection

# Function to check if the WickedWhims mod is installed
def is_wickedwhims_installed():
    try:
        import wickedwhims
        return dir(wickedwhims)
    except ImportError:
        return False

# Function to activate vibration
def start_vibration():
    try:
        # Sending a command via socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))  # Connect to the server
            s.sendall(b"start_vibration")  # Send the command to the server
            s.close()
        print("Vibration activated.")
    except Exception as e:
        print(f"Error connecting to the socket server: {e}")

# Function to stop vibration
def stop_vibration():
    try:
        # Sending a command via socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))  # Connect to the server
            s.sendall(b"stop_vibration")  # Send the command to the server
            s.close()
        print("Vibration stopped.")
    except Exception as e:
        print(f"Error connecting to the socket server: {e}")

# Handler for the start of WooHoo
def on_woohoo_started():
    if is_wickedwhims_installed():
        start_vibration()

# Handler for the end of WooHoo
def on_woohoo_ended():
    stop_vibration()

# Main game command
@sims4.commands.Command('vibrationmod', command_type=sims4.commands.CommandType.Live)
def vibrationmod(_connection=None):
    output = CheatOutput(_connection)
    output("Starting the vibration mod for WooHoo.")

    # Test command to send to the socket
    start_vibration()  # Send the command to start vibration
    output("Command to start vibration sent to the server.")

    # Stop vibration for testing
    stop_vibration()  # Send the command to stop vibration
    output("Command to stop vibration sent to the server.")

# Handler for tracking WooHoo events
def handle_woohoo_event(event):
    if event == "start":
        on_woohoo_started()
    elif event == "end":
        on_woohoo_ended()

# Register the WooHoo event (event usage)
def register_woohoo_event():
    start_vibration()
    pass

# Command to check if the WickedWhims mod is installed
@sims4.commands.Command('checkwickedwhims', command_type=sims4.commands.CommandType.Live)
def checkwickedwhims(_connection=None):
    output = CheatOutput(_connection)
    iswwi = is_wickedwhims_installed()
    if iswwi is not False:
        output("The WickedWhims mod is installed.")
        output(" ".join(iswwi))
    else:
        output("The WickedWhims mod is not installed.")
