



def fizzbuzz(n):
    output = []
    for i in range(n):
        string = ''
        if (i+1)% 3 ==0:
            string = "Fizz"
        if (i+1)% 5==0:
            string += "Buzz"

        if not string:
            string = str(i+1)
            
        output.append(string)
    return output









if __name__ == '__main__':
    n = 15
    print(fizzbuzz(n))