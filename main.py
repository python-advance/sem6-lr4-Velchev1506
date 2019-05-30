def sigmoid(x):
    import math
    return 1/(1 + math.exp(-x))

#math.exp?

#sigmoid(-30)

#print(sigmoid(-30))

def get_thata():
    thata0, thata1, thata2 = (0 , 0, 0) 
    return (thata0, thata1, thata2)

def main():
    input_x = [(0,0), (1,0), (0,1), (1,1)] 

def test_perceptron_and():
    bias_x = [1, 1 , 1, 1]
    input_x = [(0,0), (1,0), (0,1), (1,1)] 
    thata = [-30, 20, 20]
    output_h =[0, 0, 0, 1]
    #return 

    for i in range(len(input_x)):
        result = sigmoid(bias_x[i]*thata[0] + input_x[i][0]*thata[1] + input_x[i][1]*thata[2])  
        if result >= 0.9:
            result = 1
        else:
            result = 0
        assert result == output_h[i], format('*') #f"Ошибка при вычислении с параметрами x1={input_x[i][0]}, x2={input_x[i][1]}"




print(test_perceptron_and())