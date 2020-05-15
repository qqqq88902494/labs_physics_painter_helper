# _*_ coding:UTF-8 _*_
#by vfxmstc https://github.com/qqqq88902494
#email:410386656@qq.com
#houdini18 labs plugin
#just select the physical painter and run it!

import hou
pathNodefbx = hou.ui.selectNode()
nodelist = hou.node(pathNodefbx).allSubChildren()
null_list = []
outnodelist = []
for child in nodelist:
    if (child.type().name() == 'null'):
        outnodelist = child.outputs()
        if(len(outnodelist) == 0 ):
            null_list.append(child)
#paintNodefbx = hou.ui.selectNode()           
physical_paint_node = hou.selectedNodes()[0]
if (str(physical_paint_node.type().name())=='labs::physics_painter'):
    physical_paint_node.parm('folder2').set(len(null_list))
    n = 1
    for node in null_list:
        physical_paint_node.parm('objObjPath'+str(n)).set(str(node.path()))
        n = n+1