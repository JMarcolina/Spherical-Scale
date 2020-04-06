import bpy

# Set distance from center to scale around. Vertices inside this radius will scale inward, and vertices outside this radius will scale outward.
myRadius = 1.5
# Set amount to scale.
scaleAmount = 2

# Set a pointer to the currently selected object.
myObject = bpy.context.active_object

# Define a function to measure the distance between two points.
def measure (first, second):
    locx = second[0] - first[0]
    locy = second[1] - first[1]
    locz = second[2] - first[2]
    distance = sqrt((locx)**2 + (locy)**2 + (locz)**2)
    return distance

# Set a variable for the selected object's center
myCenter = myObject.location

# Iterate through all the object's vertices, and scale based on their distance from center.
for myVert in myObject.data.vertices:
    if measure(myVert, myCenter) > myRadius:
        myVert.co.x *= scaleAmount
        myVert.co.y *= scaleAmount
        myVert.co.z *= scaleAmount
    elif measure(myVert, myCenter) < myRadius:
        myVert.co.x /= scaleAmount
        myVert.co.y /= scaleAmount
        myVert.co.z /= scaleAmount
    else: nothing
