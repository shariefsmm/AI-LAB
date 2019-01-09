
#---------------Program2-template--------------------

class environment:
    #   ax+by+c;
    a=1
    b=3
    c=2
    
    def __init__(self,agent_loc_x,agent_loc_y):
        self.agent_loc_x=agent_loc_x
        self.agent_loc_y=agent_loc_y

    """Class to define the shore."""
    def percept(self,steps,direction):
        if(steps!=0):
            print(self.agent_loc_x,",",self.agent_loc_y,"\t\t", steps, "\t",direction)

        if(direction=='r'):
            self.agent_loc_x+=1
        if(direction=='l'):
            self.agent_loc_x-=1
        if(direction=='u'):
            self.agent_loc_y+=1
        if(direction=='d'):
            self.agent_loc_y-=1
        y_cal=self.agent_loc_x*self.a+self.agent_loc_y*self.b+self.c;
        if(y_cal==0):return 1;
        if(y_cal>0):present=True;
        else:present=False;
        if(present!=self.side):return 1
        else: return 0
        
class agent:
    """Class that defines agent"""
        
    steps=0
    counter=0
    temp_counter=1
    def move_left(self):
            """Perform action moves left"""
            self.steps+=1
            self.temp_counter-=1
            percept=s.percept(self.steps,'l')
            if percept:print("Shore reached!")
            elif self.temp_counter>0:
                # self.temp_counter-=1
                self.move_left()
                
            else:
                self.temp_counter=self.counter+1
                self.move_down()
                          
    def move_right(self):
            """Perform action moves right"""
            self.steps+=1
            self.temp_counter-=1
            percept=s.percept(self.steps,'r')
            if percept:print("Shore reached!")
            elif self.temp_counter>0:
                # self.temp_counter-=1
                self.move_right()
            else:
                self.temp_counter=self.counter+1
                self.move_up()
        
    def move_up(self):
            """Perform action moves up"""
            self.steps+=1
            self.temp_counter-=1
            percept=s.percept(self.steps,'u')
            if percept:print("Shore reached!")
            elif self.temp_counter>0:
                # self.temp_counter-=1
                self.move_up()
                
            else:
                self.counter+=1
                self.temp_counter=self.counter+1
                self.move_left()
            
                          
    def move_down(self):
            """Perform action moves down"""
            self.steps+=1
            self.temp_counter-=1
            percept=s.percept(self.steps,'d')
            if percept:print("Shore reached!")
            elif self.temp_counter>0:
                # self.temp_counter-=1
                self.move_down()
                
            else:
                self.counter+=1
                self.temp_counter=self.counter+1
                self.move_right()
        
       
print("Agent Location   Steps  Direction ")
x=1;
y=1;
s=environment(x,y)
if(s.a*x+s.b*y+s.c==0):
    print("Bunny is at shore")
    exit()
if(s.a*x+s.b*y+s.c>0):s.side=True
else:s.side=False


percept=s.percept(0,'p')
if percept:
    print("Shore reached")
else:
    a=agent()
    a.move_right() 
# a=agent()
# a.move_right()
        
        

        
        

