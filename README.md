# NetworkUtilityTool
A network utility tool implemented in Python that will enable users to perform various networking tasks, including DNS queries, HTTP requests, FTP transfers, and network tracing

1) Firstly, in order to check that everything work, you can manually test the files in the VsCode or in any other tool you use. 
   
   You can do it by running dns_tool.py and network_trace.py files.
   
   Comments are written near, beneath, or above the code lines so that it is easier to understand what is going on and why 
   
   variables are needed for.

2) Regarding the network_utility.py file:
   
   I built a 500x500 window, so that it is not very big and not very small at the same time.
   
   After running the file, the window will pop up. The title is "Network Utility Tool"

   There will be 4 different sections, namely: DNS Commands, Requests, Socket Programming, and Tracing 

   Now lets see how each of them work:

   1. DNS Commands:
        First thing you will probably notice are 3 buttons, and an Entry space. In the Entry space you can type domain name, such as "google.com". After entering your domain, you can either press 'nslookup', 'dig', or 'host' buttons, so the appropriate command executes. After couple of seconds in the window below you will see the resulting output.

   2. Requests:
        The Requests sections allows you to either choose GET request or FTP option. In the entry space above you can type a url address, such as "https://google.com", and press a "GET Request" button. After that you will see the result in the window below.
        Additionally, there are also 4 more entry sections of Host, Port, Password, and Username. There you can type the appropriate information in order to check it. After which you can press the "FTP Request" button. If the authorization will not go as planned, the exception will appear in the window.

   3. Socket Programming:
        This section is pretty simple. All you need is to type whatever message you want to send and provide a port of your choice (I personally always typed 8080). After providing inputs, you can either press "TCP type" or "UDP type" to check both options. The corresponding output will be given in the window below.

   4. Tracing:
        The first thing to mention is that you need to turn of Nazarbayev University Wi-Fi, and establish your personal connection (4G for ex). All you need is to type the IP address and choose any button to check both tracing methods. The corresponding result will be provided in the window below. (WARNING: most likely you will need to wait some minutes, because it takes pretty long time to execute these commands)

That is all for this README file. Hope you understood everything. As was mentioned before, you can check the code manually by executing it in the terminal / VsCode. 

