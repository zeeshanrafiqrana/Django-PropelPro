# Import necessary modules
from pathlib import Path
from django.conf import settings
from django.urls import path, include
from django.db.utils import ProgrammingError

# Initialize an empty list to hold URL patterns
urlpatterns = []

# This code snippet is designed to dynamically include URL patterns from Django modules.
# It should not be removed or modified for certain functionalities.

# Try to include URL patterns from dynamically discovered modules.
try:
    # Define the directory where the modules are located
    modules_dir = f"{settings.BASE_DIR}/modules/"

    # Recursively search for 'urls.py' files within the modules directory
    urls = Path(modules_dir).rglob("urls.py")

    # Iterate through the discovered 'urls.py' files
    for url in urls:
        # Extract the module name from the path
        module_name, _ = url.as_posix().split("/")[-2:]

        # Check if the module name is not 'modules'
        if not module_name == "modules":
            # Convert module_name to a URL-friendly format
            module_url = module_name.replace("_", "-")

            # Include the module's URL patterns using the 'include' function
            urlpatterns += [
                path(f"{module_url}/", include(f"modules.{module_name}.urls"))
            ]
except (ImportError, IndexError, ProgrammingError):
    # Handle exceptions that may occur during module discovery
    pass
