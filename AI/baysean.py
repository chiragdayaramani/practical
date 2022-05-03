import math
import math
W = [[1.0 , 0.0], [0.1, 0.9], [0.1, 0.9], [0.01, 0.99]]
R = [[0.8, 0.2], [0.2, 0.8]]
S = [[0.5, 0.5], [0.9, 0.1]]
C = [[0.5,0.5]]
dag = {'C':['S','R'],'S':['W'],'R':['W'] }
#inputs
probS = float(input("Enter probability of S: "))
probC = float(input("Enter probability of C: "))
probSF = 1 - probS
probR = float(input("Enter probability of R: "))
probRF = 1 - probR
probWSR = float(input("Enter probability of W/SR: "))
probWSR_ = float(input("Enter probability of W/SRF: "))
probWS_R = float(input("Enter probability of W/SFR: "))
probWS_R_ = float(input("Enter probability of W/SFRF: "))
# Probability of Wet Grass
probW = probWSR * probS * probR + probWSR_ * probS * probRF + probWS_R * probSF *  probR
+ probWS_R_ * probSF * probRF
print("The probability of Wet Grass is:", probW)
#Probability of Given Condition
probA = probW * probRF * probS * probC
print("The probability of the given condition is:", probA)
