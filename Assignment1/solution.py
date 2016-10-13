def apply_AND_robdds_rec ( level, robdd_f_root_index, robdd_g_root_index  ) :

    if(robdd_f_root_index==0 or robdd_g_root_index==0):
        return 0

    if ( level == NumVars ) :
        return 1 if (robdd_f_root_index==1 and robdd_g_root_index==1) else 0

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

    E_tuple_index = apply_AND_robdds_rec (  level+1, robdd_f_E_index, robdd_g_E_index )
    T_tuple_index = apply_AND_robdds_rec (  level+1, robdd_f_T_index, robdd_g_T_index )

    if ( E_tuple_index == T_tuple_index ) :
        return E_tuple_index

    if ( not ( ( 'x'+str(level) , E_tuple_index, T_tuple_index ) in robdd_store  ) ) :
      robdd_store.append( ( 'x'+str(level) , E_tuple_index, T_tuple_index ) )
        return len(robdd_store) - 1
    else :
        return robdd_store.index( ( 'x'+str(level) , E_tuple_index, T_tuple_index ) ) 

def apply_NAND_robdds_rec ( level, robdd_f_root_index, robdd_g_root_index  ) :

    if(robdd_f_root_index==0 or robdd_g_root_index==0):
        return 1
       
    if ( level == NumVars ) :
        return 0 if (robdd_f_root_index==1 and robdd_g_root_index==1) else 1

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

    E_tuple_index = apply_NAND_robdds_rec (  level+1, robdd_f_E_index, robdd_g_E_index )
    T_tuple_index = apply_NAND_robdds_rec (  level+1, robdd_f_T_index, robdd_g_T_index )

    if ( E_tuple_index == T_tuple_index ) :
        return E_tuple_index

    if ( not ( ( 'x'+str(level) , E_tuple_index, T_tuple_index ) in robdd_store  ) ) :
        robdd_store.append( ( 'x'+str(level) , E_tuple_index, T_tuple_index ) )
        return len(robdd_store) - 1
    else :
        return robdd_store.index( ( 'x'+str(level) , E_tuple_index, T_tuple_index ) ) 

def apply_NOT_robdds_rec ( level, robdd_f_root_index ) :
       
    if ( level == NumVars ) :
        return 0 if (robdd_f_root_index==1 ) else 1

    if ( 'x'+str(level) != robdd_store[ robdd_f_root_index ][0] ) :
        robdd_f_E_index = robdd_f_root_index
        robdd_f_T_index = robdd_f_root_index
    else :
        robdd_f_E_index = robdd_store[ robdd_f_root_index ][1]
        robdd_f_T_index = robdd_store[ robdd_f_root_index ][2]


    E_tuple_index = apply_NOT_robdds_rec (  level+1, robdd_f_E_index )
    T_tuple_index = apply_NOT_robdds_rec (  level+1, robdd_f_T_index )

    if ( E_tuple_index == T_tuple_index ) :
        return E_tuple_index

    if ( not ( ( 'x'+str(level) , E_tuple_index, T_tuple_index ) in robdd_store  ) ) :
        robdd_store.append( ( 'x'+str(level) , E_tuple_index, T_tuple_index ) )
        return len(robdd_store) - 1
    else :
        return robdd_store.index( ( 'x'+str(level) , E_tuple_index, T_tuple_index ) )         