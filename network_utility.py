import tkinter as tk
from tkinter import ttk
import dns_tool
import network_trace
import sys

class NetworkUtilityTool:
    def __init__(self) -> None:

        self.root = tk.Tk() # window
        self.root.title("Network Utility Tool") # giving title
        self.root.geometry("500x500") # setting size

        self.notebook = ttk.Notebook(self.root) # creating Notebook

        self.frame_dns_commands = ttk.Frame(self.notebook) # naming each and adding them to a window
        self.notebook.add(self.frame_dns_commands, text="DNS Commands") # then adding each to the notebook bar

        self.frame_requests = ttk.Frame(self.notebook) # requests
        self.notebook.add(self.frame_requests, text="Requests")

        self.frame_socket_programming = ttk.Frame(self.notebook) # socket programming
        self.notebook.add(self.frame_socket_programming, text="Socket Programming")

        self.frame_tracing = ttk.Frame(self.notebook) # tracing
        self.notebook.add(self.frame_tracing, text="Tracing")

        self.notebook.pack() 

        # DNS Commands

        self.dns_commands_asking_label = ttk.Label (self.frame_dns_commands, text="Provide the domain, please:") # text 
        self.dns_commands_asking_label.pack (pady=5)
        
        self.dns_commands_input = ttk.Entry (self.frame_dns_commands) # where the input goes
        self.dns_commands_input.pack (pady=5)

        # lookup button
        self.lookup_button = ttk.Button (self.frame_dns_commands, text="nslookup", command=self.dns_activate_nslookup)
        self.lookup_button.pack (padx=8, pady=3)

        # host button
        self.host_button = ttk.Button (self.frame_dns_commands, text="host", command=self.dns_activate_host) 
        self.host_button.pack (padx=8, pady=3)
        
        # dig button
        self.dig_button = ttk.Button (self.frame_dns_commands, text="dig", command=self.dns_activate_dig) 
        self.dig_button.pack (padx=8, pady=3)

        # output field
        self.commands_output = tk.Text(self.frame_dns_commands, height=20, width=60)
        self.commands_output.pack(pady=(5,15), padx=5)

########################


        # REQUESTS

        # text of GET
        self.requests_asking_label = ttk.Label (self.frame_requests, text="Provide a URL address if you want to proceed a GET request, please.")
        self.requests_asking_label.pack (pady=5)
        
        # input of GET req
        self.get_requests_input = ttk.Entry (self.frame_requests) # where the input goes
        self.get_requests_input.pack (pady=3)

        # text of FTP
        self.requests_asking_label2 =  ttk.Label(self.frame_requests, text="HOWEVER, if you want to process to FTP transfer, provide host, port, username, and password.")
        self.requests_asking_label2.pack (pady=5)

        # --------------------------------------- #

        self.frame_ftp_asking_commands = ttk.Frame(self.frame_requests) # creating a frame to put there labels
        
        # creating labels 
        self.requests_host_asking_label =  ttk.Label(self.frame_ftp_asking_commands, text="HOST")
        self.requests_port_asking_label = ttk.Label(self.frame_ftp_asking_commands, text="PORT")
        self.requests_username_asking_label =  ttk.Label(self.frame_ftp_asking_commands, text="Username")
        self.requests_password_asking_label = ttk.Label(self.frame_ftp_asking_commands, text="Password")

        # packing them
        self.requests_host_asking_label.pack (side=tk.LEFT, padx=30)
        self.requests_port_asking_label.pack (side=tk.LEFT, padx=30)
        self.requests_username_asking_label.pack (side=tk.LEFT, padx=30)
        self.requests_password_asking_label.pack (side=tk.LEFT, padx=30)

        # packing the frame
        self.frame_ftp_asking_commands.pack(pady=5)

        # ------------------------------------------- #

        self.frame_ftp_input_commands = ttk.Frame(self.frame_requests) # creating a frame to put there input spaces

        # creating inputs for HOST PORT USERNAME and PASSWORD
        self.host_input = ttk.Entry (self.frame_ftp_input_commands)
        self.port_input = ttk.Entry(self.frame_ftp_input_commands)
        self.username_input = ttk.Entry(self.frame_ftp_input_commands)
        self.password_input = ttk.Entry(self.frame_ftp_input_commands)

        # packing them
        self.host_input.pack (side=tk.LEFT, padx=3)
        self.port_input.pack (side=tk.LEFT, padx=3)
        self.username_input.pack (side=tk.LEFT, padx=3)
        self.password_input.pack (side=tk.LEFT, padx=3)

        # packing the input frame
        self.frame_ftp_input_commands.pack()

        # -------------------------------------------- #

        # creating buttons of GET and FTP and packing
        self.get_request_button = ttk.Button (self.frame_requests, text="GET Request", command=self.requests_activate_get) # command here
        self.get_request_button.pack (pady=10)

        self.file_transfer_button = ttk.Button (self.frame_requests, text="FTP Request", command=self.requests_activate_ftp) # command here
        self.file_transfer_button.pack (pady=10)

        # output field
        self.requests_output = tk.Text(self.frame_requests, height=20, width=60)
        self.requests_output.pack(pady=(5,15), padx=5)


