# CryptoLion SDK - Secure License Management

![CryptoLion Logo](./logo.svg)  
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)]()

The CryptoLion SDK provides a comprehensive solution for license management in desktop applications. With both C and Python APIs, it offers seamless integration for generating, validating, and managing software licenses with enterprise-grade security features.

## Key Features

- 🗝️ **License Generation**: Create time-limited licenses with custom durations
- 🔍 **License Validation**: Verify license keys in real-time
- 👥 **User Management**: Create and manage admin and standard users
- 🔒 **Secure Communication**: HTTPS with Basic Authentication
- 🌐 **Cross-Platform**: Supports Windows, macOS, and Linux
- 🐍 **Dual API**: Available in both C and Python

## Installation

### Python SDK
```bash
pip install cryptolion-sdk
```

### C SDK
```bash
git clone https://github.com/cryptolion/sdk.git
cd sdk/c
make
sudo make install
```

## Quick Start

### Python Example
```python
from cryptolion import create_license, check_license

# Create a new license
license = create_license("admin", "securepass", 365)
print(f"Created license: {license['license_key']}")

# Validate license
validated = check_license(license['license_key'])
if validated['is_active']:
    print("License is active!")
```

### C Example
```c
#include <cryptolion.h>

int main() {
    // Create license
    License lic = create_license("admin", "securepass", 365, 0);
    printf("Created license: %s\n", lic.license_key);
    
    // Validate license
    License validated = check_license(lic.license_key);
    if(validated.is_active) {
        printf("License is active!\n");
    }
    
    // Clean up
    free_license(&lic);
    free_license(&validated);
    return 0;
}
```

## Documentation

📚 Comprehensive documentation is available at:  
[https://cryptolion.github.io/sdk/docs](https://cryptolion.github.io/sdk/docs)

Key documentation sections include:
- API Reference for both C and Python
- Security Best Practices
- Error Handling Guide
- Platform-Specific Notes
- Advanced Usage Examples

## Building from Source

### Prerequisites
- libcurl
- cJSON
- Python 3.6+ (for Python bindings)
- GCC or Clang

### Build Commands
```bash
# Clone repository
git clone https://github.com/cryptolion/sdk.git
cd sdk

# Build C library
make -C c

# Build Python package
make package

# Install Python package
cd python
pip install dist/*.whl
```

## Supported Platforms

| Platform      | Architecture | C Support | Python Support |
|---------------|--------------|-----------|----------------|
| Windows       | x86-64       | ✅         | ✅             |
| Linux         | x86-64       | ✅         | ✅             |

## Contributing

We welcome contributions! Please see our [Contribution Guidelines](CONTRIBUTING.md) for details on how to contribute to the project.

## Security

This repository includes **known security issues**, do not use in production. For education purposes only.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**CryptoLion** © 2025 - Secure Software Licensing Solutions
