# for ee-677-2016 ( preparing and solving LP for 1-d placement ( without timing )
# needs python-cvxopt ( prompt> sudo apt-get install python-cvxopt )
# also needs numpy ( part of scipy or separate )
# Sachin B. Patkar ( 13th Aug 2016 )

#     minimize summation of L_j_i over all i,j such that j->i
# subject to
#       0 <= x_i <= WIDTH ...... for all i
#       x_p = X_p .....for p among fixedCells
#       L_j_i >= x_j - x_j  ..... for j->i
#       L_j_i >= x_i - x_i .... for j->i
#       L_j_i >= minimum_separation  .... for j->i
#       a_s = 0.0
#       a_t <= r_t
#       a_i >= a_j + delay_i + alpha * L_j_i  .... for all i,j such that j->i


from cvxopt import matrix, solvers
import numpy
import random

def createLP_cvxopt_sys ( fanin , fixedCells, fixedLocations ) :
 
  global RAT_t, WIDTH, SEP, ALPHA, DELAY, var_map, s, t

  V = range( len(fanin) ) 
  A_list = [ ]
  b_list = [ ]

  num_lji_vars = 0
  for k in fanin :
    num_lji_vars += len( k )

  for i in range( len(V) ) :
    var_map[ 'x_' + str(i) ] = 2*i
    var_map[ 'a_' + str(i) ] = 2*i+1

  index_var = 2*len(V)
  for i in range( len(V) ) :
    for j in fanin[ i ] :
      var_map[ 'l_' + str(j) + '_' + str(i) ] = index_var
      index_var = index_var + 1
  
  cost_list = [ 0.0 for i in range( 2*len(V) + num_lji_vars ) ]
  for i in range( len(V) ) :
    cost_list[ var_map[ 'x_' + str(i) ] ] = 0.0
    cost_list[ var_map[ 'a_' + str(i) ] ] = 0.0

  for i in range( len(V) ) :
    for j in fanin[ i ] :
      cost_list[ var_map[ 'l_' + str(j) + '_' + str(i) ] ] = 1.0
  print "printing cost_list" , cost_list

  for v in V :
    tmp_row = [ 0.0 for i in range( 2*len(V) + num_lji_vars ) ]
    tmp_row[ var_map[ 'x_'+ str(v) ] ] = -1.0
    b_list.append ( 0.0 )
    A_list.append ( tmp_row )
    print "adding constraint ", tmp_row[ var_map['x_' + str(v) ] ], ("x_"+ str(v)), " <= ", "0"

    tmp_row = [ 0.0 for i in range(2*len(V) + num_lji_vars) ]
    tmp_row[ var_map[ 'x_'+ str(v) ] ] = 1.0
    b_list.append ( WIDTH )
    A_list.append ( tmp_row )
    print "adding constraint ", tmp_row[ var_map['x_'+ str(v) ] ], ("x_"+ str(v)), " <= ", WIDTH

  for k in range(len(fixedCells)) :
    tmp_row = [ 0.0 for i in range(2*len(V) + num_lji_vars) ]
    tmp_row[ var_map[ 'x_' + str(fixedCells[k]) ] ] = -1.0
    b_list.append ( -1.0 * fixedLocations[k] )
    A_list.append ( tmp_row )
    print "adding constraint ", tmp_row[ var_map['x_'+ str(fixedCells[k]) ] ], ("x_"+str(fixedCells[k])), "  <= ", -1.0 * fixedLocations[k]

    tmp_row = [ 0.0 for i in range(2*len(V) + num_lji_vars) ]
    tmp_row[ var_map[ 'x_' + str(fixedCells[k]) ] ] = +1.0
    b_list.append ( 1.0 * fixedLocations[k] )
    A_list.append ( tmp_row )
    print "adding constraint ", tmp_row[ var_map['x_'+ str(fixedCells[k]) ] ], ("x_"+str(fixedCells[k])), "  <= ", 1.0 * fixedLocations[k]
    
  for ii  in V :
    for jj in fanin[ ii ] : 
      tmp_row = [ 0.0 for i in range(2*len(V) + num_lji_vars) ]
      tmp_row[ var_map[ 'l_' + str(jj) + '_' + str(ii) ] ] = -1.0
      tmp_row[ var_map[ 'x_' + str(ii) ] ] = 1.0
      tmp_row[ var_map[ 'x_' + str(jj) ] ] = -1.0
      b_list.append ( 0.0 )
      A_list.append ( tmp_row )
      print "adding constraint ", tmp_row[ var_map['x_'+ str(jj) ]], ("x_"+ str(jj)), " +", tmp_row[var_map['x_'+str(ii)]], (" x_"+str(ii))," + ",tmp_row[var_map['l_'+ str(jj) +'_'+ str(ii) ]],(" l_"+str(jj)+"_"+str(ii))," <= ", "0"

      tmp_row = [ 0.0 for i in range(2*len(V) + num_lji_vars) ]
      tmp_row[ var_map[ 'l_' + str(jj) + '_' + str(ii) ] ] = -1.0
      tmp_row[ var_map[ 'x_' + str(ii) ] ] = -1.0
      tmp_row[ var_map[ 'x_' + str(jj) ] ] = 1.0
      b_list.append ( 0.0 )
      A_list.append ( tmp_row )
      print "adding constraint ", tmp_row[ var_map['x_'+ str(jj) ]], ("x_"+str(jj)), " +", tmp_row[var_map['x_'+ str(ii) ]], (" x_"+str(ii))," + ",tmp_row[var_map['l_'+ str(jj) +'_'+ str(ii) ]],(" l_"+str(jj)+"_"+str(ii))," <= ", "0"
 

  for ii  in V :
    for jj in fanin[ ii ] : 
      tmp_row = [ 0.0 for i in range(2*len(V) + num_lji_vars) ]
      tmp_row[ var_map[ 'l_' + str(jj) + '_' + str(ii) ] ] = -1.0
      b_list.append ( -1.0 * SEP)
      A_list.append ( tmp_row )
      print "adding constraint ", tmp_row[ var_map['l_'+  str(jj) +'_'+ str(ii) ] ] , ("l_"+str(jj)+"_"+str(ii)), "  <= ", (-1.0*SEP)
    
  tmp_row = [ 0.0 for i in range(2*len(V) + num_lji_vars) ]
  tmp_row[ var_map[ 'a_'+str(s) ] ] = -1.0
  b_list.append ( 0.0 )
  A_list.append ( tmp_row )
  print "adding constraint :  -1.0 a_s <= 0.0"

  tmp_row = [ 0.0 for i in range(2*len(V) + num_lji_vars) ]
  tmp_row[ var_map[ 'a_'+str(s) ] ] = 1.0
  b_list.append ( 0.0 )
  A_list.append ( tmp_row )
  print "adding constraint :  1.0 a_s <= 0.0"

  tmp_row = [ 0.0 for i in range(2*len(V) + num_lji_vars) ]
  tmp_row[ var_map[ 'a_'+str(t) ] ] = 1.0
  b_list.append ( RAT_t )
  A_list.append ( tmp_row )
  print "adding constraint :  a_t <= " , RAT_t

  for ii  in V :
    for jj in fanin[ ii ] : 
      tmp_row = [ 0.0 for i in range(2*len(V) + num_lji_vars) ]
      tmp_row[ var_map[ 'l_' + str(jj) + '_' + str(ii) ] ] = 1.0 * ALPHA
      tmp_row[ var_map[ 'a_' + str(jj) ] ] = 1.0 
      tmp_row[ var_map[ 'a_' + str(ii) ] ] = -1.0 
      b_list.append ( -1.0 * DELAY[ii] )
      A_list.append ( tmp_row )
      print "adding constraint ", tmp_row[ var_map['l_'+  str(jj) +'_'+ str(ii) ] ] , ("l_"+str(jj)+"_"+str(ii)), " + ",  tmp_row[ var_map['a_'+str(jj)]] , ("a_"+str(jj)), " + ",  tmp_row[ var_map["a_"+str(ii)]] , ("a_"+str(ii)),   "  <= ", (-1.0*DELAY[ii])
    
  return A_list, b_list, cost_list
       
      
