import sys


def get_argv_port():
    if len(sys.argv) <= 1 or sys.argv[1] == "":
        print("Need arg port")
        sys.exit(1)
    port = int(sys.argv[1])
    if port <= 0 or port > 65535:
        print("port range is [1,65535]")
        sys.exit(1)
    return port
