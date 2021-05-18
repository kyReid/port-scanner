import scanner
import socket


def banner_grabber(ip):
    """
    grabs information about ports services being run on targeted machine
    :param ip: internet protocol
    :return:
    """

    # attempts a connection for 2 seconds
    socket.setdefaulttimeout(2)
    banner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while not scanner.banner_queue.empty():
        port = scanner.banner_queue.get()
        try:
            banner.connect((ip, int(port)))
            # send request
            banner.send(b"GET / HTTP/1.1\r\n\r\n")
            banner_info = banner.recv(4096)
            banner.close()
            print(f"PORT {port} service information\n" + str(banner_info.decode()) + "\n")
        except socket.error:
            pass
