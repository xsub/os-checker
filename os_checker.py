# Copyright 2023 Pawel Suchanecki <psuchanecki@almalinux.org>
# 
# MIT License
#
# os_checker: A Python library to conditionally execute functions based on the operating system and version.

import subprocess
import yaml
from functools import wraps

MESSAGE_PREFIX = "os_checker: "

class os_checker:
    def __init__(self, yaml_path=None):
        self.supported_systems_and_versions = {}
        if yaml_path:
            try:
                with open(yaml_path, 'r') as f:
                    self.supported_systems_and_versions = yaml.safe_load(f)
            except FileNotFoundError:
                print(f"{MESSAGE_PREFIX} YAML file not found. Proceeding without it.")

    def get_os_info(self):
        # First try /etc/os-release
        try:
            with open("/etc/os-release", "r") as f:
                for line in f:
                    if line.startswith('NAME='):
                        os_name = line.split('=')[1].strip('"\n')
                    if line.startswith('VERSION_ID='):
                        os_version = line.split('=')[1].strip('"\n')
                return os_name, os_version
        except FileNotFoundError:
            pass
        
        # Fallback to distro
        try:
            import distro
            return distro.name(), distro.version()
        except ImportError:
            pass

        # Last fallback to uname
        try:
            uname_output = subprocess.getoutput('uname')
            os_name = uname_output.strip()
            return os_name, None
        except Exception:
            return None, None

    def os_check_decorator(self, supported_os=None, version=None, custom_success_msg=None, custom_failure_msg=None):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                os_name, os_version = self.get_os_info()
                if not os_name:
                    print(f"{MESSAGE_PREFIX}Cannot determine OS or version.")
                    return

                if supported_os and os_name.lower() == supported_os.lower():
                    if version and os_version == version:
                        msg = custom_success_msg if custom_success_msg else f"Custom success: {supported_os} and {version}."
                        print(f"{MESSAGE_PREFIX}{msg}")
                        return func(*args, **kwargs)
                    elif not version:
                        msg = custom_success_msg if custom_success_msg else f"Custom success: {supported_os}."
                        print(f"{MESSAGE_PREFIX}{msg}")
                        return func(*args, **kwargs)

                msg = custom_failure_msg if custom_failure_msg else f"Unsupported OS: {os_name} {os_version}. Not running function: {func.__name__}"
                print(f"{MESSAGE_PREFIX}{msg}")
            return wrapper
        return decorator
