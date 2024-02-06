#define trIANGLES
left    =  "   +\n+  +\n   +"
right   = "+   \n+  +\n+"
down    = "+    +    +\n\n     +"
up      = "     +\n\n+    +    +"
#define the list
all     = ("left","right","down","up")
# ask for direction:
deirection = input("introduce the direction(upmdown,left,right:)")

#check input and print 
if deirection in all:
    if deirection == "up":
        print(up)
    if deirection =="down":
        print(down)
    if deirection == "left":
        print(left)
    if deirection =="right":
        print(right)
else:
    print(all)
    exit("Error: invalid direction")