#
#       A Simple batch Define Projection tool
#       
#       Benjamin Gappa
#       2/4/17
#
#       Adding optional parameter to add files
#       to map document
#       2/8/17
#

# Modules
import arcpy
from arcpy import env

# Inputs
in_folder = arcpy.GetParameterAsText(0)
prj = arcpy.GetParameterAsText(1) # "4326" # Code for WGS 84
add_layer = arcpy.GetParameterAsText(2) # Gets added to Arc Script tool as optional parameter, Boolean type

# Workspace
env.workspace = in_folder
env.overwriteOutput = True
# Map document
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd)[0]

# Counter
i = 0

try:
    # Loop
    for fc in arcpy.ListFeatureClasses():

        i += 1
        # Define Projection
        arcpy.DefineProjection_management(fc, prj)
        arcpy.AddMessage("Projection Defined for " + fc + ".")

        if str(add_layer) == "true":
            # Add the file to map document
            new_layer = arcpy.mapping.Layer(in_folder + "\\" + fc)
            arcpy.mapping.AddLayer(df, new_layer)

    arcpy.AddMessage("Projection Defined for " + str(i) + " shapefiles.")



except:
    # If tool does not execute, do these
    arcpy.AddError("The Define Projection script did not execute properly.")
    arcpy.AddMessage(arcpy.GetMessages())


