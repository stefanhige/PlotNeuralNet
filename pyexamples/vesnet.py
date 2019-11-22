
import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch


# parameters
height0 = 32#
width1 = 2   
height1 = height0 - 2

width2 = 4
height2 = height1 - 4

width3 = 6
height3 = height2 - 4 

width4 = 10
height4 = height3 - 2

width5 = 20
height5 = height4 - 0
offs = "2"

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

    
    to_Inp("input", "", "Input", offset="(-0.4,0,0)", to="(-2,0,0)", height=height0, depth=height0, width=2),
    to_input( 'vessels.png', to="(-2,0,0)", width=6.4, height=6.4),
    
    to_ReLu("relu1", offset="(1,0,0)", to="(0,0,0)", height=height1, depth=height1, width=1),
    to_Conv("conv1", "", "$F_1$", offset="(0,0,0)", to="(relu1-east)", height=height1, depth=height1, width=width1),
    
    to_ReLu("relu2", offset="(" + offs +",0,0)", to="(conv1-east)", height=height2, depth=height2, width=1),
    to_Norm("gn2", offset="(0,0,0)", to="(relu2-east)", height=height2, depth=height2, width=1),
    to_Conv("conv2", "", "$F_2$", offset="(0,0,0)", to="(gn2-east)", height=height2, depth=height2, width=width2),
    
    to_Pool("relu3", offset="(" + offs +",0,0)", to="(conv2-east)", height=height3, depth=height3, width=1),
    to_Norm("gn3", offset="(0,0,0)", to="(relu3-east)", height=height3, depth=height3, width=1),
    to_Conv("conv3", "", "$F_3$", offset="(0,0,0)", to="(gn3-east)", height=height3, depth=height3, width=width3),
    
    to_Pool("relu4", offset="(" + offs +",0,0)", to="(conv3-east)", height=height4, depth=height4, width=1),
    to_Norm("gn4", offset="(0,0,0)", to="(relu4-east)", height=height4, depth=height4, width=1),
    to_Conv("conv4", "", "$F_4$", offset="(0,0,0)", to="(gn4-east)", height=height4, depth=height4, width=width4),
    
    to_Conv("out", "", "Output", offset="(" + offs +",0,0)", to="(conv4-east)", height=height5, depth=height5, width=1),
    to_UnPool("sigmoid", offset="(0,0,0)", to="(out-east)", height=height5, depth=height5, width=1),
    to_input( 'output.png', to="(sigmoid-east)", width=3.95, height=3.95),
    #sigmoid

    # connections
    to_connection_coords("-2,0,0","0,0,0"),
    to_connection("conv1", "relu2"), 
    to_connection("conv2", "relu3"),    
    to_connection("conv3", "relu4"),    
    to_connection("conv4", "out"),    
    
     
    to_connection_coords("11,-5,0","14.5,-5,0", text="3D conv + ReLu"),
    textbox(to="(0,-3.2,4)",text="$3~\mathrm{x}~3~\mathrm{x}~3 $"), 
    textbox(to="(3.3,-2.9,4)",text="$5~\mathrm{x}~5~\mathrm{x}~5 $"), 
    textbox(to="(6.6,-2.5,4)",text="$5~\mathrm{x}~5~\mathrm{x}~5 $"), 
    textbox(to="(10.3,-2.3,4)",text="$3~\mathrm{x}~3~\mathrm{x}~3 $"), 
    textbox(to="(14.6,-2,4)",text="$1~\mathrm{x}~1~\mathrm{x}~1 $"), 
    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
