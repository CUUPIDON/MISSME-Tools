import bpy

def main(context):
    # SELECT REF MESH
    bpy.context.scene.objects.active = bpy.data.objects['REF']


    # SUB MOD REF MESH FOR SMOOTH UV_1 TRANSFER
    bpy.ops.object.modifier_add(type='SUBSURF')
    bpy.context.object.modifiers["Subsurf"].levels = 5
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


def register():
    bpy.utils.register_class(DataTransfer)


def unregister():
    bpy.utils.unregister_class(DataTransfer)


    register()

    # test call
    # bpy.ops.datatransfer.operator()
