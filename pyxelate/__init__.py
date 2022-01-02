__version__ = "2.1.0"

__short_description__ = (
    "Downsample images to 8-bit pixel art.",
)
__license__ = "MIT"
__author__ = "Richard Nagyfi"
__author_email__ = "sedthh@gmail.com"
__github_username__ = "sedthh"

from .pal import Pal
from .pyx import Pyx
from .vid import images_to_parts, parts_to_images
