import matplotlib.pyplot as plt

def small():
  x=(3,3,4,4,3)
  y=(3,4,4,3,3)
  plt.plot(x, y, 'ro--')
  plt.show()

def medium():
  x=(3,3,4,4,3)
  y=(3,4,4,3,3)
  plt.plot(x, y, 'go--')
  plt.show()

small()
medium()