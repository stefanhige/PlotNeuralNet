
import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch


# parameters
height = 32#
width1 = 2
width2 = 4
width3 = 6
width4 = 10
width5 = 20

arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),


    # conv
    # relu

    # conv
    # relu
    # Groupnorm or idendity

    # conv
    # relu
    # Groupnorm or idendity

    # conv
    # relu
    # Groupnorm or idendity

    
    
    to_Conv("conv1", "", "$F_1$", offset="(0,0,0)", to="(0,0,0)", height=height, depth=height, width=width1),
    to_ReLu("relu1", offset="(1,0,0)", to="(conv1-east)"),
    
    to_Conv("conv2", "", "$F_2$", offset="(1.5,0,0)", to="(relu1-east)", height=height-2, depth=height-2, width=width2),
    to_ReLu("relu2", offset="(0,0,0)", to="(conv2-east)", height=height-2, depth=height-2, width=1),
    to_Norm("gn2", offset="(0,0,0)", to="(relu2-east)", height=height-2, depth=height-2, width=1),
    
    to_Conv("conv3", "", "$F_3$", offset="(1.5,0,0)", to="(relu2-east)", height=height-2-4, depth=height-2-4, width=width3),
    to_Pool("relu3", offset="(0,0,0)", to="(conv3-east)", height=height-2-4, depth=height-2-4, width=1),
    to_Norm("gn3", offset="(0,0,0)", to="(relu3-east)", height=height-2-4, depth=height-2-4, width=1),
    
    to_Conv("conv4", "", "$F_3$", offset="(1.5,0,0)", to="(relu3-east)", height=height-2-4-4, depth=height-2-4-4, width=width4),
    to_Pool("relu4", offset="(0,0,0)", to="(conv4-east)", height=height-2-4-4, depth=height-2-4-4, width=1),
    to_Norm("gn4", offset="(0,0,0)", to="(relu4-east)", height=height-2-4-4, depth=height-2-4-4, width=1),
    
    to_Conv("conv5", "", "$F_3$", offset="(1.5,0,0)", to="(relu4-east)", height=height-2-4-4, depth=height-2-4-4, width=width5),
    
    # connections
    to_connection("relu1", "conv2"), 
    to_connection("relu2", "conv3"),    
    to_connection("relu3", "conv4"),    
    to_connection("relu4", "conv5"),    
    
    
    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
