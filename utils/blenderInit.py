import bpy

def blenderInit(resolution_x, resolution_y, numSamples = 128, exposure = 1.5):
	# clear all
	bpy.ops.wm.read_homefile()
	bpy.ops.object.select_all(action = 'SELECT')
	bpy.ops.object.delete() 
	# use cycle
	bpy.context.scene.render.engine = 'CYCLES'
	bpy.context.scene.render.resolution_x = resolution_x 
	bpy.context.scene.render.resolution_y = resolution_y 
	bpy.context.scene.cycles.film_transparent = True
	bpy.context.scene.cycles.device = 'GPU'
	bpy.context.scene.cycles.samples = numSamples 
	bpy.context.scene.cycles.film_exposure = exposure