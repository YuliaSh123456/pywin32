import win32api
import win32con
import win32process
import win32gui
import argparse



def build_parser():
    parser = argparse.ArgumentParser(description='This is a title changer')
    parser.add_argument('proc_name', action="store", type=str)
    parser.add_argument('new_title', action="store", type=str)

    parse_results = parser.parse_args()

    return parse_results


def enum_handler(hwnd, parser):
    _, p = win32process.GetWindowThreadProcessId(hwnd)

    try:
        handle = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ, False, p)
        proc_name = win32process.GetModuleFileNameEx(handle, 0)
    except Exception as ex:
        print ex

    if parser.proc_name in proc_name:
        win32gui.SetWindowText(hwnd, parser.new_title)


def main():
    parser = build_parser()

    win32gui.EnumWindows(enum_handler, parser)


if __name__ == "__main__":
    main()
