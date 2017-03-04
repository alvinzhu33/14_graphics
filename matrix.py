import math

def transpose(old):
    new = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]];
    for r in range(4):
        for c in range(4):
            new = old[c][r];

def make_translate( x, y, z ):
    trans = [[1, 0, 0, x], [0, 1, 0, y], [0, 0, 1, z], [0, 0, 0, 1]]
    return trans;

def make_scale( x, y, z ):
    scale = [[x, 0, 0, 0], [0, y, 0, 0], [0, 0, z, 0], [0, 0, 0, 1]]
    return scale;

def make_rotX( theta ):
    rad = math.radians(theta);
    sin = math.sin(rad);
    cos = math.cos(rad);
    rot = [[1, 0, 0, 0], [0, cos, -sin, 0], [0, sin, cos, 0], [0, 0, 0, 1]]
    return rot;

def make_rotY( theta ):
    rad = math.radians(theta);
    sin = math.sin(rad);
    cos = math.cos(rad);
    rot = [[cos, 0, sin, 0, 0], [0, 1, 0, 0], [-sin, 0, cos, 0], [0, 0, 0, 1]]
    return rot;

def make_rotZ( theta ):
    rad = math.radians(theta);
    sin = int(math.sin(rad));
    cos = int(math.cos(rad));
    rot = [[cos, -sin, 0, 0], [sin, cos, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]];
    return rot;

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

def scalar_mult( matrix, s ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            matrix[c][r]*= s

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):

    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]

        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
