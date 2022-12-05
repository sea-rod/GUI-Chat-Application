import socket 
import threading

class Server:
    '''
    This is the server side code
    '''

    __client_soc = {}

    def __init__(self, host:str = "0.0.0.0", port:int = 8080, mess_size:int = 1024*128, head:int = 20) -> None:
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
        try:
            while self.__server:
                conn ,addr = self.__server.accept()
                print(f"{addr} connected....")
                try:
                    name = conn.recv(self.__mess_size).decode()
                    name = name[self.__head:]
                    if not self.user_exit(name):
                        print(name)
                        self.__client_soc[name] = conn
                        print(self.__client_soc) 
                        self.t1=threading.Thread(target = self.receive,args=(name,))
                        self.t1.start()
                    else:
                        mess = "xxxclosedxxx"
                        mess = f"{len(mess):{self.__head}}{mess}".encode()
                        conn.send(mess)
                    
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)


    def receive(self, name:str):
        '''
        This function receives messaages from the clients
        Parameters:
            conn (socket): It holds the clients socket
        '''
        try:
            while self.__server:
                conn = self.__client_soc[name]
                mess = ''
                raw_mess = conn.recv(self.__mess_size).decode()
                mess_len = int(raw_mess[:self.__head])
                mess += raw_mess[self.__head:]

                while len(mess) < mess_len:
                    mess += conn.recv(self.__mess_size).decode()

                cl_mess = f'{name}:{mess}'
                mess_len = (f'{len(cl_mess):{self.__head}}')
                mess_len += cl_mess

                if mess == "xxxclosedxxx":
                    conn.close()
                    del self.__client_soc[name]
                    break

                self.__send(mess_len,conn)

        except Exception as e: 
            conn.close() 
            del self.__client_soc[name]
            # print(e)
            


    

    def __send(self,mess:str,conn:socket):
        '''
        It send the message to all the clients connected
        '''
        for soc in self.__client_soc.values():
            if soc == conn:
                continue
            soc.send(mess.encode())
        print(mess)


    def terminate(self):
        self.__server.close()


    def get_port(self):
        return self.__port

    def user_exit(self,key):
        return key in self.__client_soc.keys()

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
    except KeyboardInterrupt:
        print("Server closed")




