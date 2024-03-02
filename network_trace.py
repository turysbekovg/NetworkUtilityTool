import subprocess

def traceroute_method(user_input): # traceroute function
    try:
        trace_type = "traceroute"
        result = subprocess.check_output([trace_type, user_input], text=True)
        return result # returning result
    except subprocess.CalledProcessError as traceroute_method_exception: #if exception occurs 
        return f"Oops, error happened when executing traceroute: {traceroute_method_exception}"

def tracepath_method(user_input): # tracepath function
    try:
        trace_type = "tracepath"
        result = subprocess.check_output([trace_type, user_input], text=True)
        return result
    except subprocess.CalledProcessError as tracepath_method_exception: #if exception occurs
        return f"Oops, error happened when executing tracepath: {tracepath_method_exception}"

def main():
    user_input = input("Hello! Please, give the IP address or domain name for tracing: ") # asking for the IP or domain name

    print("\nThere are 2 types of tracing:") # list of options
    print("1) Tracepath")
    print("2) Traceroute")

    # asking for the preferred option
    method_choice = input("Now, choose a tracing method that you want (1 | 2): ")

    if method_choice == '1': #proceeding to tracepath if #1
        result = tracepath_method(user_input)
        print (result)
    elif method_choice == '2': #proceeding to tracerout if #2
        result = traceroute_method(user_input)
        print (result)
    else: # incorrect input
        print("Sorry! The number you provided is incorrect. Please try again and enter a correct number.")


if __name__ == "__main__":
    main()