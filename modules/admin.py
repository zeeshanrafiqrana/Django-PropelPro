# Import necessary modules
from importlib import import_module
from pathlib import Path
from django.conf import settings

# WARNING: Do not remove or change this code snippet; it's essential for functionality

try:
    # Define the directory where the modules are located
    modules_dir = f"{settings.BASE_DIR}/modules/"

    # Recursively search for 'admin.py' files within the modules directory
    admins = list(Path(modules_dir).rglob('admin.py'))

    # Iterate through the 'admin.py' files
    for admin in admins:
        # Extract the module name from the path
        module_name, _ = admin.as_posix().split('/')[-2:]

        # Check if the module name is not 'modules'
        if not module_name == "modules":
            # Dynamically import the 'admin' module for the current module
            module = import_module(f"modules.{module_name}.admin")

            # Import all items from the 'module' (admin module) into the current namespace
            from module import *  # noqa
except (ImportError, IndexError):
    pass
