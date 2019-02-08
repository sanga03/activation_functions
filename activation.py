import numpy as np
import matplotlib.pyplot as plt
import sys


def sigmoid(inputs):
    """
    Calculate the sigmoid for the give inputs (array)
    :param inputs:
    :return:
    """
    sigmoid_scores = [1 / float(1 + np.exp(- x)) for x in inputs]
    return sigmoid_scores

def softmax(inputs):
    """
    Calculate the softmax for the give inputs (array)
    :param inputs:
    :return:
    """
    return np.exp(inputs) / float(sum(np.exp(inputs)))
  
def stepfunc(inputs,th):
    steps=[]
    for i in inputs:
        if i > th:
            steps.append(1)
        else:
            seps.append(0)
    return steps

def linear(inputs,c):
    return[i*c for i in inputs]

def tanh(inputs):
    tan_S=[2/float(2+np.exp(-2*x))-1 for x in inputs]
    return tan_S
def line_graph(x, y, x_title, y_title):
    plt.plot(x, y)
    plt.xlabel(x_title)
    plt.ylabel(y_title)
    plt.show()
def relu(inputs):
    outs=[]
    for i in inputs:
        if(i<0):
            outs.append(0)
        else:
            outs.append(i)
    return outs

def lrelu(inputs):
    outs=[]
    for i in inputs:
        if(i<0):
            outs.append(0.01*i)
        else:
            outs.append(i)
    return outs



#inputs=[2,3,7,100,-12]
inputs=range(-100,100)
args=sys.argv
print(softmax(inputs))
if(args[1]=="sigmoid"):
    print(sigmoid(inputs))
    graph_x = inputs
    graph_y = sigmoid(inputs)
    line_graph(graph_x, graph_y, "Inputs", "Sigmoid Scores")

if(args[1]=="softmax"):
    print(softmax(inputs))
    graph_x = inputs
    graph_y = softmax(inputs)
    line_graph(graph_x, graph_y, "Inputs", " softmax Scores")

 
if(args[1]=="linear"):
    print(linear(inputs,5))
    graph_x = inputs
    graph_y = linear(inputs,5)
    line_graph(graph_x, graph_y, "Inputs", " linear Scores")   

if(args[1]=="tanh"):
    print(tanh(inputs))
    graph_x = inputs
    graph_y = tanh(inputs)
    line_graph(graph_x, graph_y, "Inputs", "tanh Scores")

if(args[1]=="relu"):
    sub=sys.argv[2]
    print(sub)
    if sub=='0':
       # print(relu(inputs))
        graph_x = inputs
        print("inside relu")
        graph_y = relu(inputs)
        line_graph(graph_x, graph_y, "Inputs", " relu Scores")
    if sub=='1':
        #print(nrelu(inputs))
        graph_x = inputs
        graph_y = relu(inputs)
        line_graph(graph_x, graph_y, "Inputs", "noisy relu  Scores")
    if sub=='2':
        #print(lrelu(inputs))
        graph_x = inputs
        graph_y = lrelu(inputs)
        line_graph(graph_x, graph_y, "Inputs", " leaky relu Scores")

if(args[1]=="step"):
    print(stepfunc(inputs,10))
    graph_x = inputs
    graph_y = stepfunc(inputs,10)
    line_graph(graph_x, graph_y, "Inputs", "step function Scores")



