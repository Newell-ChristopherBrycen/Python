import logging

logging.basicConfig(filename='myProgramLog.txt',level=logging.DEBUG, format= '%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.DEBUG)

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n+1):  # error was that range started at 0 rather than 1
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))

    logging.debug('Return value is %s' %(total))
    return total

print(factorial(5))

logging.debug('End of program')


'''
2023-12-10 14:59:16,989 - DEBUG - Start of program
2023-12-10 14:59:17,014 - DEBUG - Start of factorial(5)
2023-12-10 14:59:17,015 - DEBUG - i is 0, total is 0
2023-12-10 14:59:17,015 - DEBUG - i is 1, total is 0
2023-12-10 14:59:17,029 - DEBUG - i is 2, total is 0
2023-12-10 14:59:17,031 - DEBUG - i is 3, total is 0
2023-12-10 14:59:17,031 - DEBUG - i is 4, total is 0
2023-12-10 14:59:17,031 - DEBUG - i is 5, total is 0
2023-12-10 14:59:17,031 - DEBUG - Return value is 0
'''
