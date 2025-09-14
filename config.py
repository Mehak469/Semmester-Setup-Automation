""" 

Configuration settings for the Semester Setup Automation Tool.

"""
import re
class ConfigSem:
    def __init__(self):
        self.BASE_DIR = "D:\\" #OR It can be Current working directory(os.getcwd()) -->According to the need
        self.SUBFOLDERS = ["Books", "Notes", "Projects", "Assignments"]
        self.INVALID_CHARS = r'[<>:"/\|?*]'

    def safe_name(self, name):
        """Sanitize folder names (avoid invalid chars)."""
        name = name.strip()
        return re.sub(self.INVALID_CHARS, '_', name)
    

# Create global config instance
setup=ConfigSem()
