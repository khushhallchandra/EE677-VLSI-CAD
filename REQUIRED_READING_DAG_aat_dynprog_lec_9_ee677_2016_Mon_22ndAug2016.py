# file DAG_aat_dynprog_lec_9_ee677_2016_Mon_22ndAug2016.py

# We will assume that "fanin" represents a DAG ( directed acyclic  graph )

# For ee-677-2016
# --- SBP ( Mon - 22nd Aug 2016 )

import copy

def toposort( fanin_copy ) :

  # Initially "fanin_copy" is a deepcopy of "fanin"
  # We have made a deepcopy, so that we allow this subroutine 
  # to modify "fanin_copy" so that
  # each of its sublists "fanin_c py[v]" is a list containing 
  # yet-to-be-topologically-sorted nodes that are in the "fanin" of node v
  
  topo_list = []
  while ( len(topo_list) < len( fanin_copy ) ) :

    # Rather than using "zero-indegree" idea, that I was outlining 
    # during lecture, I prefer to express the logic of this algo as below

    # "curr_src" denotes the next vertex/node in topological order.
    # ( You might prefer to name it "next_vertex_to_be_put_in_topo_list" )
    # And it is a node that has
    # all its fanin-neighbours already processed (i.e. put in topo_list )
   
    curr_src = find_Node_Whose_All_Fanin_Nodes_Are_Processed( fanin_copy, topo_list )

    topo_list.append( curr_src ) 

    # "removing" this "curr_src" as anybody's "fanin-neighbour"

    for v in range( len( fanin_copy ) ) :
      if ( curr_src in fanin_copy[v] ) :
        # remove "curr_src" from fanin_copy[ v ]
        fanin_copy[v].remove( curr_src ) 

  return topo_list  

def find_Node_Whose_All_Fanin_Nodes_Are_Processed( fanin_copy, topo_list ) :
  for v in range( len( fanin_copy ) ) :
    if ( len( fanin_copy[ v ] ) == 0 ) and ( v not in topo_list ) :
      return v
  return None

    
def aat_dynprog ( fanin, dly ) :

  aat = [ 0 for l in fanin ]

  toposort_list = toposort ( copy.deepcopy( fanin ) ) 
  
  for v in toposort_list :
    tmp = dly[ v ]
    for u in fanin[ v ] :
      if ( tmp < aat[u] + dly[v] ) :
        tmp = aat[u] + dly[v] 
    aat[v] = tmp  
       
  return aat


fanin = [[3, 2, 1], [], [8, 5, 4, 3], [7, 6], [8, 6, 5], [7, 6], [9, 8], [9], [9], []]

N = len(fanin)

dly = [ 10 for l in fanin ]

print "aat values are ", aat_dynprog( fanin, dly ) 
#output : aat values are  [70, 10, 60, 40, 50, 40, 30, 20, 20, 10]
