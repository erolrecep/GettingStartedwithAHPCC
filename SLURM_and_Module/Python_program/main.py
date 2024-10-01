import socket

def main():
    try:
        hostname = socket.gethostname()
        print("Hostname:", hostname)
    except Exception as e:
        print("Error getting hostname:", e)
        exit(1)

if __name__ == "__main__":
    main()
