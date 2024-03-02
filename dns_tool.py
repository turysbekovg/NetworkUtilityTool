import subprocess
import requests
from ftplib import FTP
import socket
import threading


server_ip = '127.0.0.1' 

def nslookupCommand(domain_name): # lookup command 
    try:
        result = subprocess.check_output(['nslookup', domain_name], text=True)
        return result

    except FileNotFoundError as lookup_exception: # if an exception occurs
        return f"Oops, error happened when executing nslookup command: {lookup_exception}"


def hostCommand(domain_name):  # host command 
    try:
        result = subprocess.check_output(['host', domain_name], text=True)
        return result
    
    except FileNotFoundError as host_exception: # if an exception occurs
        return f"Oops, error happened when executing host command: {host_exception}"


def digCommand(domain_name):  # dig command 
    try:
        result = subprocess.check_output(['dig', domain_name], text=True)
        return result
    
    except FileNotFoundError as dig_exception: # if an exception occurs
        return f"Oops, error happened when executing host command: {dig_exception}"

# ------------------------------------------------------------- #

def http_get_request(url_address):   # get request command
    try:
        # getting the URL address
        given_response = requests.get(url_address)
        print("Connection is successfully established. The HTTP Status Code:", given_response.status_code)
        print("Below is the response text:")
        print(given_response.text)
        return f"Connection is successfully established. Below is the response text:{given_response.text}"

    except requests.RequestException as http_get_request_exception: # if and exception occurs
        return f"Oops, error happened when executing GET request command: {http_get_request_exception}"
    


def ftp_transfer_request(server_name, port_name, username, password): # ftp transfer command
    try:
        temp_ftp = FTP()
        temp_ftp.connect(server_name, port_name) # connecting
        output = temp_ftp.login(username, password)   # logging with pass and username
        temp_ftp.quit() # quitting

        if output.startswith("230"): # in case of a successfull connection
            return f"Successfully connected to {server_name} with username: {username} and pass: {password}"
        else:
            return "Authorization is declined." # or decline

    except Exception as transfer_request_exception: # if and exception occurs
        return f"Oops, error happened when executing FTP transfer command: {transfer_request_exception}"

    # finally:
    #     temp_ftp.quit() # quitting


# ------------------------------------------------------------- #
        
# If user chooses Socket Programming

def handle_server_connection (user_socket_type, socket_port_number): 
    # this function is needed to create a server, then to accept a message from a user and then send it back

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM if user_socket_type == 'tcp' else socket.SOCK_DGRAM)
    server_socket.bind((server_ip, socket_port_number))

    if user_socket_type == 'udp': # if the provided type is UDP
        # firstly, we start a server then accepting a user connection
        user_data, user_address = server_socket.recvfrom(1024)
        user_message = user_data.decode('utf-8')
        # then we printing the following messages
        print("The chosen socket type: UDP. Listening on port number:", socket_port_number)
        print("The server received a user message", user_message, "from IP", user_address[0], "and Port", user_address[1])
        response_from_server = f"The server has obtained a message from a user with the following message: {user_message}"
        # then we send the server response to user
        server_socket.sendto(response_from_server.encode('utf-8'), user_address)

    elif user_socket_type == 'tcp': # if the provided type is TCP
        # the same precodure here
        server_socket.listen(10)
        user_data, user_address = server_socket.accept()
        user_message = user_data.recv(1024).decode('utf-8')
        # printing
        print("The chosen socket type: TCP. Listening on port number:", socket_port_number)
        print("The server received a user message", user_message, "from IP", user_address[0], "and Port", user_address[1])
        # sending response
        response_from_server = f"The server has obtained a message from a user with the following message: {user_message}"
        user_data.send(response_from_server.encode('utf-8'))
        user_data.close()
    
    # closing server socket
    server_socket.close()



def handle_client_connection (user_socket_type, socket_port_number, user_message): 
    # this function is needed to create a user and send a messsage based on an input the user has provided

    user_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM if user_socket_type == 'tcp' else socket.SOCK_DGRAM)
    user_socket.connect((server_ip, socket_port_number))

    if user_socket_type == 'udp': # if the provided type is UDP
        # printing a successfull connection
        print ("A user connection is successfully established")
        # sending message
        user_socket.sendto(user_message.encode('utf-8'), (server_ip, socket_port_number))
        # getting server response
        socket_response, _ = user_socket.recvfrom(1024)
        print("The user received a message:", socket_response.decode('utf-8'), "\n")

    elif user_socket_type == 'tcp': # if the provided type is TCP
        # the same here
        print ("A user connection is successfully established")
        user_socket.send(user_message.encode('utf-8'))
        socket_response = user_socket.recv(1024).decode('utf-8')
        print ("The user received a message:", socket_response, "\n")

    # closing user socket
    user_socket.close()


