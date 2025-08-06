import os
import sys
import platform
import atexit
from pathlib import Path

# Detect architecture and create symbolic link
# (to resolve binary path which is hardcoded to same dir as toupcam.py)
def setup_library_link():
    """Create symbolic link to the appropriate library file based on architecture."""
    current_dir = Path(__file__).parent
    lib_dir = current_dir / "lib"
    
    # Determine architecture
    arch = platform.machine()
    if arch == "x86_64":
        arch_dir = "x64"
    elif arch == "i686" or arch == "i386":
        arch_dir = "x86"
    elif arch == "aarch64" or arch == "arm64":
        arch_dir = "arm64"
    else:
        # Fallback to x64 for unknown architectures
        arch_dir = "x64"
    
    # Paths
    source_lib = lib_dir / arch_dir / "libtoupcam.so"
    target_lib = current_dir / "libtoupcam.so"
    
    # Check if source library exists
    if not source_lib.exists():
        raise FileNotFoundError(f"Library not found at {source_lib}")
    
    # Check if link already exists and points to the correct source
    link_exists = target_lib.exists() and target_lib.is_symlink()
    if link_exists:
        try:
            # Check if the existing link points to the correct source
            if target_lib.resolve() == source_lib.resolve():
                # Link already exists and points to correct source, don't create or cleanup
                setup_library_link.target_path = None
                return target_lib
        except (OSError, RuntimeError):
            # Link is broken or invalid, remove it
            target_lib.unlink()
            link_exists = False
    
    # Remove existing link if it exists but points to wrong location
    if link_exists:
        target_lib.unlink()
    
    # Create symbolic link
    target_lib.symlink_to(source_lib)
    
    # Store the target path for cleanup (only if we created it)
    setup_library_link.target_path = target_lib
    
    return target_lib

def cleanup_library_link():
    """Remove the symbolic link on program shutdown."""
    if hasattr(setup_library_link, 'target_path') and setup_library_link.target_path is not None:
        try:
            if setup_library_link.target_path.exists() and setup_library_link.target_path.is_symlink():
                setup_library_link.target_path.unlink()
        except (OSError, FileNotFoundError):
            pass  # Ignore errors during cleanup

# Setup library link
setup_library_link()

# Register cleanup function
atexit.register(cleanup_library_link)

# Import the toupcam module
from . import toupcam
