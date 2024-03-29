import os
import sys


def check_reboot():
    """Return true if computer has pending reboot"""
    return os.path.exists('/run/reboot-required')


def check_disk_full(disk, min_gb, min_percent):
    """Return true if there isn't enough space, false otherwise."""
    du = shutil.disk_usage(disk)
    #calculate percentage of free space
    percent_free = 100 * du.free / du.total
    #calculate how many free gigabytes
    gigabytes_free = du.free / 2 ** 30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return True
    return False


def check_root_full():
    """Return true if root partition is full, False otherwise."""
    return check_disk_full(disk="/", min_gb=2, min_percent=10)




def main():
    checks = [
        (check_reboot, "Pending Reboot"),
        (check_root_full, "Root Partition full")
    ]
    everything_ok = True
    for check, msg in checks:
        if checks():
            print(msg)
            everything_ok = False
            sys.exit(1)


    if not everything_ok:
        sys.exit(1)


    if check_reboot():
        print('Pending reboot..')
        sys.exit(1)
    if check_disk_full(disk="/", min_gb=2, min_percent=10):
        print("Root partition full.")
        sys.exit(1)
    print("Everything ok.")
    sys.exit(0)


main()
