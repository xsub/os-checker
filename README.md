# os_checker Library (PoC)

## Author
Pawel Suchanecki <psuchanecki@almalinux.org>

## License
MIT License

## Overview
The `os_checker` library offers a Python decorator to conditionally execute functions based on the underlying operating system and its version. It provides an interface for specifying supported systems and versions through a YAML configuration file.

## Features
- Utilizes `/etc/os-release` for accurate OS information.
- Fallbacks to Python `distro` library or `uname` if `/etc/os-release` is unavailable.
- Supports YAML configuration for defining supported OS versions.
- Customizable success and failure messages.
- Built-in caching for repeated checks.

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

checker = os_checker(yaml_path='supported_versions.yaml')

MESSAGE_PREFIX = "os_checker-demo: "

# Check only based on the OS
@checker.os_check_decorator(supported_os='AlmaLinux')
def only_os_demo():
    print(f"{MESSAGE_PREFIX}OS-only check for supported_os='AlmaLinux'.")
    print(f"{MESSAGE_PREFIX}This will run only on AlmaLinux, irrespective of the version.")
    print("---")

```

## Fallback Mechanism

If `/etc/os-release` is not available, the library falls back to using the Python `distro` library. If `distro` is also not accessible, it uses `uname` to fetch the system name.


# API Documentation

### Class: `os_checker`

The primary class that provides the core functionalities for operating system checks.

#### Methods:

##### `__init__(self, yaml_path=None)`

- **Parameters:**
  - `yaml_path`: Path to the YAML configuration file that defines supported OS versions. Default is `None`.
  
- **Usage:**
  
  ```python
  checker = os_checker(yaml_path='supported_versions.yaml')
  ```

##### `os_check_decorator(self, supported_os=None, supported_versions=None, unsupported_message=None, supported_message=None)`

A decorator to conditionally execute functions based on the underlying operating system and its version.

- **Parameters:**
  - `supported_os`: A string specifying the supported OS.
  - `supported_versions`: A list of strings specifying the supported OS versions.
  - `unsupported_message`: Custom message to display when the OS is unsupported. Default is `None`.
  - `supported_message`: Custom message to display when the OS is supported. Default is `None`.

- **Usage:**

  ```python
  @checker.os_check_decorator(supported_os='AlmaLinux', supported_versions=['8.4', '9.2'])
  def my_function():
      print("This function will run only on AlmaLinux versions 8.4 or 9.2.")
  ```

### Utility Functions

#### `parse_yaml(yaml_path)`

Parses the YAML file to get the supported OS and versions.

- **Parameters:**
  - `yaml_path`: Path to the YAML file to parse.

- **Returns:**
  - Dictionary containing the supported OS and versions.

- **Usage:**

  ```python
  supported_versions = parse_yaml('supported_versions.yaml')
  ```

#### `get_os_info()`

Fetches the OS information either from `/etc/os-release`, Python `distro` library, or `uname`.

- **Returns:**
  - Dictionary containing OS information like `ID` and `VERSION_ID`.

- **Usage:**

  ```python
  os_info = get_os_info()
  ```

#### `cache_clear()`

Clears the internal cache used for OS checks.

- **Usage:**

  ```python
  checker.cache_clear()
  ```
