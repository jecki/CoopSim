# Compatibility

"""Provides code snipplets for ompatibility with older python versions.
"""

try:
    set
except NameError:
    try:
        import sets
    except ImportError:
        import altsets as sets
    set = sets.Set

# had to be commented out in order to allow Python 3.0 compatibility
# sacrifices some backward compatibility (python 2.1?) though
#try:
#    True, False
#except NameError:
#    True, False = (0==0, 0!=0)

try:
    object
except NameError:
    class object:
        pass

import sys
if sys.platform[:4] == "java" and sys.version[:3] == "2.2":
    class object: # avoid problems with copy.deepcopy
        pass


def GetDriver(check=["qtGfx", "gtkGfx", "wxGfx", "tkGfx", "awtGfx"]):
    """Get any available Gfx Driver."""
    for wish in check:
        if wish == "qtGfx":
            try:
                import qtGfx
                return qtGfx
            except ImportError:
                try:
                    from . import qtGfx
                    return qtGfx
                except ImportError:
                    pass
        elif wish == "gtkGfx":
            try:
                import gtkGfx
                return gtkGfx
            except ImportError:
                try:
                    from . import gtkGfx
                    return gtkGfx
                except ImportError:
                    pass
        elif wish == "wxGfx":
            try:
                import wxGfx
                return wxGfx
            except ImportError:
                pass
        elif wish == "tkGfx":
            try:
                import tkGfx
                print("WARNING: tk is not fully supported by PyPlotter.\n"+\
                      "Use of wxPython or PyGTK2 is highly recoomended!\n\n")
                return tkGfx
            except ImportError:
                try:
                    from . import tkGfx
                    return tkGfx
                except ImportError:
                    pass
        elif wish == "awtGfx":
            try:
                import awtGfx
                return awtGfx
            except ImportError:
                pass
    raise ImportError("Could not find a graphics drivers for PyPlotter!\n\n")
