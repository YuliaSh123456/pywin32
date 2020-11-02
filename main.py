import psutil
import win32api
import win32con
import win32process
import win32gui
import argparse


# pid = None

def build_parser():
    parser = argparse.ArgumentParser(description='This is a title changer')
    parser.add_argument('proc_name', action="store", type=str)
    parser.add_argument('new_title', action="store", type=str)

    parse_results = parser.parse_args()

    return parse_results


def enum_handler(hwnd, ll):
    _, p = win32process.GetWindowThreadProcessId(hwnd)
    if p is not None and p == ll[0]:
        win32gui.SetWindowText(hwnd, ll[1])


def main():
    parser = build_parser()

    for proc in psutil.process_iter():
        if parser.proc_name in proc.name():
            pid = proc.pid

    win32gui.EnumWindows(enum_handler, [pid, parser.new_title])


if __name__ == "__main__":
    main()
