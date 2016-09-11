# 11th Aug 2016 , EE-677-2016 , Foundations of VLSI CAD
# -- Sachin B. Patkar

def fib_rec ( n ) :

  global count

  if ( n == 2  or n==1 ) :
    count = count + 1
    # maintaining in "count" some estimate of the number of "steps" 
    # executed during the run of this code.
    return 1

  count = count + 3
  # count is incremented by 3, to account for "three basic steps" done here
  # "setting up the TWO recursive calls and the "addition" task
  # Note that this "increment-by-3" does not account for the "time consumed" 
  # for the work done inside these two recursive function calls.
  # During recursive calls themselves, "count" would be suitable incremented

  return fib_rec( n-1 ) + fib_rec( n-2 )


# Let us test it ....

#  for N in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

#  Note [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19] is more compactly
#  just "range(20)"  or "range(0,20)"
#  

# "count" variable would be updated inside function "fib_rec", in
# which it is declared as from "global" scope

count = 0

for N in range(1,20) :
  count = 0
  print "fibonacci(", N , ") = " , fib_rec ( N )
  print count
