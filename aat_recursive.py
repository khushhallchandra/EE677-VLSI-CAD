# file aat_recursive.py

# Described during Lecture # 7 (Thu-11 Aug 2016 ) of ee-677-2016
# Try it as follows :
# prompt> python aat_recursive.py 

# --- SBP ( Fri - 12th Aug 2016 )

def aat_recursive ( v ) :

  global fanin, MIN, dly
# comment : being declared as "global" because otherwise Python
#           will think of these variables as locally defined 
#           and therefore would not realize that these are defined
#           outside the function ( i.e. in global scope )
# comment : an important convenience of Python, being dynamically-typed, is
#           that we do not "declare" types of variables 
#           Python interpreter "infers" the type of variables by knowing the
#           the types of objects that are being assigned to these variables

# "fanin" is an object of the type "list". It is defined outside this function.
# Elements of list are obtained in various ways, including by "indexing"
# You notice "square bracket" .... means you are using a "list" object

  fanin_of_v = fanin[v]
  
  tmp = MIN
  if ( len(fanin_of_v) > 0 ) :
    for u in fanin_of_v :
      if ( tmp < aat_recursive( u ) + dly[ v ] ) :
        tmp = aat_recursive( u ) + dly[ v ] 
        # comment : poor coding .... recursive function aat_recursive called
        # twice for the same argument .... making things further inefficient
        # Don't blame it on "recursion" though. Recursion is fundamental !
    return tmp 
  else :
    return 0

MIN=-999999999  
# MIN is set some large negative number

# Python-object named "fanin" is of type "list" ( a "collection" object )
# elements of list "fanin" are lists themselves, containing the nodes in the 
# "fanin" of respective nodes.
 
fanin = [ [], [0], [0], [0,1], [2,3], [1,3,4], [2,3], [1,4,5,6],[],[6,7,8] ]
dly = [1,1,1,1,1,1,1,1,1,1]

# "dly" is a list object, whose i^th element represents delay of i^th node
# all delays equal to 1 ... just for simplicity of verification
# comment : more compactly  ...... dly = [ 1 ] * 10 .......

print aat_recursive ( 9 )
        
