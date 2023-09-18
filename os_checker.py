
# Copyright 2023 Pawel Suchanecki <psuchanecki@almalinux.org>
# 
# MIT License
#
# os_checker: A Python library to conditionally execute functions based on the operating system and version.

import os
import yaml
from functools import wraps
import subprocess

MESSAGE_PREFIX = "os_checker: "

class os_checker:
    def __init__(self, yaml_path=None, supported_versions=None):
        self.supported_versions = supported_versions or {}
        self.os_info_cache = None

        if yaml_path:
            try:
                with open(yaml_path, 'r') as f:
                    self.supported_versions = yaml.safe_load(f)
            except FileNotFoundError:
                print(f"{MESSAGE_PREFIX}YAML file not found. Proceeding without it.")

    def get_os_info(self):
        if self.os_info_cache:
            return self.os_info_cache

        if os.path.exists("/etc/os-release"):
            with open("/etc/os-release", "r") as f:
                lines = f.readlines()
            os_info = {}
            for line in lines:
                if "=" in line:
                    key, value = line.strip().split("=", 1)
                    os_info[key] = value.strip('"')
            self.os_info_cache = os_info
            return os_info
        else:
            try:
                import distro
                self.os_info_cache = {'ID': distro.id(), 'VERSION_ID': distro.version()}
                return self.os_info_cache
            except ImportError:
                self.os_info_cache = {'ID': subprocess.getoutput("uname"), 'VERSION_ID': 'Unknown'}
                return self.os_info_cache

    def os_check_decorator(self, supported_os=None, version=None, custom_success_msg=None, custom_failure_msg=None):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                os_info = self.get_os_info()
                current_os = os_info.get('ID', 'Unknown').lower()
                current_version = os_info.get('VERSION_ID', 'Unknown').lower()

                supported_versions = self.supported_versions.get(current_os, [])
                is_supported = current_os == supported_os.lower() and (not version or current_version == version.lower() or not supported_versions)

                if is_supported:
                    if custom_success_msg:
                        print(f"{MESSAGE_PREFIX}{custom_success_msg}")
                    return func(*args, **kwargs)
                else:
                    if custom_failure_msg:
                        print(f"{MESSAGE_PREFIX}{custom_failure_msg}")
                    else:
                        print(f"{MESSAGE_PREFIX}Unsupported OS: {current_os} {current_version}. Not running function: {func.__name__}")

            return wrapper
        return decorator

