# Import the MelodyCraftServer class
from melodycraftWS.server.melody_craft_server import MelodyCraftServer

# Create an instance of the server
server = MelodyCraftServer()

if __name__ == '__main__':
    # Run the server with debug mode enabled (debug=True)
    server.run(debug=True)