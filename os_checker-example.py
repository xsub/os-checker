# Copyright 2023 by Pawel Suchanecki <psuchanecki@almalinux.org>
# A demo to illustrate how to use the os_checker library for enforcing system and release version requirements.

from os_checker import os_checker

checker = os_checker(supported_versions={'AlmaLinux': ['9.2'], 'Ubuntu': ['20.04', '23.04']})

MESSAGE_PREFIX = "os_checker-demo: "

# AlmaLinux 8.4 Cases
def almalinux_84_default():
    print(f"{MESSAGE_PREFIX}Default check for supported_os='AlmaLinux', version='8.4'.")
    print("---")

def almalinux_84_custom_failure():
    print(f"{MESSAGE_PREFIX}Custom Failure check for supported_os='AlmaLinux', version='8.4'.")
    print("---")

def almalinux_84_custom_success():
    print(f"{MESSAGE_PREFIX}Custom Success check for supported_os='AlmaLinux', version='8.4'.")
    print("---")

def almalinux_84_both_custom():
    print(f"{MESSAGE_PREFIX}Both Custom check for supported_os='AlmaLinux', version='8.4'.")
    print("---")

# AlmaLinux 9.2 Cases
def almalinux_92_default():
    print(f"{MESSAGE_PREFIX}Default check for supported_os='AlmaLinux', version='9.2'.")
    print("---")

def almalinux_92_custom_failure():
    print(f"{MESSAGE_PREFIX}Custom Failure check for supported_os='AlmaLinux', version='9.2'.")
    print("---")

def almalinux_92_custom_success():
    print(f"{MESSAGE_PREFIX}Custom Success check for supported_os='AlmaLinux', version='9.2'.")
    print("---")

def almalinux_92_both_custom():
    print(f"{MESSAGE_PREFIX}Both Custom check for supported_os='AlmaLinux', version='9.2'.")
    print("---")

# Ubuntu 20.04 Cases
def ubuntu_2004_default():
    print(f"{MESSAGE_PREFIX}Default check for supported_os='Ubuntu', version='20.04'.")
    print("---")

def ubuntu_2004_custom_failure():
    print(f"{MESSAGE_PREFIX}Custom Failure check for supported_os='Ubuntu', version='20.04'.")
    print("---")

def ubuntu_2004_custom_success():
    print(f"{MESSAGE_PREFIX}Custom Success check for supported_os='Ubuntu', version='20.04'.")
    print("---")

def ubuntu_2004_both_custom():
    print(f"{MESSAGE_PREFIX}Both Custom check for supported_os='Ubuntu', version='20.04'.")
    print("---")

# Ubuntu 23.04 Cases
def ubuntu_2304_default():
    print(f"{MESSAGE_PREFIX}Default check for supported_os='Ubuntu', version='23.04'.")
    print("---")

def ubuntu_2304_custom_failure():
    print(f"{MESSAGE_PREFIX}Custom Failure check for supported_os='Ubuntu', version='23.04'.")
    print("---")

def ubuntu_2304_custom_success():
    print(f"{MESSAGE_PREFIX}Custom Success check for supported_os='Ubuntu', version='23.04'.")
    print("---")

def ubuntu_2304_both_custom():
    print(f"{MESSAGE_PREFIX}Both Custom check for supported_os='Ubuntu', version='23.04'.")
    print("---")

if __name__ == '__main__':
    # AlmaLinux 8.4
    checker.os_check_decorator(supported_os='AlmaLinux', version='8.4')(almalinux_84_default)()
    checker.os_check_decorator(supported_os='AlmaLinux', version='8.4', custom_failure_msg="Custom failure: OS and version.")(almalinux_84_custom_failure)()
    checker.os_check_decorator(supported_os='AlmaLinux', version='8.4', custom_success_msg="Custom success: OS and version.")(almalinux_84_custom_success)()
    checker.os_check_decorator(supported_os='AlmaLinux', version='8.4', custom_success_msg="Custom success: OS and version.", custom_failure_msg="Custom failure: OS and version.")(almalinux_84_both_custom)()

    # AlmaLinux 9.2
    checker.os_check_decorator(supported_os='AlmaLinux', version='9.2')(almalinux_92_default)()
    checker.os_check_decorator(supported_os='AlmaLinux', version='9.2', custom_failure_msg="Custom failure: OS and version.")(almalinux_92_custom_failure)()
    checker.os_check_decorator(supported_os='AlmaLinux', version='9.2', custom_success_msg="Custom success: OS and version.")(almalinux_92_custom_success)()
    checker.os_check_decorator(supported_os='AlmaLinux', version='9.2', custom_success_msg="Custom success: OS and version.", custom_failure_msg="Custom failure: OS and version.")(almalinux_92_both_custom)()

    # Ubuntu 20.04
    checker.os_check_decorator(supported_os='Ubuntu', version='20.04')(ubuntu_2004_default)()
    checker.os_check_decorator(supported_os='Ubuntu', version='20.04', custom_failure_msg="Custom failure: OS and version.")(ubuntu_2004_custom_failure)()
    checker.os_check_decorator(supported_os='Ubuntu', version='20.04', custom_success_msg="Custom success: OS and version.")(ubuntu_2004_custom_success)()
    checker.os_check_decorator(supported_os='Ubuntu', version='20.04', custom_success_msg="Custom success: OS and version.", custom_failure_msg="Custom failure: OS and version.")(ubuntu_2004_both_custom)()

    # Ubuntu 23.04
    checker.os_check_decorator(supported_os='Ubuntu', version='23.04')(ubuntu_2304_default)()
    checker.os_check_decorator(supported_os='Ubuntu', version='23.04', custom_failure_msg="Custom failure: OS and version.")(ubuntu_2304_custom_failure)()
    checker.os_check_decorator(supported_os='Ubuntu', version='23.04', custom_success_msg="Custom success: OS and version.")(ubuntu_2304_custom_success)()
    checker.os_check_decorator(supported_os='Ubuntu', version='23.04', custom_success_msg="Custom success: OS and version.", custom_failure_msg="Custom failure: OS and version.")(ubuntu_2304_both_custom)()

