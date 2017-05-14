def test(a, b, numbers):
    for a in range(0,b):
        print "At the top a is %d" % a
        numbers.append(a)
    
        a = a + 1
        print "Number now:", numbers
        print "At the bottom a is %d" % a
 

b = int(raw_input("Please type the assignment:"))

test(0,b,[])    

