def quad_par():
    lista= []
    qp= [x**2 for x in range(1,11)]
    lista.append(qp)
    return qp

if  __name__=='__main__':
    k= quad_par()
    print(k)