def preparefanin_from_fanout ( fanout ) :
  fanin = [ [] for i in range( len( fanout ) ) ] 
  for i in range( len( fanout ) ) :
    for j in range( len(fanout[i]) ) :
      fanin[ fanout[i][j] ].append(i)  
  return fanin

fanout = [ [ 1, 2, 3 ], [ 3, 5, 7 ], [4, 6], [4, 5, 6], [5, 7], [7], [7,9], [9], [9], [] ]
fanin = preparefanin_from_fanout( fanout )
s=0
t=9
  
fixedCells = [0,4,6,8,9]
fixedLocations = [0, 400, 600, 800,  900 ]
WIDTH = 1000
RAT_t = 1000.0
ALPHA = 0.5
SEP = 100.0
DELAY = [ 100.0 for i in range( len( fanin ) ) ]
DELAY[0] = 0.0
DELAY[9] = 0.0
var_map = {}

print "\n********************************************  \n"
print "BEGIN : Printing the FanIn information \n"

for i in range( len(fanin) ) :
  for j in fanin[i] :
    print "cell/node ", j, " is in fanin of cell/node ", i

print "END : Printing the FanIn information \n"
print "\n********************************************  \n"

print "Fixed cells are \n"
print fixedCells
print "\n********************************************  \n"

print "Their fixed locations are \n"
print fixedLocations
print "\n********************************************  \n"

print "Source cell is ", s
print "Required arrival time at sink cell ", t, " = ", RAT_t

print "The delays of cells are \n"
print DELAY
print "\n********************************************  \n"

print "Proportionality Factor ALPHA is ", ALPHA
print "\n********************************************  \n"

A_l, b_l, c_l = createLP_cvxopt_sys ( fanin , fixedCells, fixedLocations ) 

A_matrix = matrix( numpy.array(A_l).transpose().tolist() )
b_matrix = matrix ( b_l )
c_matrix = matrix ( c_l )

print "DIM are ", A_matrix.size, len(b_matrix), len(c_matrix)

#sol=solvers.lp(c_matrix,A_matrix,b_matrix, solver='glpk')
sol=solvers.lp(c_matrix,A_matrix,b_matrix)
print ( sol['x'] )

print "optimum placement along X-axis is ", [ sol['x'][ var_map['x_'+str(i)] ] for i in range(len(fanin)) ]

