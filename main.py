import win32api
import win32process
import win32gui
import argparse


def build_parser():
    parser = argparse.ArgumentParser(description='This is a title changer')
    parser.add_argument('pid', action="store", type=int)
    parser.add_argument('new_title', action="store", type=str)

    parse_results = parser.parse_args()

    return parse_results


def find_it(hwnd, parser):
    ttl = win32gui.GetWindowText(hwnd)
    t, p = win32process.GetWindowThreadProcessId(hwnd)

    if parser.pid == p:
        win32gui.SetWindowText(hwnd, parser.new_title)


def main():
    parser = build_parser()
    win32gui.EnumWindows(find_it, parser)


if __name__ == "__main__":
    main()
