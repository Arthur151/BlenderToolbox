import sys
sys.path.append('/Users/hsuehtil/Dropbox/BlenderToolbox2.8')
sys.path.append('/home/hsuehtil/Dropbox/BlenderToolbox2.8')

from include import *
import bpy

outputPath = './results/demo_vertPointCloud.png'

# # init blender
imgRes_x = 1000 # should set to > 2000 for paper figures
imgRes_y = 1000 # should set to > 2000 for paper figures
numSamples = 100 # should set to >1000 for high quality paper images
exposure = 1.8
blenderInit(imgRes_x, imgRes_y, numSamples, exposure)

# # read mesh 
meshPath = './meshes/spot_pt.ply'
location = (-0.3, 0.6, -0.04)
rotation = (90, 0,0)
scale = (1.5,1.5,1.5)
mesh = readPLY(meshPath, location, rotation, scale)

# # draw point cloud
ptColor = (144.0/255, 210.0/255, 236.0/255, 0)
ptSaturation = 1.7
ptBrightness = 0.8
ptSize = 0.012
numPt = len(mesh.data.vertices) # this needs to be the number of vertices for vertex_point_cloud
drawPointCloud(mesh, ptColor, ptSize, numPt, ptSaturation, ptBrightness)

# # set invisible plane (shadow catcher)
groundCenter = (0,0,0)
shadowDarkeness = 0.05
groundSize = 20
invisibleGround(groundCenter, groundSize, shadowDarkeness)

# # set camera
camLocation = (1.9,2,2.2)
lookAtLocation = (0,0,0.5)
focalLength = 45
cam = setCamera(camLocation, lookAtLocation, focalLength)

# # set sunlight
lightAngle = (-15,-34,-155) 
strength = 2
shadowSoftness = 0.1
sun = setLight_sun(lightAngle, strength, shadowSoftness)

# # set ambient light
ambientColor = (0.1,0.1,0.1,1)
setLight_ambient(ambientColor)

# # save blender file
bpy.ops.wm.save_mainfile(filepath='./test.blend')

# # # save rendering
bpy.data.scenes['Scene'].render.filepath = outputPath
bpy.data.scenes['Scene'].camera = cam
bpy.ops.render.render(write_still = True)