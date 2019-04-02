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
  
  # fp = open('Entropy_Result.txt', 'w+')
  # string = 'Approximate Entropy\nFor series: ',  ' '.join(str(n) for n in series), '\nPhi1: ', str(phi[0]), ', Phi2: ', str(phi[1]), '\nEntropy: ', str(entropy)
  # fp.writelines(string)

  print('For series:', series)
  print('Phi1:', phi[0], ', Phi2:', phi[1])
  print('Entropy:', entropy)

def shannonEn(series):
  classify = []
  count = []
  for number1 in series:
    if number1 not in classify:
      classify.append(number1)
      count.append(0)
      for number2 in series:
        if number1 == number2:
          count[classify.index(number1)] += 1
  entropy = 0
  for prob in count:
    entropy += prob / len(series) * math.log(prob / len(series), 2)
  entropy *= -1
  print('For series:', series)
  print('Entropy:', entropy)

def sampleEn(series, m):
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
      c += temp / (len(series) - winSize[i] + 1)
    phi[i] = c / (len(series) - winSize[i] + 1)
  entropy = math.log(phi[0] / phi[1])
  print('For series:', series)
  print('Phi1:', phi[0], ', Phi2:', phi[1])
  print('Entropy:', entropy)

series1 = [10,20,10,20,10,20,10,20,10,20,10,20]
series2 = [10,10,20,10,20,20,20,10,10,20,10,20]
series3 = ['A','A','A','A','B','B','C','D']
# approxEn(series1, 1)
# approxEn(series2, 1)
shannonEn(series3)
sampleEn(series1, 1)
sampleEn(series2, 1)
