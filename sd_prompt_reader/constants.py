# -*- encoding:utf-8 -*-
__author__ = 'receyuki'
__filename__ = 'constants.py'
__copyright__ = 'Copyright 2023, '
__email__ = 'receyuki@gmail.com'

from importlib import resources
from pathlib import Path

RELEASE_URL = "https://api.github.com/repos/receyuki/stable-diffusion-prompt-reader/releases/latest"
RESOURCE_DIR = str(resources.files("resources"))
SUPPORTED_FORMATS = [".png", ".jpg", ".jpeg", ".webp"]
COLOR_THEME = Path(RESOURCE_DIR, "gray.json")
INFO_FILE = Path(RESOURCE_DIR, "info_24.png")
ERROR_FILE = Path(RESOURCE_DIR, "error_24.png")
WARNING_FILE = Path(RESOURCE_DIR, "warning_24.png")
OK_FILE = Path(RESOURCE_DIR, "check_circle_24.png")
UPDATE_FILE = Path(RESOURCE_DIR, "update_24.png")
DROP_FILE = Path(RESOURCE_DIR, "place_item_48.png")
COPY_FILE_L = Path(RESOURCE_DIR, "content_copy_24.png")
COPY_FILE_S = Path(RESOURCE_DIR, "content_copy_20.png")
CLEAR_FILE = Path(RESOURCE_DIR, "mop_24.png")
DOCUMENT_FILE = Path(RESOURCE_DIR, "description_24.png")
EXPAND_FILE = Path(RESOURCE_DIR, "expand_more_24.png")
EDIT_FILE = Path(RESOURCE_DIR, "edit_24.png")
EDIT_OFF_FILE = Path(RESOURCE_DIR, "edit_off_24.png")
LIGHTBULB_FILE = Path(RESOURCE_DIR, "lightbulb_20.png")
SAVE_FILE = Path(RESOURCE_DIR, "save_24.png")
SORT_FILE = Path(RESOURCE_DIR, "sort_by_alpha_20.png")
ICON_FILE = Path(RESOURCE_DIR, "icon.png")
ICO_FILE = Path(RESOURCE_DIR, "icon.ico")
MESSAGE = {
    "default":          ["Drag and drop your image file into the window"],
    "success":          ["Voilà!"],
    "format_error":     ["No data", "No data detected or unsupported format"],
    "suffix_error":     ["Unsupported format"],
    "clipboard":        ["Copied to clipboard"],
    "update":           ["A new version is available, click here to download"],
    "export":           ["The TXT file has been generated"],
    "alongside":        ["The TXT file has been generated alongside the image"],
    "txt_select":       ["The TXT file has been generated in the selected directory"],
    "remove":           ["A new image file has been generated"],
    "suffix":           ["A new image file with suffix has been generated"],
    "overwrite":        ["A new image file has overwritten the original image"],
    "remove_select":    ["A new image file has been generated in the selected directory"],
}
DEFAULT_GRAY = "#8E8E93"
ACCESSIBLE_GRAY = ("#6C6C70", "#AEAEB2")
TOOLTIP_DELAY = 1.5