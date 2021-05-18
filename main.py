import grabber
import parser
import scanner

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # grab cmd arguments
    ip, port_mode = parser.arg_parser()

    # determines port mode based on user request
    scanner.port_mode_handler(port_mode)

    # run port scanning and banner grabbing based on port mode request
    # header for port status table
    print("\n\nPORT\t\tSTATUS\n" + "-" * 25)
    if port_mode == "s":
        scanner.thread_processor(ip)
        print("\n[+] port Scanning is complete.\n[+] port service processing complete.")
        print("\nPort service details displayed below:\n"
              + "-" * 40)
        grabber.banner_grabber(ip)
    elif port_mode == "m":
        scanner.thread_processor(ip)
        print("\n[+] port Scanning is complete.\n[+] port service processing complete.")
        print("\nPort service details displayed below:\n"
              + "-" * 40)
        grabber.banner_grabber(ip)
    elif port_mode == "r":
        scanner.thread_processor(ip)
        print("\n[+] port Scanning is complete.\n[+] port service processing complete.")
        print("\nPort service details displayed below:\n"
              + "-" * 40)
        grabber.banner_grabber(ip)
    else:
        print("[ERROR] exiting program!")
        exit(-1)

