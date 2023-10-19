# Import necessary modules
import importlib
import json
from pathlib import Path

# Define the path to the global options JSON file
GLOBAL_OPTIONS_FILE_PATH = f"{Path.cwd()}/modules/options.json"


# Define a function to retrieve module-specific options
def get_options(module_slug, option_key):
    # Open and read the global options JSON file
    with open(GLOBAL_OPTIONS_FILE_PATH, "r") as f:
        module_options = json.loads(f.read())

    # Search for the specified module's options based on its slug
    option_value = [
        module.get(option_key)
        for module in module_options["module_options"]
        if module.get("slug") == module_slug
    ]

    # Get the default value for the option by dynamically importing the module
    default_value = getattr(
        importlib.import_module(f"modules.{module_slug}.options"), option_key
    )

    # Return the option value if found, otherwise return the default value
    return option_value[0] if option_value else default_value
