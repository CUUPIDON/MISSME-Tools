import bpy

bl_info = {
    "name": "MISSME Tools: Step Two",
    "author": "MISSME12",
    "version": (0, 1),
    "blender": (2, 70, 0),
    "location": "View3D > Tool Shelf > MISSME Tools: Step Two",
    "description": "Adds an easy to use button(s) and info to do most of the leg-work for you in clothing content creation.",
    "warning": "This is part two of the add-on. It will only work in versions similar to 2.70. This excludes 2.79 and up.",
    "wiki_url": "",
    "category": "Object",
    }


def main(context):
    # TAKE OBJECTS OUT OF MODES
    bpy.context.active_object.mode   # = 'OBJECT'
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.context.active_object.mode   # = 'EDIT'


    # SELECT OBJECTS FOR WEIGHT TRANSFER
    bpy.ops.object.select_all(action='DESELECT')
    for o in bpy.data.objects:
        # Check for given object names
        if o.name in ("REF","s4studio_mesh_1"):
            o.select = True
            
            
    # TRANSFER WEIGHTS
    bpy.ops.paint.weight_paint_toggle()
    bpy.ops.object.vertex_group_transfer_weight()


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

class MissMePanel(bpy.types.Panel):
    """Creates a Panel in the Tool Shelf"""
    bl_label = "MISSME Tools: Step Two"
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

        
#Weight & Vertex Transfer 2.70
        row = layout.row()
        row = layout.row()
        row = layout.row()
        row = layout.row()       
        row = layout.row()
        row = layout.row()  
        row.label(text="Transfers both weights and vertex paints to your mesh:")
        row = layout.row()
        row.operator("myops.wegvertra_operator", text='Weight & Vertex Transfer')
        
        
#Finished?                  
        row = layout.row()
        row = layout.row()
        row = layout.row()
        row = layout.row()       
        row = layout.row()          
        row = layout.row()
        row.label(text="Step two done!", icon= 'INFO') 
        row = layout.row()
        row.label(text="Check to make sure the weight and vertex paints are there!", icon= 'ERROR') 
        row = layout.row()
        row.label(text="Continue to refine your mesh, making sure there are no issues.", icon= 'INFO')  
        row = layout.row()            
        row.label(text="When you're sure it's perfect, you may import it into Sims 4 Studio!", icon= 'INFO')      
   
        
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
    bpy.utils.register_class(weightvertex)
    bpy.utils.register_class(MissMePanel)

def unregister():
    bpy.utils.unregister_class(weightvertex)
    bpy.utils.unregister_class(MissMePanel)


if __name__ == "__main__":
    register()

    # test call
    # bpy.ops.myops.wegvertra_operator()
