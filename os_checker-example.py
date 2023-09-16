# Copyright 2023 Pawel Suchanecki <psuchanecki@almalinux.org>
# 
# MIT License
#
# os_checker-example: Demonstration of the os_checker library's capabilities.

from os_checker import os_checker

checker = os_checker(yaml_path='supported_systems.yaml')

MESSAGE_PREFIX = "os_checker-demo: "

@checker.os_check_decorator(supported_os='AlmaLinux', custom_success_msg='Custom success: OS-only.')
def only_os_demo():
    print(f"{MESSAGE_PREFIX}OS-only check for supported_os='AlmaLinux'.")
    print(f"{MESSAGE_PREFIX}This will run only on AlmaLinux irrespective of the version.")
    print("---")

@checker.os_check_decorator(supported_os='AlmaLinux', version='8.4', custom_success_msg='Custom success: OS and version.')
def os_and_version_demo():
    print(f"{MESSAGE_PREFIX}OS and version check for supported_os='AlmaLinux', version='8.4'.")
    print(f"{MESSAGE_PREFIX}This will run only on AlmaLinux version 8.4.")
    print("---")

@checker.os_check_decorator(supported_os='AlmaLinux', version='9.2', custom_success_msg='Custom success: OS and version 9.2.')
def os_and_version_demo_2():
    print(f"{MESSAGE_PREFIX}OS and version check for supported_os='AlmaLinux', version='9.2'.")
    print(f"{MESSAGE_PREFIX}This will run only on AlmaLinux version 9.2.")
    print("---")

if __name__ == '__main__':
    only_os_demo()
    os_and_version_demo()
    os_and_version_demo_2()
    
    # With custom failure messages
    checker.os_check_decorator(supported_os='Ubuntu', custom_failure_msg='Custom failure: OS-only.')(only_os_demo)()
    checker.os_check_decorator(supported_os='AlmaLinux', version='8.4', custom_failure_msg='Custom failure: OS and version.')(os_and_version_demo)()
    checker.os_check_decorator(supported_os='AlmaLinux', version='9.2', custom_failure_msg='Custom failure: OS and version 9.2.')(os_and_version_demo_2)()

    # With both custom success and failure messages
    checker.os_check_decorator(supported_os='AlmaLinux', custom_success_msg='Both custom: success', custom_failure_msg='Both custom: failure')(only_os_demo)()
    checker.os_check_decorator(supported_os='AlmaLinux', version='8.4', custom_success_msg='Both custom: success', custom_failure_msg='Both custom: failure')(os_and_version_demo)()
    checker.os_check_decorator(supported_os='AlmaLinux', version='9.2', custom_success_msg='Both custom: success', custom_failure_msg='Both custom: failure')(os_and_version_demo_2)()

    # Cases with only custom success message
    checker.os_check_decorator(supported_os='AlmaLinux', custom_success_msg='Only custom success: OS-only.')(only_os_demo)()
    checker.os_check_decorator(supported_os='AlmaLinux', version='8.4', custom_success_msg='Only custom success: OS and version.')(os_and_version_demo)()
    checker.os_check_decorator(supported_os='AlmaLinux', version='9.2', custom_success_msg='Only custom success: OS and version 9.2.')(os_and_version_demo_2)()
