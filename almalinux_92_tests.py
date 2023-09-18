from os_checker import os_checker

checker = os_checker(yaml_path="supported_versions.yaml")  # Assuming YAML config with supported versions

# Default Test
@checker.os_check_decorator(supported_os='AlmaLinux', version='9.2')
def almalinux_92_default():
    print("AlmaLinux 9.2: Default")

# Custom Success Message Test
@checker.os_check_decorator(supported_os='AlmaLinux', version='9.2', custom_success_msg="Custom success message.")
def almalinux_92_custom_success():
    print("AlmaLinux 9.2: Custom Success Message")

# Custom Failure Message Test
@checker.os_check_decorator(supported_os='AlmaLinux', version='8.4', custom_failure_msg="Custom failure message.")
def almalinux_92_custom_failure():
    print("AlmaLinux 9.2: Custom Failure Message")

if __name__ == '__main__':
    almalinux_92_default()
    almalinux_92_custom_success()
    almalinux_92_custom_failure()

