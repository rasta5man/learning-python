Graphic application TK-Paint:

Developed in Python, using Tkinter module.

Graphics area is divided into 2 parts:
- left side as a control area with buttons, shape and color selection.
- right side as a workspace.

Controls on the left:
- 3 buttons (colored rectangles, not Button components): Read from file, Save workspace, Delete workspace.
- blue geometric shapes: circle, square, oval, rectangles, triangle.
- coloring buckets, able to change color of objects in workspace.

Working principle of the program:

You can move different geometric objects with mouse from control panel to workspace and create collage.
When mouse button is released, an exact copy of an object will appear on workspace. You can move 
the object inside the workspace. In addition, the user can paint any shape with coloring buckets from control panel. 
Simply drag and drop your selected color to the object on workspace.
To delete the object from the workspace, you just simple move it outside the workspace. Done.
In addition, the user can paint any shape with coloring elements.
In this way, various compositions can be made from offered shapes, which can then be:
 - written to a file so they can be used later
 - read from file

The program works with the text file "shapes.txt", which is empty at the beginning.
Button "Save workspace" overwrites the current contents of the file with information about all geometric figures in the workspace.
"Read from file" button removes all objects in the workspace, then reads the saved composition of the objects from the file 
and place them into the workspace.
