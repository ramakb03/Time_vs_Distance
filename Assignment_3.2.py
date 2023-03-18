import numpy as np
import matplotlib.pyplot as plt

def calcTime(distance, speed):
    #This function calculates and returns time
    time = distance / speed
    
    return time

def plotTime_Distance_Graph():
    #function plots time vs distance graph at varying speeds given by user 
    speeds = []
    #get user input for speed
    a = float(input("Enter first speed in miles: "))
    b = float (input("Enter second speed in miles: "))
    c = float (input("Enter third speed in miles: "))
    
    speeds.append(a)
    speeds.append(b)
    speeds.append(c)
    
    t1 = calcTime(15, speeds[0])
    t2 = calcTime(15, speeds[1])
    t3 = calcTime(15, speeds[2])
    t = [t1, t2, t3]
    d = [15, 15, 15]
    # plot the distance over time for each speed
    plt.plot(t, d, 'o')

    # add labels and legend to the plot
    plt.xlabel('Time (hours)')
    plt.ylabel('Distance (miles)')
    plt.title('Distance vs Time')

    # display the plot
    plt.show()
    
plotTime_Distance_Graph()
