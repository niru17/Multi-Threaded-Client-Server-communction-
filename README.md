# Multi-Threaded-Client-Server-communction-
The client code establishes a connection with the server and sends commands to perform operations such as PUT, GET, and DUMP. It prompts the user to input one of these commands and sends it to the server. The client then receives the response from the server and displays it to the user. The client continues to prompt the user until the user enters 'q' to quit the connection.

The server code listens for incoming connections from clients on a specified port. Once a client connects, the server spawns a new thread to handle communication with that client. It processes commands received from the client, such as PUT, GET, and DUMP, and responds accordingly. The server maintains a cache to store key-value pairs and a proxy to forward requests to another server if necessary.

How to Run the application
1. Start Server: Execute the server code to start the server. The server will listen for incoming connections from clients.
2. Run Client: Execute the client code to establish a connection with the server. The client will prompt the user to input commands such as PUT, GET, and DUMP.
3. Follow the prompts to interact with the server.
4. Interact with Server: Enter commands on the client-side to perform operations on the server-side. The server will respond accordingly based on the received commands.
5. Quit Connection: To quit the connection, enter 'q' when prompted by the client. This will close the connection with the server and terminate the client program.
