if __name__ == '__main__':

    a = 1.0
    b = 0.0
    c = 0.2 - 1.0
    d = -0.7 * 0.2

    q = (3 * a * c - b ** 2) / (9 * a ** 2)
    r = (9 * a * b * c - 27 * a ** 2 * d - 2 * b ** 3) / (54 * a ** 3)

    print ("q = ", q)
    print ("r = ", r)

    delta = q ** 3 + r ** 2

    print ("delta = ", delta)


    rho = (-q ** 3) ** 0.5
   
out
    s_real = rho ** (1. / 3.)
    t_real = rho ** (1. / 3.)

    print ("s [real] = ", s_real)
    print ("t [real] = ", t_real)

    x1 = s_real + t_real - b / (3. * a)

    print ("x1 = ", x1)

    print ("should be zero: ", a * x1 ** 3 + b * x1 ** 2 + c * x1 + d)
    t_real = rho ** (1. / 3.)
    print ("s [real] = ", s_real)
    print ("t [real] = ", t_real)

    x1 = s_real + t_real - b / (3. * a)

    print ("x1 = ", x1)

    ans= testEquastion(x1,a,b,c,d)#Вызов функции автотестирования

    print (ans)

