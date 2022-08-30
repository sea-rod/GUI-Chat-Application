import socket 
import threading

class Server:
    '''
    This is the server side code
    '''

    __client_soc = {}

    def __init__(self, host = "127.0.0.1", port = 8080, mess_size = 1024*128, head = 20) -> None:
        self.__host = host
        self.__port = port 
        self.__mess_size = mess_size
        self.__head = head
    
    def listen(self):
        '''
        It starts listening for clients
        '''
        self.__server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.__server.bind((self.__host,self.__port))
        print(f"sever listening on {self.__host}:{self.__port}")
        print("press Clrl+c to exit..")
        self.__server.listen(5)
    
    def accept(self):
        '''
        It accepts connection from the clients
        '''
        while True:
            conn ,addr = self.__server.accept()
            print(f"{addr} connected....")
            conn.send(("                  16Enter your name:").encode())
            try:
                name = conn.recv(self.__mess_size).decode()
                self.__client_soc[conn] = name[self.__head:]
                t1=threading.Thread(target = self.receive,args=(conn,))
                t1.start()
            except Exception as e:
                print(e)


    def receive(self, conn:socket):
        '''
        This function receives messaages from the clients
        Parameters:
            conn (socket): It holds the clients socket
        '''
        try:
            while True:
                mess = ''
                raw_mess = conn.recv(self.__mess_size).decode()
                mess_len = int(raw_mess[:self.__head])
                mess += raw_mess[self.__head:]

                while len(mess) < mess_len:
                    mess += conn.recv(self.__mess_size).decode()

                cl_mess = f'[+][{self.__client_soc[conn]}]:{mess}'
                mess_len = (f'{len(cl_mess):{self.__head}}')
                mess_len += cl_mess

                if mess == "xxxclosedxxx":
                    del self.__client_soc[conn]
                    break

                self.__send(mess_len)

        except Exception as e:  
            del self.__client_soc[conn]
            print(e)
            


    

    def __send(self,mess:str):
        '''
        It send the message to all the clients connected
        '''
        for soc in self.__client_soc.keys():
            soc.send(mess.encode())
        print(mess)

if __name__ == "__main__":
    try:
        ip = input("Enter the host name or ip address you to bind the server with:")
        port = int(input("Enter the port:"))
        ip = socket.gethostbyname(ip)
        srv = Server(ip,port)
        srv.listen()
        srv.accept()


    except socket.gaierror:
        print("Please a enter a valid ip or host name and try again")

        
    except ValueError:
        print("Port number should be a integer")




