"""i_am__controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

if __name__ =="__main__":

    robot = Robot()
    timestep = 64;
    max_s=6.28;
    
    lm=robot.getMotor('motor_1')
    rm=robot.getMotor('motor_2')
    lm.setPosition(float('inf'));
    rm.setPosition(float('inf'));
    
    front=robot.getDistanceSensor('front')
    left=robot.getDistanceSensor('left')
    right=robot.getDistanceSensor('right')
    front.enable(timestep)
    left.enable(timestep)
    right.enable(timestep)
    
    
    lm.setVelocity(0.0)
    rm.setVelocity(0.0)
    
    
    
    while robot.step(timestep) != -1:
        lval=left.getValue();
        rval=right.getValue();
        fval=front.getValue();
        print("left: " ,lval ,"right: ",rval,"front :",fval);
        f=fval>800;
        l=lval>800;
        r=rval>800;
        
        if f and l :
          ls=-max_s/2;
          rs=max_s;
          print("left")
          
        elif(f):   
          ls=max_s;
          rs=max_s;
          print("front")
          
        elif(l)  :
          ls=-max_s/2;
          rs=max_s;
          print("left")
        
        elif(r)  :
          ls=max_s;
          rs=-max_s/2;
          print("right")
        else:
          ls=-max_s;
          rs=max_s;
            
          
      
        lm.setVelocity(ls); 
        rm.setVelocity(rs);    