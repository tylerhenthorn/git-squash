from importlib.metadata import version, PackageNotFoundError

from .squash import squash_history

try:
    __version__ = version("git-squash")
except PackageNotFoundError:
    __version__ = "0.1.0"

__all__ = ["squash_history"]
