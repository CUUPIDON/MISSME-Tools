import bpy


def main(context):
    # TAKE OBJECTS OUT OF MODES
    bpy.context.active_object.mode   # = 'OBJECT'
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.context.active_object.mode   # = 'EDIT'


    # SELECT OBJECTS FOR WEIGHT TRANSFER
    bpy.ops.object.select_all(action='DESELECT')

    for o in bpy.data.objects:
        if o.name in ("s4studio_mesh_1"):
            o.select = True

    object = bpy.data.objects['s4studio_mesh_1']
    bpy.context.scene.objects.active = object

    for o in bpy.data.objects:
        if o.name in ("REF", "s4studio_mesh_1"):
            o.select = True
            
            
    # TRANSFER WEIGHTS
    bpy.ops.paint.weight_paint_toggle()
    bpy.ops.object.data_transfer(use_reverse_transfer=True, data_type='VGROUP_WEIGHTS')
    bpy.ops.object.data_transfer(use_reverse_transfer=True, data_type='VGROUP_WEIGHTS', layers_select_src='NAME')
    bpy.ops.object.data_transfer(use_reverse_transfer=True, data_type='VGROUP_WEIGHTS', layers_select_src='NAME', layers_select_dst='ALL')
    bpy.ops.object.vertex_group_clean()
    bpy.ops.object.vertex_group_clean(group_select_mode='ALL')



    # TAKE OBJECTS OUT OF MODES
    bpy.context.active_object.mode   # = 'OBJECT'
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.context.active_object.mode   # = 'EDIT'


    # SELECT MD MESH FOR VERTEX COLORS
    bpy.context.scene.objects.active = bpy.data.objects['s4studio_mesh_1']


    # GIVE VERTEX COLORS
    bpy.ops.paint.vertex_paint_toggle()
    bpy.data.brushes["Draw"].color[0] = 0
    bpy.data.brushes["Draw"].color[2] = 0
    bpy.data.brushes["Draw"].color[1] = 1
    bpy.data.brushes["Draw"].color = (0, 1, 0)
    bpy.ops.paint.vertex_color_set()
    bpy.ops.paint.vertex_paint_toggle()



    # TAKE OBJECTS OUT OF MODES
    bpy.context.active_object.mode   # = 'OBJECT'
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.context.active_object.mode   # = 'EDIT'


    # DELETE REF MESH
    bpy.ops.object.select_all(action='DESELECT')
    for o in bpy.data.objects:
        # Check for given object names
        if o.name in ("REF"):
            o.select = True
    bpy.ops.object.delete()


class weightvertex(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "myops.wegvertra_operator"
    bl_label = "Simple Object Operator"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(weightvertex)


def unregister():
    bpy.utils.unregister_class(weightvertex)


if __name__ == "__main__":
    register()

    # test call
    # bpy.ops.myops.wegvertra_operator()
