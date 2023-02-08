# Portscanner.py
A simple Port Scanner

So I've been working on creating this simple Python port scanner as a small project. It allows you to scan a target's open ports. It uses the socket library to initiate a connection to each port in the range specified, and prints the result of the connection attempt (open or closed) to the console. The scan function takes a target (IP address or hostname) and the number of ports to scan as input and calls the scan_port function for each port in the specified range. 
The scan_port function uses a try-except block to attempt a connection to the specified port on the target, and prints a message indicating whether the port is open or closed based on the result of the connection attempt.
When I test it against my Metasploitable machine it responded great!
But my goal was or is for the output to show in two columns, which it does, but I'm still trying to learn how I can bring the open ports on the second column to start on top as a separate list. 
Work still in progress...