##########################
        

        # TRACING

        # text
        self.tracing_asking_label = ttk.Label (self.frame_tracing, text="Provide an IP adress or a domain name, please.")
        self.tracing_asking_label.pack(pady=5)

        # input ask and pack
        self.tracing_input = ttk.Entry (self.frame_tracing) # where the input goes
        self.tracing_input.pack (pady=3)

        # traceroute button
        self.traceroute_button = ttk.Button (self.frame_tracing, text="Traceroute", command=self.tracing_activate_traceroute) # command here
        self.traceroute_button.pack (padx=8, pady=4)

        # tracepath button
        self.tracepath_button = ttk.Button (self.frame_tracing, text="Tracepath", command=self.tracing_activate_tracepath) # command here
        self.tracepath_button.pack (padx=8, pady=4)

        # output field
        self.tracing_output = tk.Text(self.frame_tracing, height=20, width=60)
        self.tracing_output.pack(pady=(5,15), padx=5)


#########################


        # SOCKET PROGRAMMING

        # text
        self.socket_asking_label = ttk.Label (self.frame_socket_programming, text="Provide a message you want to send, please.")
        self.socket_asking_label.pack(pady=5)

        # MESSAGE input
        self.socket_message_input = ttk.Entry (self.frame_socket_programming) # where the input goes
        self.socket_message_input.pack (pady=3)

        # another text
        self.socket_asking_label2 = ttk.Label (self.frame_socket_programming, text="Provide a port, please.")
        self.socket_asking_label2.pack(pady=5)

        # PORT input
        self.socket_port_input = ttk.Entry (self.frame_socket_programming) # where the input goes
        self.socket_port_input.pack (pady=3)

        # TCP button
        self.tcp_button = ttk.Button (self.frame_socket_programming, text="TCP type", command=self.socket_activate_tcp) # command here
        self.tcp_button.pack (padx=8, pady=4)

        # UDP button
        self.udp_button = ttk.Button (self.frame_socket_programming, text="UDP type", command=self.socket_activate_udp) # command here
        self.udp_button.pack (padx=8, pady=4)

        # output button
        self.socket_programming_output = tk.Text(self.frame_socket_programming, height=20, width=60)
        self.socket_programming_output.pack(pady=(5,15), padx=5)



###### 

    # activating functions of DNS commands 

    def dns_activate_nslookup (self):
        domain_name = self.dns_commands_input.get()
        output_text = dns_tool.nslookupCommand(domain_name)
        self.commands_output.insert(tk.END, output_text + "\n")

    def dns_activate_host (self):
        domain_name = self.dns_commands_input.get()
        output_text = dns_tool.hostCommand(domain_name)
        self.commands_output.insert(tk.END, output_text + "\n")

    def dns_activate_dig (self):
        domain_name = self.dns_commands_input.get()
        output_text = dns_tool.digCommand(domain_name)
        self.commands_output.insert(tk.END, output_text + "\n")

#######
        
    # activating functions of GET and FTP 

    def requests_activate_get (self):
        url_address = self.get_requests_input.get()
        output_text = dns_tool.http_get_request(url_address)
        self.requests_output.insert(tk.END, output_text + "\n")

    def requests_activate_ftp (self):
        host_name = self.host_input.get()
        port_name = int(self.port_input.get())
        username = self.username_input.get()
        password = self.password_input.get()
        output_text = dns_tool.ftp_transfer_request(host_name, port_name, username, password)
        self.requests_output.insert(tk.END, output_text + "\n")


######
        
    # activation commands of TCP and UDP

    def socket_activate_tcp (self):
        sys.stdout = ChangeDestination(self.socket_programming_output)
        user_message = self.socket_message_input.get()
        user_port_input = int(self.socket_port_input.get())
        dns_tool.gui_sockets(user_message, user_port_input, 'tcp')

    def socket_activate_udp (self):
        sys.stdout = ChangeDestination(self.socket_programming_output)
        user_message = self.socket_message_input.get()
        user_port_input = int(self.socket_port_input.get())
        dns_tool.gui_sockets(user_message, user_port_input, 'udp')


######

      # activation commands for Tracing  

    def tracing_activate_traceroute (self):
        user_input = self.tracing_input.get()
        output_text = network_trace.traceroute_method(user_input)
        self.tracing_output.insert(tk.END, output_text + "\n")

    def tracing_activate_tracepath (self):
        user_input = self.tracing_input.get()
        output_text = network_trace.tracepath_method(user_input)
        self.tracing_output.insert(tk.END, output_text + "\n")


def main():
    app = NetworkUtilityTool()
    run(app)

def run(app):
    app.root.mainloop()

# this helps me to change the destination of output that is in the console to the output field of socket programming
class ChangeDestination:  
    def __init__(self, socket_programming_output):
        self.socket_programming_output = socket_programming_output

    def write(self, temp):
        self.socket_programming_output.insert(tk.END, temp)
        self.socket_programming_output.see(tk.END)

    def flush(self):
        pass
    

if __name__ == "__main__":
    main()
