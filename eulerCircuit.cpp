# file : EulerCircuit_Hierholzer_Lec_25_ee677_2016_Thu_27_Nov.py

#   Hierholzer's algorithm " crowdsourced (???) " in ee-677-2016 Lec-25 )

#  Small "reordering" of edges of G, so that we get the same Euler (closed) path#    as was worked out manually. No cheating whatsoever !

import copy

#G = [(1,2),(2,3),(3,4),(4,1),(2,5),(5,6),(6,3),(3,2),(2,7),(7,5),(5,8),
#     (8,2),(3,9),(9,4),(4,3)]
G = [(1,2),(2,3),(2,5),(2,7),(3,4),(3,2),(3,9),(4,1),(4,3),(5,6),(5,8),
     (6,3),(7,5),(8,2),(9,4)]

def empty( G ) :
  return ( len(G) == 0 )  

def find_outedge ( G, v ) :
  for e in G :
    if ( e[0] == v ) :
      return e
  return None

def remove_edge ( G, e ) :
  G.pop( G.index( e ) )
 
def source( e ) :
  return e[0]

def target( e ) :
  return e[1]

def euler_recur_helper ( G, v , pathsofar ) :
  if ( empty(G) ) :
    return True
  e = find_outedge ( G, v )
  if ( e == None ) :
    return False
  u = target ( e )
  remove_edge( G, e )
  pathsofar.append( u )
  return euler_recur_helper ( G, u, pathsofar )


def edges( G ) :
  return copy.deepcopy( G )

def patch_paths ( p1, p2 ) :
  print "patching paths ", p1, p2
  l = p1.index( p2[0] )
  return p1[ : l ] + p2 + p1[ l+1 : ]

def find_next_start ( G, pathsofar ) :
  if ( empty( G ) ) :
    raise Exception ( "" )
  next_start = None 
  for e in edges(G) :
    if ( source(e) in pathsofar ) :
      return source( e )
  return next_start

def EulerCircuit ( G ) :
  if (  empty(G) ) :
    raise Exception( "" )
  
  pathsofar = [ edges(G)[0][0] ]
  while ( True ) :
    next_start = find_next_start ( G, pathsofar )
    patch = [ next_start ]
    print "next start is at ", next_start
    status = euler_recur_helper( G, next_start, patch )
    pathsofar = patch_paths( pathsofar, patch )
    if ( status ) :
      return pathsofar

  raise Exception( " " )

print EulerCircuit( G )

print "EXITING !"
exit(0)
      

#######################################################

start = 1
pathsofar=[start]
print "euler_recur_helper over or not ", euler_recur_helper( G, start, pathsofar )
print pathsofar

next_start = find_next_start( G, pathsofar )
#next_start = 2

next_patch = [next_start]
print "euler_recur_helper over or not ", euler_recur_helper( G, next_start, next_patch )
print next_patch

pathsofar = patch_paths( pathsofar, next_patch )

next_start = find_next_start( G, pathsofar )
#next_start = 3

next_patch = [next_start]
print "euler_recur_helper over or not ", euler_recur_helper( G, next_start, next_patch )
print next_patch

pathsofar = patch_paths( pathsofar, next_patch )

print pathsofar
