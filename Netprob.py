import socket
def prob_http(ip,port):
    s=socket.socket()
    s.settimeout(3)

    try:
        s.connect((ip,port))
        s.send(b"GET / HTTP/1.1\r\nHost:test \r\n\r\n")    
        response = s.recv(1024)
        ##print("\n--- RAW RESPONSE ---")
        print(response.decode(errors="ignore"))
        ##fingerprinting analysis
        print("\n---Analysis---")
        if b"HTTP" in response:
            print("Protocol: HTTP")
        if b"apache" in response: 
            print("Web-Server:Apache")
        for line in response.split(b"\r\n"):
            if b"Server:" in line:
                print("Server Header:", line.decode(errors="ignore"))
    except Exception as e:
        print("Failed:", e)
    finally:
        s.close()
    



ip = input("Enter IP: ")
port = int(input("Enter Port: "))
prob_http(ip,port)
