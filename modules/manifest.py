# Import the pathlib module for working with file paths
from pathlib import Path

# Define the name of the modules package and the path to the modules directory
MODULES_PACKAGE_NAME = "modules"
MODULES_DIR = f"{Path.cwd()}/{MODULES_PACKAGE_NAME}/"

# Recursively search for 'apps.py' files within the modules directory
APPS = Path(MODULES_DIR).rglob("apps.py")


# Define a function to get a list of module names
def get_modules():
    try:
        # Initialize an empty list to store module names
        modules = []

        # Define the separator for Python package names (dot)
        python_package_separator = "."

        # Iterate through the 'apps.py' files found in the modules directory
        for app in APPS:
            # Convert the path to a Python package-style name
            app_name = app.as_posix().replace(MODULES_DIR, f"{MODULES_PACKAGE_NAME}/")
            app_name = python_package_separator.join(app_name.split("/")[:-1])

            # Add the module name to the list
            modules.append(app_name)

        # Return the list of module names
        return modules
    except (ImportError, IndexError):
        pass
