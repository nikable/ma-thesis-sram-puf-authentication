import socket
import time
import os
import model_inference as mi
import argparse

def server_program():
    # get the hostname/ip address
    # host = "192.168.178.40" ## considering when static ip
    host = "rp-labs1.local"
    port = 18000  #  port no above reserved ports (1024)

    server_socket = socket.socket()  # get socket instance
    server_socket.bind((host, port))  # bind host address and port together
    
    # starting server module
    print("Server started")

    # set metadata
    BUFFER_SIZE = 4096
    SEPARATOR = "<SEPARATOR>"
    ENCODING = "utf-8"

    # configure how many client the server can listen simultaneously
    server_socket.listen(1)
    
    # add a timeout
    server_socket.settimeout(150.0)   # in seconds  
    
    # parse labels/device list
    parser = argparse.ArgumentParser()
    parser.add_argument(
    '-d',
    '--devices',
    default='../efficientnet/labels.txt',
    help='list of enrolled devices')
    args = parser.parse_args()
    
    with open(args.devices) as file:
        devices = [line.rstrip() for line in file]
    #print(devices)

    # accept a new connection 
    conn, address = server_socket.accept()

    print("Connection from: " + str(address))

    auth_req = conn.recv(BUFFER_SIZE).decode()
    print(auth_req)
    board = auth_req.split()[-1]
    print("Board name:", board)
    
    if board not in devices:
        print("Board is not present in the enrolled device list... Request rejected!!")
        conn.close()  # close the connection
        server_socket.close() # close the server socket
    
    if board in devices:
        time.sleep(2)
        
        # file related stuff
        conn.send("Please send the board image".encode(ENCODING))
        received = conn.recv(BUFFER_SIZE).decode()
        filename, filesize = received.split(SEPARATOR)
        # remove absolute path if there is
        filename = os.path.basename(filename)
        # informing the recived file 
        print("Receiving file:", filename)

        
        with open(filename, "wb") as file:
            while True:
                # read 1024 bytes from the socket (receive)
                bytes_read = conn.recv(BUFFER_SIZE)
                if not bytes_read:
                # terminate file transmitting is done
                    break
                # write to the file the bytes we just received
                file.write(bytes_read)

        print("File received. model being executed..")
        time.sleep(2)

        # calling efficientnet_lite model for classification
        model = "/home/pi1/tflite/model3_v2/efficientnet/model.tflite"

        image = filename
        score, label = mi.classify_image(model,image)  

        print("Image label detected:", label , "with confidence:", score*100, "%")
        
        if(score*100 > 90 and label.lower() == board.lower()):
            print("Predicted label by model from board image is correct.. authentication successful")
            conn.send("Device authenticated".encode(ENCODING))

        else:
            print("Board name and predicted image label mismatch...authentication not successful!")
            conn.send("Device not authenticated".encode(ENCODING))
        

        conn.close()  # close the connection
        server_socket.close() # close the server socket

if __name__ == '__main__':
    server_program()
