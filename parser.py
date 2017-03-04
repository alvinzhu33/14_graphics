from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix -
	 scale: create a scale matrix,
	    then multiply the transform matrix by the scale matrix -
	    takes 3 arguments (sx, sy, sz)
	 translate: create a translation matrix,
	    then multiply the transform matrix by the translation matrix -
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 yrotate: create an y-axis rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 1 argument (theta)
	 zrotate: create an z-axis rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 1 argument (theta)
	 apply: apply the current transformation matrix to the
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    fileD = open(fname,'r');
    lines = fileD.read().split("\n");
    x = 0;
    print("length: " + str(len(lines)) + "\n")
    while x<len(lines)-1:
        line = lines[x]
        print(str(x) + ": " + line)
        if line in ["display", "apply", "ident"]:
            if line == "ident":
                ident(transform);
            if line == "apply":
                points = (transform);
            if line == "display":
                draw_lines(points, screen, color);
                display(screen);

            x+=1;
        else:
            args = lines[x+1].split(" ");
            print(str(args) + "\n")

            if line == "line":
                add_edge(points, int(args[0]), int(args[1]), int(args[2]), int(args[3]), int(args[4]), int(args[5]));
                #transform = points
            if line == "scale":
                scaler = make_scale(args[0], args[1], args[2]);
                transform = matrix_mult(scaler, transform);
            if line == "move":
                trans = make_translate(int(args[0]), int(args[1]), int(args[2]));
                transform = matrix_mult(trans, transform);
            if line == "rotate":
                if args[0] == "x":
                    rot = make_rotX(float(args[1]));
                if args[0] == "y":
                    rot = make_rotY(float(args[1]));
                if args[0] == "z":
                    rot = make_rotZ(float(args[1]));
                transform = matrix_mult(rot, transform);
            if line == "save":
                display(points);
                save_extension(points, args[0]);
            #transform = points
            x+=2;

        print_matrix(points)
        print("---")
        print_matrix(transform)
        print("_____")
