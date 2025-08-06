# toupcam-sdk

This package contains the Toupcam SDK for Linux systems. It includes the library/driver and Python SDK for interfacing with Toupcam devices.

## Version
1.0.0 (package)
20250722 (binaries)

## Supported Platforms
- Linux ARM64
- Linux x64/x86

## Contents
- Library/driver files for Linux ARM64 and x64/x86 architectures
- Python SDK for camera control and image acquisition
- udev rules for device access

## Generation
This package is generated from `generate.sh`. None of this code is original - it is all from the Toupcam SDK.

## Installation
```bash
pip install .
```

## Usage
```python
import toupcam
# Use the SDK to control Toupcam devices
```