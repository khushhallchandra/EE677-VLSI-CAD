# ProgAssign_2_ee677_2016_8_Oct.py  ( 2 MARKS WORTH )
#     Submission deadline : (Thursday : 13th October 2016 , 7.00 pm )
#
# This code illustrates recursive approach to building ROBDD
# using already existing ROBDDs.
# This involves "applying" operators to a pair of robdds that use the
# same ordering of variables.

# In particular, only XOR, OR operators are supported in the following.

# Using these two operators, it is demonstrated how the ROBDD for 
# (( x1 | x0 ) ^ x2 ^ x3 ) is built

# YOUR PROGRAMMING TASK / assignment is as follows :
# Write python code to implement the following features
# Provide examples to illustrate each of the following

#    1. Provide similar facilities for binary operator AND
#    2. Provide similar facilities for unary operator NOT
#    3. Provide similar facility for binary operator NAND
#    4. Improve the efficiency by terminating the recursion early, 
#          when one of the functions is the constant 0 or the constant 1 function
#       

#  DISCLAIMER : This code itself is **NOT AT ALL** optimized 
#     The modest aim is merely to illustrate some of the essential concepts. 

# --- Sachin B. Patkar ( 8th Oct 2016 )

# Number of variables 

NumVars = 4

print "Number of variables is ", NumVars


print """

 For instance, the nodes in the following robdd_store represent the boolean formulae 
 "0", "1", "x0", "not(x0)", "x1", "not(x1)", "x2", "not(x2)', "x3", "not(x3)" respectively.

"""

robdd_store = [ ( '0',None,None ), ('1',None,None ) , ('x0',0,1) , ('x0',1,0), ('x1',0,1), ('x1',1,0), \
    ('x2',0,1), ('x2',1,0), ('x3',0,1), ('x3',1,0) ]

print robdd_store

# In the following dictionary, we will hold the mapping ( association ) between the boolean expressions and the
# indices of corresponding robdd_nodes in the ROBDD_store

# Initially the "robdd_store" has only elementary boolean formulae 

expr2node = { '0' : 0, '1' : 1, 'x0' : 2, '~x0' : 3, 'x1' : 4, '~x1' : 5, 'x2' : 6, '~x2':7, 'x3':8, '~x3':9  }


print """

 This, by itself, is not so interesting collection of boolean formulae. But clearly this is
   merely a starting point. You can apply binary boolean operators to create more nodes
   corresponding to different boolean formulae, and store them in the same array.

 Starting with we will see, as an example, how AND operator can be applied repeatedly
    to build a couple of more boolean formulae.

 After understanding the essence of this, you can easily "generalize" it to other
    binary boolean operators such as OR, NAND, NOR, XOR, XNOR

 In practical tools based on ROBDDs, massive pools of robdd_nodes are maintained
    in an essentially similar, but far more efficiently programmed manner.

"""

  
def apply_XOR_robdds_rec ( level, robdd_f_root_index, robdd_g_root_index  ) :
  
  if ( level == NumVars ) :
    return 0 if (robdd_f_root_index==robdd_g_root_index) else 1

  if ( 'x'+str(level) != robdd_store[ robdd_f_root_index ][0] ) :
    robdd_f_E_index = robdd_f_root_index
    robdd_f_T_index = robdd_f_root_index
  else :
    robdd_f_E_index = robdd_store[ robdd_f_root_index ][1]
    robdd_f_T_index = robdd_store[ robdd_f_root_index ][2]

  if ( 'x'+str(level) != robdd_store[ robdd_g_root_index ][0] ) :
    robdd_g_E_index = robdd_g_root_index
    robdd_g_T_index = robdd_g_root_index
  else :
    robdd_g_E_index = robdd_store[ robdd_g_root_index ][1]
    robdd_g_T_index = robdd_store[ robdd_g_root_index ][2]

  E_tuple_index = apply_XOR_robdds_rec (  level+1, robdd_f_E_index, robdd_g_E_index )
  T_tuple_index = apply_XOR_robdds_rec (  level+1, robdd_f_T_index, robdd_g_T_index )

  if ( E_tuple_index == T_tuple_index ) :
    return E_tuple_index

  if ( not ( ( 'x'+str(level) , E_tuple_index, T_tuple_index ) in robdd_store  ) ) :
    robdd_store.append( ( 'x'+str(level) , E_tuple_index, T_tuple_index ) )
    return len(robdd_store) - 1
  else :
    return robdd_store.index( ( 'x'+str(level) , E_tuple_index, T_tuple_index ) ) 


def apply_OR_robdds_rec ( level, robdd_f_root_index, robdd_g_root_index  ) :
  
  if ( level == NumVars ) :
    return 1 if (robdd_f_root_index==1 or robdd_g_root_index==1) else 0
  
  if ( 'x'+str(level) != robdd_store[ robdd_f_root_index ][0] ) :
    robdd_f_E_index = robdd_f_root_index
    robdd_f_T_index = robdd_f_root_index
  else :
    robdd_f_E_index = robdd_store[ robdd_f_root_index ][1]
    robdd_f_T_index = robdd_store[ robdd_f_root_index ][2]

  if ( 'x'+str(level) != robdd_store[ robdd_g_root_index ][0] ) :
    robdd_g_E_index = robdd_g_root_index
    robdd_g_T_index = robdd_g_root_index
  else :
    robdd_g_E_index = robdd_store[ robdd_g_root_index ][1]
    robdd_g_T_index = robdd_store[ robdd_g_root_index ][2]

  E_tuple_index = apply_OR_robdds_rec (  level+1, robdd_f_E_index, robdd_g_E_index )
  T_tuple_index = apply_OR_robdds_rec (  level+1, robdd_f_T_index, robdd_g_T_index )

  if ( E_tuple_index == T_tuple_index ) :
    return E_tuple_index

  if ( not ( ( 'x'+str(level) , E_tuple_index, T_tuple_index ) in robdd_store  ) ) :
    robdd_store.append( ( 'x'+str(level) , E_tuple_index, T_tuple_index ) )
    return len(robdd_store) - 1
  else :
    return robdd_store.index( ( 'x'+str(level) , E_tuple_index, T_tuple_index ) ) 
    
# Let's build the robdd for the formula '( (((x1 | x0 ) ^ x2) ^ x3) ) '
# tmp1 represents (x1 | x0)
# tmp2 represents ((x1 | x0) ^ x2 )


tmp1 = apply_OR_robdds_rec ( 0, expr2node['x1'], expr2node['x0'] ) 
expr2node[ '(x0 | x1)' ] = tmp1
tmp2 = apply_XOR_robdds_rec ( 0, tmp1, expr2node['x2'] ) 
expr2node[ '((x0 | x1) ^ x2)' ] = tmp2
root_of_rbd_for_given_expr = apply_XOR_robdds_rec ( 0, tmp2, expr2node['x3'] ) 
expr2node[ '( (((x1 | x0 ) ^ x2) ^ x3) )' ] = root_of_rbd_for_given_expr

print (robdd_store)

print (" PRINTING robdd_store with node indices \n" )
print( "[\n")
for i in range( len ( robdd_store ) ) :
  print ( "  " + str(i) + ":"  + str( robdd_store[i] ) + "\n" )
print( "]\n")

print (" robdd for ( (((x1 | x0 ) ^ x2) ^ x3) ) is rooted at node with index " + str( root_of_rbd_for_given_expr ) + "..... Please CHECK !" )
exit()

###############################################################3
