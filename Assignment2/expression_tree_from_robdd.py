# file : prog_assign_2_ee677_2016_expression_tree_from_robdd_Wed_26_Oct.py

# The following code contains the simple classes to model following
#    types of logic node objects
# Binary Boolean Operation node, Not Operation node, Input node, Constant node

# Using these classes and the utility function "robdd_to_expr_tree(...)" 
#    provided herewith, you can build examples of expression trees
#    representing (combinational) logic functions.

# Your programming tasks are described below


# Programming Assignment # 2 :
# 1.    Implement the "evaluate" function that can be used as below
#       val = evaluate( expr_tree_function_1 , { 'x1':True, 'x2':False, 'x3':True } )
# 2.    Implement utility function to find all ON-minterms of the expression given by the
#          expression tree rooted at the given_BinBoolOp_node
#       def find_all_ON_minterms ( given_BinBoolOp_node ) :
#         ..................
#       You may represent the minterms as a tuple of positive/negative integers
#         that represent the index and polarity of variables.
#       For example,
#         ( 2, -3, -5, 6 ) represents the minterm ( x2 & ~x3 & ~x5 & x6 )
# 3.    Implement Quine's tabular method that takes a list of the on-minterms
#       of the specified function ( minterms in the above convenient form )
#       and outputs the list of primes of that function.

#--- Sachin B. Patkar ( for ee-677-2016 , Wed 26 Oct 2016 )

class BinBoolOp  :
  def __init__ ( self, name, type, inp1, inp2 ) :
    self.m_name = name
    self.m_type = type
    self.m_inp1 = inp1
    self.m_inp2 = inp2
  def __str__ ( self ) :
    return self.m_type + "( " + self.m_inp1.__str__() + "," + self.m_inp2.__str__() + " )"

class Input  :
  def __init__ ( self, name ) :
    self.m_name = name
    self.m_type = "Input"
    self.m_value = None
  def __str__ ( self ) :
    return self.m_name

class Const  :
  def __init__ ( self, value) :
    self.m_type = "Const"
    if ( value == False ) :
      self.m_name = "0"
    elif ( value == True ) :
      self.m_name = "1"
    else :
      raise Exception ( "Illegal Constant " )
    self.m_value = value
  def __str__ ( self ) :
    return str( self.m_value )

class NotOp :
  def __init__ ( self, name, inp ) :
    self.m_name = name
    self.m_type = "NOT"
    self.m_inp = inp
  def __str__ ( self ) :
    return "~(" + self.m_inp.__str__() + ")"


     
################################################################################
### utility functions to be defined  programming assignment # 2: ###############
################################################################################


def find_all_ON_minterms ( given_BinBoolOp_node ) :
  raise Exception( "to be implemented as part of programming assignment " )


def combine(m, n):
  a = len(m)
  c = ''
  count = 0
  for i in range(a): 
      if(m[i] == n[i]):
          c += m[i]
      elif(m[i] != n[i]):
          c += '-'
          count += 1

  if(count > 1): 
      return None
  else:            
      return c


def find_prime_implicants(newList):
  size = len(newList)
  IM = []
  im = []
  im2 = []
  mark = [0]*size
  m = 0
  for i in range(size):
      for j in range(i+1, size):
          c = combine(str(newList[i]), str(newList[j]))
          if c != None:
              im.append(str(c))
              mark[i] = 1
              mark[j] = 1
          else:
              continue

  mark2 = [0]*len(im)
  for p in range(len(im)):
      for n in range(p+1, len(im)):
          if( p != n and mark2[n] == 0):
              if( im[p] == im[n]):
                  mark2[n] = 1


  for r in range(len(im)):
      if(mark2[r] == 0):
          im2.append(im[r])

  for q in range(size):
      if( mark[q] == 0 ):
          IM.append( str(newList[q]) )
          m = m+1

  if(m == size or size == 1):
      return IM
  else:
      return IM + find_prime_implicants(im2)

def find_all_primes_using_Quine_s_tabular_method ( list_of_on_minterms ) :
	newList = []
	for x in list_of_on_minterms:
		temp = ''
		for i in x:
			if(i>0):
				temp += '1'
			else:
				temp += '0'
		newList.append(temp)
	# list_of_on_minterms = [ ( 2, -3, -5, 6 ), ( 2, -3, 5, 6 )]		
	# output = ['10-1']
	return find_prime_implicants(newList)

######################################################################
### DEMO of the above ( simple ) classes and utility functions : #####
######################################################################


nd_0 = Const( False )
nd_1 = Const( True )
nd_x1 = Input( 'x1' )
nd_x2 = Input( 'x2' )
nd_x3 = Input( 'x3' )
nd_x4 = Input( 'x4' )
nd_x5 = Input( 'x5' )
nd_x6 = Input( 'x6' )
nd_x7 = Input( 'x7' )
nd_x8 = Input( 'x8' )

