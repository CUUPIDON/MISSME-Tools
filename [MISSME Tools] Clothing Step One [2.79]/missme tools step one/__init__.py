import bpy
 
bl_info = {
    "name": "MISSME Tools: Step One",
    "author": "MISSME12",
    "version": (0, 1),
    "blender": (2, 79, 0),
    "location": "View3D > Tool Shelf > MISSME Tools: Step One",
    "description": "Adds an easy to use button(s) and info to do most of the leg-work for you in clothing content creation.",
    "warning": "This is part one of the add-on. It will only work in versions similar to 2.79. This excludes 2.80 and up.",
    "wiki_url": "https://github.com/MISSME12/MISSME-Tools/wiki",
    "category": "Object",
    }
    
    
import bpy


# load and reload submodules
##################################

import importlib
from . import developer_utils
importlib.reload(developer_utils)
modules = developer_utils.setup_addon_modules(__path__, __name__, "bpy" in locals())



# register
##################################

import traceback

def register():
    try: bpy.utils.register_module(__name__)
    except: traceback.print_exc()

    print("Registered {} with {} modules".format(bl_info["name"], len(modules)))

def unregister():
    try: bpy.utils.unregister_module(__name__)
    except: traceback.print_exc()

    print("Unregistered {}".format(bl_info["name"]))