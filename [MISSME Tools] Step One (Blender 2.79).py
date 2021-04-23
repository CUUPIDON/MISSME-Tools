import bpy

bl_info = {
    "name": "MISSME Tools: Step One",
    "author": "MISSME12",
    "version": (0, 1),
    "blender": (2, 79, 0),
    "location": "View3D > Tool Shelf > MISSME Tools: Step One",
    "description": "Adds an easy to use button(s) and info to do most of the leg-work for you in clothing content creation.",
    "warning": "This is part one of the add-on. It will only work in versions similar to 2.79. This excludes 2.80 and up.",
    "wiki_url": "",
    "category": "Object",}

def main(context):
    # SELECT REF MESH
    bpy.context.scene.objects.active = bpy.data.objects['REF']


    # SUB MOD REF MESH FOR SMOOTH UV_1 TRANSFER
    bpy.ops.object.modifier_add(type='SUBSURF')
    bpy.context.object.modifiers["Subsurf"].levels = 3
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Subsurf")


    # change the 'levels' number depending on the capability of your computer 
    # the higher it is, the longer it'll take for the script to run
    # DO NOT set this number too high, it could lock up/crash Blender


    # RETURN TO MD MESH
    bpy.context.scene.objects.active = bpy.data.objects['s4studio_mesh_1']


    # APPLY DATA TRANSFER MOD TO MD MESH
    bpy.ops.object.modifier_add(type='DATA_TRANSFER')
    bpy.context.object.modifiers["DataTransfer"].use_poly_data = True
    bpy.context.object.modifiers["DataTransfer"].use_loop_data = True
    bpy.context.object.modifiers["DataTransfer"].data_types_loops = {'UV'}
    bpy.ops.object.editmode_toggle()
    bpy.context.object.modifiers["DataTransfer"].object = bpy.data.objects["REF"]
    bpy.context.object.modifiers["DataTransfer"].layers_uv_select_src = 'uv_1'
    bpy.context.object.modifiers["DataTransfer"].layers_uv_select_dst = 'uv_1'
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="DataTransfer")


    #Step One Done
    #Save your Blend file and open Blender 2.70 then open script "Step Two_Weight Transfer"


class DataTransfer(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "datatransfer.operator"
    bl_label = "Data Transfer from REF mesh to your new mesh."


    def execute(self, context):
        main(context)
        return {'FINISHED'}


class MissMePanel(bpy.types.Panel):
    """Creates a Panel in the Tool Shelf"""
    bl_label = "MISSME Tools: Step One"
    bl_idname = "OBJECT_PT_missme"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "MISSME"

    def draw(self, context):
        layout = self.layout

        obj = context.object
        
        row = layout.row()
        row.label(text="A PY script that does most of the hard-work for you.", icon= 'INFO') 
        row = layout.row()
        row.label(text="Arrange the UVs for your MD Mesh and rename the UVMap to UV_0 then join it to s4studio_mesh_1.", icon= 'INFO') 
        row = layout.row()
        row.label(text="Make sure you import your reference mesh and name it REF so the script can find the object it needs.", icon= 'ERROR')
        row = layout.row()
        row.label(text="When you've done that, click Run Script at the bottom." , icon= 'INFO')

#Data Transfer
        row = layout.row()
        row = layout.row()
        row = layout.row()
        row = layout.row()
        row = layout.row()
        row = layout.row()
        row.label(text="Smooth and Transfers UV_1 to your mesh:")

        row = layout.row()
        row.operator("datatransfer.operator", text='Data Transfer')
        
#Finished?                  
        row = layout.row()
        row = layout.row()
        row = layout.row()
        row = layout.row()       
        row = layout.row()          
        row = layout.row()
        row.label(text="Step one done!", icon= 'INFO') 
        row = layout.row()
        row.label(text="Check and make sure the UV_1 was properly transferred!", icon= 'ERROR') 
        row = layout.row()            
        row.label(text="When you're ready, open Blender 2.70 and continue to step two.", icon= 'INFO')
        
#Patreon Button
        row = layout.row()
        row = layout.row()
        row = layout.row()
        row = layout.row()
        row = layout.row()
        row = layout.row()
        row.label(text="If you like my work, consider supporting me on Patreon:", icon='SOLO_ON')
        
        row = layout.row()
        row.operator('wm.url_open', text='MISSME').url='https://www.patreon.com/missme'


def register():
    bpy.utils.register_class(DataTransfer)
    bpy.utils.register_class(MissMePanel)

def unregister():
    bpy.utils.unregister_class(DataTransfer)
    bpy.utils.unregister_class(MissMePanel)

if __name__ == "__main__":
    register()

    # test call
    # bpy.ops.datatransfer.operator()