def gui_sockets (user_message, user_port, socket_type): # this function is needed to interact with GUI 

    thread_serv = threading.Thread (target=handle_server_connection, args=(socket_type, user_port)) # server thread
    thread_user = threading.Thread (target=handle_client_connection, args=(socket_type, user_port, user_message)) # user thread
 
    thread_serv.start() # start 
    thread_user.start() # start

# ------------------------------------------------------------- #

def main():  

    print("Hello! Firstly, you are going to choose the command type below.")  
    
    # Showing the list of the available operation types

    print("\nHere are available operation types:")
    print("1) DNS-related Commands")
    print("2) HTTP GET Request")
    print("3) FTP File Transfer")
    print("4) Socket Programming")

    # asking for the required operation type from a user

    user_choice = input("Enter the operation you want to proceed (1 | 2 | 3 | 4): ")

    # --------------------------- #

    # if the user chooses 1

    if user_choice == '1': # DNS Commands

        # providing a lsit of available operations

        print("\nPlease, choose a DNS command:")
        print("1) nslookup command")
        print("2) host command")
        print("3) dig command")

        # asking for the operation choice

        dns_command_choice = input("Enter the command number (1 | 2 | 3): ")

        domain_name = input("Now, provide the domain name, please: ")   # asking for the domain name

        commandType = None 

    
        if dns_command_choice == '1': # if the user chooses 1 then we execute the nslookup
            commandType = nslookupCommand(domain_name) # procedding to the function

        elif dns_command_choice == '2': # if the user chooses 2 then we execute the host
            commandType = hostCommand(domain_name) # procedding to the function

        elif dns_command_choice == '3': # if the user chooses 3 then we execute the dig
            commandType = digCommand(domain_name) # procedding to the function

        else:  # if the user provides incorrect number or character
            raise ValueError("You provided incorrect number. Please, try again and enter a correct number.")
        
        print("\nResults:") # results
        print(commandType)

    # --------------------------- #

    # if the user chooses 2

    elif user_choice == '2': # GET Request
        url_address = input("\nPlease, provide the URL for the HTTP GET request: ") # asking for the URL 
        response = http_get_request(url_address) # procedding to the function
        print(response)

    # --------------------------- #

    # if the user chooses 3

    elif user_choice == '3': # File transfer
        server_name = input("\nPlease, provide the FTP server address (host): ")  # Asking for the adress name
        port_name = int(input("Now give the FTP server port: ")) # asking for the port name
        username = input("Please, provide the username: ") # username input
        password = input("Now, give some sample password: ") # password input
        response = ftp_transfer_request(server_name, port_name, username, password) # procedding to the function
        print(response)
    # --------------------------- #
        
    elif user_choice == '4': # Socket programming
        print ("\nThere are two types of socket:") # showing the list of available types
        print ("1) TCP")
        print ("2) UDP")

        user_message = input("\nFIRSTLY, provide the MESSAGE you want to send to the server: ") # asking for a message
        socket_port_number = int(input("Next, please, enter the port 8080: ")) # asking for a port number (8080)

        user_socket_type = input("Now, choose the option you want (1 | 2): ") # asking for a preferred option
        print()

        if user_socket_type == '1': # if user chooses TCP
            thread_serv = threading.Thread (target=handle_server_connection, args=('tcp', socket_port_number)) # server thread
            thread_user = threading.Thread (target=handle_client_connection, args=('tcp', socket_port_number, user_message)) # user thread

        elif user_socket_type == '2': # if user chooses UDP
            thread_serv = threading.Thread (target=handle_server_connection, args=('udp', socket_port_number)) # server thread
            thread_user = threading.Thread (target=handle_client_connection, args=('udp', socket_port_number, user_message)) # user thread
        
        else: # if a user provides incorrect option
            raise ValueError ("Oops, You provided incorrect number. Please, try again and give a correct number.")
        
        thread_serv.start() # starting threads
        thread_user.start()

     
    # if incorrect number is provided
    else:
        raise ValueError ("Sorry! You provided incorrect operation number. Please, try again and provide a correct operation number.")


if __name__ == "__main__":
    main()