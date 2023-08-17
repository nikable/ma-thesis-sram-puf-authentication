import socket
import os
import time
import errno

def client_program():
    # host = "192.168.178.40"  # when considering static ip
    host = "rp-labs1.local"  # assign hostname
    port = 18000  # socket server port number

    client_socket = socket.socket()  # instantiate client socket
    client_socket.connect((host, port))  # connect to the server
    print(f"[+] Connected to {host}:{port}")
    
    SEPARATOR = "<SEPARATOR>" # to seperate the metadata
    BUFFER_SIZE = 4096  # buffer size for data transmission
    
    ## file related data

    ## outliers
    #filename = "board001Bcycle0058_rgb.png"
    #filename = "board003Acycle0050_rgb.png"
    
    #filename = "board0017cycle0080_rgb.png"
    
    ## example boards from which model is trained on colab
    #filename = "board002Acycle0064_rgb.png"
    #filename = "board003Dcycle0055_rgb.png"
    #filename = "board000Bcycle0007_rgb.png"


    ## local boards
    
    #filename = "board002Acycle0064_rgb.png"
    #filename = "board002Acycle0017_rgb.png"
    #filename = "board002Acycle0087_rgb.png"
    
    #filename = "board0035cycle0002_rgb.png"
    #filename = "board0035cycle0095_rgb.png"
    #filename = "board0035cycle0065_rgb.png"


    #filename = "board0088cycle0005_rgb.png"
    #filename = "board0088cycle0049_rgb.png"

    #filename = "board0088cycle0036_rgb.png"
    #filename = "board0088cycle0005_rgb.png"
    #filename = "board0088cycle0049_rgb.png"
    #filename = "board0088cycle0063_rgb.png"


    


    filesize = os.path.getsize(filename) # get the file size
    
    ## trained on google-colab
    ## for board 002A
    #client_socket.send("Authentication request from board002A".encode("utf-8"))
    
    ## for board 003D
    #client_socket.send("Authentication request from board003D".encode("utf-8"))

    ## for board 000B
    #client_socket.send("Authentication request from board000B".encode("utf-8"))

    ## local
    ## for board 002A
    #client_socket.send("Authentication request from board002A".encode("utf-8"))
    
    ## for board 0035
    #client_socket.send("Authentication request from board0035".encode("utf-8"))

    ## for board 0088
    client_socket.send("Authentication request from board0088".encode("utf-8"))



    ## outliers
    #client_socket.send("Authentication request from board001B".encode("utf-8"))
    #client_socket.send("Authentication request from board003A".encode("utf-8"))

    #client_socket.send("Authentication request from board0017".encode("utf-8"))


    print("Sending auth request to server...")
    time.sleep(3)
  
     
    msg = client_socket.recv(BUFFER_SIZE).decode("utf-8")
    print("From server:", msg)
   
    ## sending image for authentication

    try:
            
        print("Sending image:", filename)
 
        
        # send the filename and filesize
        client_socket.send(f"{filename}{SEPARATOR}{filesize}".encode())
        
        # open the file in read binary mode
        with open(filename, "rb") as file:
            while True:
                # read the bytes from the file
                bytes_read = file.read(BUFFER_SIZE)
                if not bytes_read:
                    # file transmitting is done
                    break
                # sendall to assure transimission in busy networks
                client_socket.sendall(bytes_read)
    
    except BrokenPipeError:
        print("Connection closed by remote server.. try again!")

    ### todo ack from server
    #auth_msg = client_socket.recv(BUFFER_SIZE).decode("utf-8")
    #print("from server:",auth_msg)
    #time.sleep(5)

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
