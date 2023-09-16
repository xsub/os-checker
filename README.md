# os_checker Library (PoC)

## Author
Pawel Suchanecki <psuchanecki@almalinux.org>

## License
MIT License

## Overview
The `os_checker` library offers a Python decorator to conditionally execute functions based on the underlying operating system and its version. It supports specifying supported systems and versions through a YAML configuration file.

## Features
- Utilizes `/etc/os-release` for accurate OS information.
- Fallbacks to Python `distro` library or `uname` if `/etc/os-release` is unavailable.
- Customizable success and failure messages.

## Requirements
- Python 3.x
- PyYAML (for YAML configuration)
- distro library (Optional, for fallback)

## Installation
```bash
pip install PyYAML
pip install distro  # Optional
```

## Usage & Example Explanation

### Code Snippet from `os_checker-example.py`

```python
from os_checker import os_checker

checker = os_checker(yaml_path='supported_systems.yaml')

MESSAGE_PREFIX = "os_checker-demo: "

# Check only based on the OS
@checker.os_check_decorator(supported_os='AlmaLinux')
def only_os_demo():
    print(f"{MESSAGE_PREFIX}OS-only check for supported_os='AlmaLinux'.")
    print(f"{MESSAGE_PREFIX}This will run only on AlmaLinux, irrespective of the version.")
    print("---")

# ... Other functions
```

### Example Cases Explained

1. **Only OS Check (`only_os_demo`)**  
   - **What it does**: Verifies if the running OS is AlmaLinux. If so, executes the function.
   - **Messages**: Custom success or failure messages related to OS-only checks.
  
2. **OS and Version Check (`os_and_version_demo`)**  
   - **What it does**: Verifies if the running OS is AlmaLinux and its version is 8.4. If so, executes the function.
   - **Messages**: Custom success or failure messages for both OS and version checks.
  
3. **OS and Another Version Check (`os_and_version_demo_2`)**  
   - **What it does**: Verifies if the running OS is AlmaLinux and its version is 9.2. If so, executes the function.
   - **Messages**: Custom success or failure messages for both OS and version checks.
  
Each function in `os_checker-example.py` illustrates one of these cases.

## Fallback Mechanism

If `/etc/os-release` is not available, the library falls back to using the Python `distro` library. If `distro` is also not accessible, it uses `uname` to fetch the system name.

---
