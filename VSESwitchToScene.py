# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


import bpy


bl_info = {
    "name": "VSE Switch To Scene",
    "description": "Assists in using Scene strips in the Blender VSE by providing a way to quickly switch to and from editing them.",
    "author": "Hudson Barkley (Snu/snuq/Aritodo)",
    "version": (0, 9, 0),
    "blender": (2, 80, 0),
    "location": "Sequencer Panel; Sequencer, 3D View, Compositor headers; Sequencer Shift-TAB Shortcut",
    "wiki_url": "https://github.com/snuq/VSESwitchToScene",
    "tracker_url": "https://github.com/snuq/VSESwitchToScene/issues",
    "category": "Sequencer"
}


def get_active(context):
    sequencer = context.scene.sequence_editor
    if sequencer:
        active = sequencer.active_strip
        if active:
            return active
    return None


def draw_switch_to_header(self, context):
    layout = self.layout
    scene_name = context.scene.vsests.scene
    if scene_name and scene_name in bpy.data.scenes:
        layout.operator("vsests.switch_back", text="Switch Back To: "+scene_name)


class VSESTSWorkspaceMenu(bpy.types.Menu):
    bl_idname = 'VSESTS_MT_workspace_menu'
    bl_label = 'List Of Workspaces'

    def draw(self, context):
        layout = self.layout
        for workspace in bpy.data.workspaces:
            layout.operator('vsests.select_workspace', text=workspace.name).name = workspace.name


class VSESTSWorkspaceSet(bpy.types.Operator):
    bl_idname = 'vsests.select_workspace'
    bl_label = "Select Workspace"

    name: bpy.props.StringProperty()

    def execute(self, context):
        for workspace in bpy.data.workspaces:
            if workspace.name == self.name:
                context.scene.vsests.workspace = self.name
                return {'FINISHED'}
        return {'CANCELLED'}


class VSESTSSwitch(bpy.types.Operator):
    bl_idname = 'vsests.switch'
    bl_label = 'Switch To Scene'
    bl_description = 'Switch To Scene'

    def execute(self, context):
        scene_name = context.scene.vsests.scene
        if scene_name and scene_name in bpy.data.scenes:
            bpy.ops.vsests.switch_back()
        else:
            bpy.ops.vsests.switch_to()
        return {'FINISHED'}


class VSESTSSwitchTo(bpy.types.Operator):
    bl_idname = 'vsests.switch_to'
    bl_label = 'Switch To Scene'
    bl_description = 'Switch To Scene'

    def execute(self, context):
        active = get_active(context)
        if active and active.type != 'SCENE':
            return {'CANCELLED'}
        scene = active.scene
        if context.scene.vsests.workspace in bpy.data.workspaces:
            workspace = bpy.data.workspaces[context.scene.vsests.workspace]
        else:
            workspace = context.workspace
        scene.vsests.scene = context.scene.name
        scene.vsests.workspace = context.workspace.name
        context.window.workspace = workspace
        context.window.scene = scene
        return {'FINISHED'}


class VSESTSSwitchBack(bpy.types.Operator):
    bl_idname = 'vsests.switch_back'
    bl_label = 'Switch To Scene'
    bl_description = 'Switch To Scene'

    def execute(self, context):
        if context.scene.vsests.scene in bpy.data.scenes:
            scene = bpy.data.scenes[context.scene.vsests.scene]
        else:
            return {'CANCELLED'}
        if context.scene.vsests.workspace in bpy.data.workspaces:
            workspace = bpy.data.workspaces[context.scene.vsests.workspace]
        else:
            workspace = context.workspace
        context.window.workspace = workspace
        context.window.scene = scene
        return {'FINISHED'}


class VSESTS_PT_VSEPanel(bpy.types.Panel):
    bl_label = "VSE Switch To Scene"
    bl_space_type = 'SEQUENCE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'Strip'

    @classmethod
    def poll(cls, context):
        active = get_active(context)
        if active and active.type == 'SCENE':
            return True
        return False

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Workspace:")
        row.menu('VSESTS_MT_workspace_menu', text=context.scene.vsests.workspace)
        row = layout.row()
        row.operator("vsests.switch_to")


class VSESTSSettings(bpy.types.PropertyGroup):
    workspace: bpy.props.StringProperty(
        name="Workspace To Switch To",
        default='')
    scene: bpy.props.StringProperty(
        name="Scene To Switch To",
        default='')


classes = [VSESTSSwitchTo, VSESTSSwitchBack, VSESTS_PT_VSEPanel, VSESTSWorkspaceSet, VSESTSWorkspaceMenu,
           VSESTSSettings, VSESTSSwitch]


def register():
    #Register classes
    for cls in classes:
        bpy.utils.register_class(cls)

    #Add headers
    bpy.types.SEQUENCER_HT_header.append(draw_switch_to_header)
    bpy.types.VIEW3D_HT_header.append(draw_switch_to_header)
    bpy.types.NODE_HT_header.append(draw_switch_to_header)

    #Group properties
    bpy.types.Scene.vsests = bpy.props.PointerProperty(type=VSESTSSettings)

    #Register shortcut
    keymap = bpy.context.window_manager.keyconfigs.addon.keymaps.new(name='Sequencer', space_type='SEQUENCE_EDITOR', region_type='WINDOW')
    keymapitems = keymap.keymap_items
    keymapitems.new('vsests.switch', 'TAB', 'PRESS', shift=True)


def unregister():
    #Remove headers
    bpy.types.SEQUENCER_HT_header.remove(draw_switch_to_header)
    bpy.types.VIEW3D_HT_header.remove(draw_switch_to_header)
    bpy.types.NODE_HT_header.remove(draw_switch_to_header)

    #Unregister classes
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