input_nodes_map = {}
input_nodes_map['x1'] = nd_x1
input_nodes_map['x2'] = nd_x2
input_nodes_map['x3'] = nd_x3
input_nodes_map['x4'] = nd_x4
input_nodes_map['x5'] = nd_x5
input_nodes_map['x6'] = nd_x6
input_nodes_map['x7'] = nd_x7
input_nodes_map['x8'] = nd_x8


##################################################################################
## The following robdd_store convention might be a little different than
## the one used in earlier programming assignment / lectures. But nonetheless
## this is fine ( for the purpose of this programming assignment ).
##################################################################################

my_robdd_store = [
# rbd_node format (var_or_constant_label,index_of_E_child,index_of_T_child ) 
# ordering of variables is x1 > x2 > x3
        ('0', None, None ),    # rbd_nd_0  equiv logic-0
        ('1', None, None ),    # rbd_nd_1  equiv logic-1
        ('x3', 0, 1 ),         # nbd_nd_2  equiv x3
        ('x3', 1, 0 ),         # rbd_nd_3  equiv ~x3
        ('x2', 0, 1 ),         # rbd_nd_4  equiv x2
        ('x2', 1, 0 ),         # rbd_nd_5  equiv ~x2
        ('x1', 0, 1 ),         # rbd_nd_6  equiv x1
        ('x1', 1, 0 ),         # rbd_nd_7  equiv ~x1
        ('x2', 2, 3 ),         # rbd_nd_8  equiv x2 ? rbd_nd_3 : rbd_nd_2
        ('x2', 3, 2 ),         # rbd_nd_9  equiv x2 ? rbd_nd_2 : rbd_nd_3
        ('x1', 8, 9 ),         # rbd_nd_10 equiv x1 ? rbd_nd_9 : rbd_nd_8
        ('x1', 9, 8 ),         # rbd_nd_11 equiv x1 ? rbd_nd_8 : rbd_nd_9
      ]

index_of_rbd_nd_function_1 = 10 

def robdd_to_expr_tree ( given_rbd_node_index ) :
  global my_robdd_store
  global input_nodes_map

  if ( given_rbd_node_index == 0 ) :
    return Const ( False )      
  elif ( given_rbd_node_index == 1 ) :
    return Const ( True )      
  
  pos_cofactor_expr_tree =  robdd_to_expr_tree ( my_robdd_store[ given_rbd_node_index ][2] )
  neg_cofactor_expr_tree =  robdd_to_expr_tree ( my_robdd_store[ given_rbd_node_index ][1] )
  
  return BinBoolOp( "", "OR", 
                       BinBoolOp( "", "AND", 
                           input_nodes_map[ 
                              my_robdd_store[ given_rbd_node_index ][0] ], 
                           pos_cofactor_expr_tree ),
                       BinBoolOp( "", "AND", 
                           NotOp("", 
                             input_nodes_map[ 
                                my_robdd_store[ given_rbd_node_index ][0] ]), 
                           neg_cofactor_expr_tree ) ) 

expr_tree_function_1 = robdd_to_expr_tree ( index_of_rbd_nd_function_1 )

print "\n############################\n"
print "printing expression tree representing function_1 \n", expr_tree_function_1
print "\n############################\n"

# To be completed as part of programming assignment
def evaluate( given_logic_node , valuation ) :
  if isinstance( given_logic_node , Const ) :
    raise Exception( "to be implemented as part of programming assignment " )
  if isinstance ( given_logic_node, Input ) :
    raise Exception( "to be implemented as part of programming assignment " )
  if isinstance ( given_logic_node, NotOp ) :
    raise Exception( "to be implemented as part of programming assignment " )
  if isinstance ( given_logic_node, BinBoolOp ) :
    return 1
  raise Exception( " Something wrong : unsupported operation ? " )


#val = evaluate( expr_tree_function_1 , { 'x1':True, 'x2':False, 'x3':True } )
#print val
#val = evaluate( expr_tree_function_1 , { 'x1':False, 'x2':False, 'x3':True } )
#print val
#val = evaluate( expr_tree_function_1 , { 'x1':False, 'x2':True, 'x3':True } )
#print val
#val = evaluate( expr_tree_function_1 , { 'x1':False, 'x2':True, 'x3':False } )
#print val
#val = evaluate( expr_tree_function_1 , { 'x1':True, 'x2':True, 'x3':False } )
#print val
#val = evaluate( expr_tree_function_1 , { 'x1':True, 'x2':False, 'x3':False } )
#print val

