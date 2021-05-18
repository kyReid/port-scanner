import argparse


def arg_parser():
    """
    parses arguments input from user on the command line
    :return: arguments (tuple)
    """
    # generate parser object and create arguments
    parser = argparse.ArgumentParser(description="Port Scanner with Banner Grabbing functionality")
    parser.add_argument("-i", dest="internet_protocol", help="IP address, use /x for range in 255.255.255.x network")
    parser.add_argument("-p", dest="port_mode", help="s: single port | m: multiple ports | r: range of ports")

    args = parser.parse_args()
    port_modes = ['s', 'm', 'r']

    # error handling
    if not args.internet_protocol:
        parser.error(">> please specify an IP address of IP address range, use --help for more info")
    elif not args.port_mode:
        parser.error(">> Please specify how you'd like to handle ports, use --help for more info.")
    elif not args.port_mode.isalpha():
        parser.error(">> Please verify port mode is a letter, use --help for more info.")
    elif args.port_mode not in port_modes:
        parser.error(">> Please verify port mode is 1 of 3 usable letters, use --help for more info.")
    else:
        pass

    return args.internet_protocol, args.port_mode
