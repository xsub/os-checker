from os_checker import os_checker

checker = os_checker(yaml_path="supported_versions.yaml")  # Assuming YAML config with supported versions

# macOS 16.0 Custom Success Message Test
@checker.os_check_decorator(supported_os='macOS', version='16.0', custom_success_msg="Custom success message.")
def macos_16_custom_success():
    print("macOS 16.0: Custom Success Message")

# Ubuntu 20.04 Default Test
@checker.os_check_decorator(supported_os='Ubuntu', version='20.04')
def ubuntu_2004_default():
    print("Ubuntu 20.04: Default")

# AlmaLinux 8.4 Custom Failure Message Test (AlmaLinux 8.4 should be unsupported)
@checker.os_check_decorator(supported_os='AlmaLinux', version='8.4', custom_failure_msg="Custom failure message.")
def almalinux_84_custom_failure():
    print("AlmaLinux 8.4: Custom Failure Message")

if __name__ == '__main__':
    macos_16_custom_success()
    ubuntu_2004_default()
    almalinux_84_custom_failure()
