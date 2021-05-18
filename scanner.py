from queue import Queue
import threading
import socket

# manage access of multiple threats on a single resource
port_queue = Queue()
banner_queue = Queue()


def port_mode_handler(mode):
    """
    Adds ports to queue based on mode request from user

    :param mode: multiple ports or range of ports
    :return:
    """

    global banner_queue

    # single port request
    if mode == 's':
        request = input("Enter port number: ")
        port_queue.put(request)
        banner_queue.put(request)
    # multiple ports requested
    elif mode == 'm':
        port_requests = ""
        while port_requests != '0':
            port_requests = input("Enter port numbers, (enter 0 to stop): ")
            if port_requests == '0':
                break
            else:
                port_queue.put(port_requests)
                banner_queue.put(port_requests)
    # range of requested ports
    elif mode == 'r':
        port_request = []
        print("[Enter min/max port range]")
        min_port = int(input("Enter min port: "))
        max_port = int(input("Enter max port: "))
        # append requests to list
        current_port = min_port
        while current_port <= max_port:
            port_queue.put(current_port)
            banner_queue.put(current_port)
            current_port = current_port + 1
    else:
        print("ERROR, exiting program")
        exit(-1)


def port_connect(ip, port):
    """
    establishes a connection to ports
    :param ip: internet protocol
    :param port: services
    :return: True if connection found/ False if no connection found
    """
    try:
        # create connection socket object, try to connect 3 times
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.settimeout(3)
        conn.connect((ip, port))
        return True
    except socket.error:
        return False


def thread_outcome(ip):
    """
    threads scans if user requests a range of  ports
    :param ip: internet protocol
    :return:
    """
    while not port_queue.empty():
        port = port_queue.get()
        if port_connect(ip, int(port)):
            print(f"{port}\t\tOPEN")


def thread_processor(ip):
    """
    executes threading outcome based on thread size request
    :param ip: internet protocol
    :return:
    """
    threads = []

    # threading process for range of ports
    for thread in range(100):
        thread = threading.Thread(target=thread_outcome(ip))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()