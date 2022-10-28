import socket

words = ["able","acid","aged","also","area","army","away","baby","back","ball","bath","bear","beat","been","beer","bell","belt","best","bill","bird","blow","blue","boat","body","both","bowl","bulk","burn","bush","busy","call","calm","came","camp","card","care","case","cash","coat","code","cold","come","cook","cool","cope","copy","core","cost","crew","crop","dear","debt","deep","deny","desk","dial","drug","dual","duke","dust","duty","each","earn","ease","east","easy","edge","else","even","ever","evil","exit","face","fact","fail","fair","fall","farm","fast","fate","fear","feed","feel","feet","foot","ford","form","fort","four","free","from","fuel","full","fund","gain","game","gate","gave","gear","gene","gift","girl","give","glad","goal","goes","gold","Golf","gone","good","gray","held","hell","help","here","hero","high","hill","hire","hold","hole","holy","home","hope","hunt","hurt","idea","inch","into","iron","item","jack","king","knee","knew","know","lack","lady","laid","lake","like","lost","love","luck","made","mail","main","make","male","many","Mark","mass","matt","meal","mean","meat","meet","menu","much","must","name","navy","near","neck","need","news","next","nice","open","oral","over","pace","pack","page","paid","pain","pair","palm","park","part","pass","past","path","peak","pick","pink","pull","pure","push","race","rail","rain","rank","rare","rate","read","real","roll","roof","room","root","rose","rule","rush","ruth","safe","said","sake","sale","salt","some","song","soon","sort","soul","spot","star","stay","step","stop","such","suit","sure","take","tale","talk","tall","true","tune","turn","twin","type","unit","upon","used","user","vary","vast","very","what","when","whom","wide","wife","wild","will","wood","word","wore","work","yard","yeah","year","your","zero","zone"]

def server_program():
    # get the hostname
    port = int(input("Enter port number (above 1023): "))
    host = socket.gethostbyname(socket.gethostname())
    nums = host.split(".")
    name = words[int(nums[0])] + "-" + words[int(nums[1])] + "-" + words[int(nums[2])] + "-" + words[int(nums[3])]
    print("Name: ", name)
    print("Code: ", port)
    print("^^Share these with friends!^^")
    count = 0
    quit = ''
    
    server_socket = socket.socket()
    try:
        server_socket.bind((host, port))
    except socket.error as e:
        print(str(e))
    print('Server Created...')
    server_socket.listen(2)

    # accept connections
    conn1, addr1 = server_socket.accept()
    name1 = conn1.recv(1024).decode()
    print(name1 + " connected " + str(addr1))
    conn2, addr2 = server_socket.accept()
    name2 = conn2.recv(1024).decode()
    print(name2 + " connected " + str(addr2))

    conn1.send(name2.encode())
    conn2.send(name1.encode())

    while True:

        while True:
            resp1 = conn1.recv(1024).decode()
            resp2 = conn2.recv(1024).decode()
            if resp1 != "" and resp2 != "":
                break

        if resp1 == "leave":
            conn1.close()
            conn2.send((name1 + " left the game").encode())
            conn2.close()
            break
        if resp2 == "leave":
            conn2.close()
            conn1.send((name2 + " left the game").encode())
            conn1.close()
            break

        if resp1 == resp2:
            conn1.send("tie".encode())
            conn2.send("tie".encode())
        elif resp1 == "r" and resp2 == "p":
            conn1.send(name2.encode())
            conn2.send(name2.encode())
        elif resp1 == "r" and resp2 == "s":
            conn1.send(name1.encode())
            conn1.send(name1.encode())
        elif resp1 == "p" and resp2 == "r":
            conn1.send(name1.encode())
            conn2.send(name1.encode())
        elif resp1 == "p" and resp2 == "s":
            conn1.send(name2.encode())
            conn2.send(name2.encode())
        elif resp1 == "s" and resp2 == "r":
            conn1.send(name2.encode())
            conn2.send(name2.encode())
        elif resp1 == "s" and resp2 == "p":
            conn1.send(name1.encode())
            conn2.send(name1.encode())
        resp1 = ''
        resp2 = ''

# main
if __name__ == '__main__':
    server_program()