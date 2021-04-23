import bpy



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
    bpy.utils.register_class(MissMePanel)


def unregister():
    bpy.utils.unregister_class(MissMePanel)


if __name__ == "__main__":
    register()
