# robdd_recur_as_in_Lec16_Mon_26thSept_ee677_2016.py
# prepared for illustrating recursive approach to building ROBDD
# using already existing ROBDDs.
# This involves "applying" operators to a pair of robdds that use the
# same ordering of variables.

# --- Sachin B. Patkar ( Mon 26th Sept. 2016 )


# Assume the variable ordering a-b-c  ( often different orderings
# result in ROBDDs ( i.e. MUX2 based realizations ) of differing efficiency.
# However, here I am NOT demonstrating this important point.

# We will use a python-list "robdd_store" to store a sequence of triples ( that is, 3-tuples )
# Thus each item in this list is a triple ( i.e. 3-tuple ) that
# represents a node of ROBDD of some function on  a,b,c
# ---   field-0 is either '0'/'1'/'a'/'b'/'c'
# ---   field-1 is either None or index of the E-child 
# ---   field-1 is either None or index of the T-child 
# Importantly, the items at position 0 and 1 in this list
#   are ('0',None,None) and ('1',None,None) respectively.
#   In our notation, these are nodes "n0" and "n1" respectively.
#
# An important observation is the following :
#    robdd_store can be a used as a pool of robdd_nodes which
# can be used to represent different functions on the given set of variables, however with the
# same chosen ordering of variables ( in our example, a-b-c ).

ordered_var_list = ['a', 'b', 'c' ]

robdd_store = [ ( '0',None,None ), ('1',None,None ) , ('a',0,1) , ('a',1,0), ('b',0,1), ('b',1,0), \
    ('c',0,1), ('c',1,0), ('b',6,7), ('b',7,6), ('a',8,9), ('b',0,6), ('a',0,11), ('a',4,1) ]

def apply_AND_robdds_rec ( var_name, robdd_f_root_index, robdd_g_root_index  ) :
  
  # Termination conditions for recursion ( if both functions are constants ).
  # This should be improved by detecting the cases, where one of the functions is a constant function.
  # Left as a simple exercise

  if ( var_name == None ) :
    if ( robdd_f_root_index == robdd_g_root_index ) :
      return robdd_f_root_index
    else :
      return 0
  
  # scheme to find the robdd nodes which represent the
  #    negative and positive cofactors w.r.t. variable "var_name"

  #    I did not elaborate over it during today's lecture ( Lec 16, Mon 26th Sept 2016 )
  #    I intended it to be an exercise left to you to understand this logic
  #      of finding the nodes corresponding to negative and positive cofactors w.r.t. var_name

  #################### PART OF CODE not discussed in Lec 16 (Mon 26th Sept 2016 ) begins ########################
  if ( var_name != robdd_store[ robdd_f_root_index ][0] ) :
    robdd_f_E_index = robdd_f_root_index
    robdd_f_T_index = robdd_f_root_index
  else :
    robdd_f_E_index = robdd_store[ robdd_f_root_index ][1]
    robdd_f_T_index = robdd_store[ robdd_f_root_index ][2]

  if ( var_name != robdd_store[ robdd_g_root_index ][0] ) :
    robdd_g_E_index = robdd_g_root_index
    robdd_g_T_index = robdd_g_root_index
  else :
    robdd_g_E_index = robdd_store[ robdd_g_root_index ][1]
    robdd_g_T_index = robdd_store[ robdd_g_root_index ][2]

  if ( ordered_var_list.index( var_name ) == len( ordered_var_list ) - 1 ) :
    next_var_name = None
  else :
    next_var_name = ordered_var_list[ ordered_var_list.index( var_name ) + 1 ]
  #################### PART OF CODE not discussed in Lec 16 (Mon 26th Sept 2016 ) ends ########################

  
  ############# MAIN PART OF RECURSIVE LOGIC begins ################################
  E_tuple_index = apply_AND_robdds_rec (  next_var_name, robdd_f_E_index, robdd_g_E_index )
  T_tuple_index = apply_AND_robdds_rec (  next_var_name, robdd_f_T_index, robdd_g_T_index )

  if ( E_tuple_index == T_tuple_index ) :
    return E_tuple_index

  # Check if the triple ( i.e. 3-tuple ) that would represent the result is already
  # in the robdd_store : if so simply return the index at which it is stored in robdd_store
  #                      else append this new triple ( 3-tuple ) in the robdd_store
  #                              and return its index / position in the robdd_store
  # Note : I had omitted ( due to hurry ) this important nuance while "outlining" the recursive code

  if ( not ( ( var_name, E_tuple_index, T_tuple_index ) in robdd_store  ) ) :
    robdd_store.append( ( var_name , E_tuple_index, T_tuple_index ) )
    return len(robdd_store) - 1
  else :
    return robdd_store.index( ( var_name , E_tuple_index, T_tuple_index ) ) 
  ############# MAIN PART OF RECURSIVE LOGIC ends ################################
    

print "\n\nPresently the triples in the robdd_store are as shown below ( along with their node-ids ) \n"
print [ ( robdd_store[i], 'n'+str(i) ) for i in range( len ( robdd_store ) ) ]

print """
 applying AND operator on boolean formulae represented by nodes n10 and n13
    that is, building ROBDD for AND( XOR(a,b,c), OR(a,b) )
"""

index_of_n10_AND_n13 = apply_AND_robdds_rec( 'a', 10, 13 )

print "\n\nNow the triples in the robdd_store are as shown below ( along with their node-ids ) \n"
print [ ( robdd_store[i], 'n'+str(i) ) for i in range( len ( robdd_store ) ) ]
print "\nThe node ", ('n'+str(index_of_n10_AND_n13)), " represents AND( XOR(a,b,c), OR(a,b) ) \n"
  

