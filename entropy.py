import math
import statistics

def approxEn(series, m):
  winSize = [m, m + 1]
  win = []
  r = statistics.stdev(series) * 0.2
  for (k, n) in enumerate(winSize):
    win.append([])
    for i in range(len(series) - n + 1):
      temp = []
      for j in range(n):
        temp.append(series[i + j])
      win[k].append(temp)

  phi = [0, 0]
  for i in range(2):
    c = 0
    for number1 in range(0, len(win[i])):
      temp = 0
      for number2 in range(number1, len(win[i])):
        if all(abs(win[i][number1][index] - win[i][number2][index]) < r for index in range(len(win[i][number1]))):
          temp += 1
      c += math.log(temp / (len(series) - winSize[i] + 1), 2)
    phi[i] = c / (len(series) - winSize[i] + 1)
  entropy = abs(phi[0] - phi[1])
  print('For series: ', series)
  print('Phi1: ', phi[0], ', Phi2: ', phi[1])
  print('Entropy: ', entropy)


series1 = [10,20,10,20,10,20,10,20,10,20,10,20]
series2 = [10,10,20,10,20,20,20,10,10,20,10,20]
approxEn(series1, 1)
approxEn(series2, 1)
