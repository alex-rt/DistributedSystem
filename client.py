import wget
from time import time


start_time = time()

wget.download('https://b9a3681663d3.ngrok.io/get')

elapsed_time = time() - start_time
print("\nElapsed time: %.10f seconds." % elapsed_time)