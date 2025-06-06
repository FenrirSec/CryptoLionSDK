import ctypes
import os
import sys
from ctypes import Structure, c_char_p, c_int, POINTER, byref

# Define the License structure for Python
class License(Structure):
    _fields_ = [
        ("license_key", c_char_p),
        ("created_at", c_char_p),
        ("expires_at", c_char_p),
        ("is_active", c_int)
    ]

# Load the shared library
def load_library():
    lib_name = None
    # Determine shared library extension
    if sys.platform.startswith('win'):
        lib_name = "LibLion64.dll"
    elif sys.platform == 'darwin':
        lib_name = "LibLion.dylib"
    else:
        lib_name = "LibLion.so"
    
    # Try to load from current directory and system paths
    try:
        return ctypes.CDLL(lib_name, winmode=0)
    except OSError as e:
        print("lib_name", lib_name)
        raise e
        # Try relative path
        lib_path = os.path.join(os.path.dirname(__file__), lib_name)
        return ctypes.CDLL(lib_path)

lib = load_library()

# Set function prototypes

lib.create_license.argtypes = [c_char_p, c_char_p, c_int, c_int]
lib.create_license.restype = License

lib.check_license.argtypes = [c_char_p]
lib.check_license.restype = License

lib.create_user.argtypes = [c_char_p, c_char_p, c_char_p, c_char_p, c_int]
lib.create_user.restype = c_int

lib.free_license.argtypes = [POINTER(License)]
lib.free_license.restype = None

# Pythonic wrapper functions
def set_base_url(url: str):
    """Set the base URL for the API"""
    lib.set_base_url(url.encode('utf-8'))

def create_license(username: str, password: str, 
                 duration_days: int, user_id: int = 0) -> dict:
    """
    Create a new license (Admin only)
    
    Args:
        username: Admin username
        password: Admin password
        duration_days: License duration in days
        user_id: Optional user ID to associate
    
    Returns:
        Dictionary with license details
    """
    lic = lib.create_license(
        username.encode('utf-8'),
        password.encode('utf-8'),
        duration_days,
        user_id
    )
    
    result = {
        'license_key': lic.license_key.decode() if lic.license_key else None,
        'created_at': lic.created_at.decode() if lic.created_at else None,
        'expires_at': lic.expires_at.decode() if lic.expires_at else None,
        'is_active': bool(lic.is_active)
    }
    
    # Free C memory
    lib.free_license(byref(lic))
    return result

def check_license(license_key: str) -> dict:
    """
    Check license validity
    
    Args:
        license_key: License key to validate
    
    Returns:
        Dictionary with license details
    """
    lic = lib.check_license(license_key.encode('utf-8'))
    result = {
        'license_key': lic.license_key.decode() if lic.license_key else None,
        'created_at': lic.created_at.decode() if lic.created_at else None,
        'expires_at': lic.expires_at.decode() if lic.expires_at else None,
        'is_active': bool(lic.is_active)
    }
    
    # Free C memory
    lib.free_license(byref(lic))
    return result

def create_user(admin_user: str, admin_pass: str, 
              username: str, password: str, is_admin: bool = False) -> bool:
    """
    Create a new user (Admin only)
    
    Args:
        admin_user: Admin username
        admin_pass: Admin password
        username: New username
        password: New password
        is_admin: Whether new user should be admin
    
    Returns:
        True if successful, False otherwise
    """
    return bool(lib.create_user(
        admin_user.encode('utf-8'),
        admin_pass.encode('utf-8'),
        username.encode('utf-8'),
        password.encode('utf-8'),
        int(is_admin)
    ))

print(create_license("admin", "admin123", 32, 0))
print(check_license("C66B10093A6F4D488A0C5085C5E0D61F"))
