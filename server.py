###b_kh
###ali_coder

import socket,threading
from router import Router

#found thread for process
def Tread(client):
        router=Router('maps.txt')
        start,end=tuple(client.recv(1024))
        best_direction = router.find_shortest_path( start,end )

        client.send("maps.txt".encode())
        client.send(f'{best_direction}'.encode())
        client.close()

#found socket for server with id and port appoint
soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
id,port="127.0.0.1",72
soc.bind((id,port))
soc.listen(10)

#listen to ten client for give answer
for _ in range(1,11):
    client,address=soc.accept()
    threading.Thread(target=Tread,args=(client,)).start()
    print(f"Hi client {_}")
soc.close()
