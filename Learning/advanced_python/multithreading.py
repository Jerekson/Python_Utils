import threading, time
import request as r

def my_function(arg):
    print("first try thread with arg : " + arg)

# Creation d'un thread
thread = threading.Thread(target=my_function, args=("2"))
thread.start()
thread.join() # .join permet d'attendre la fin de l'exuction du thread



# ------------- Execution en parallèle d'une requete http
base_URL = "https://archive


# Source : 
# - https://ledatascientist.com/multithreading-en-python/
# - https://www.educative.io/answers/what-is-threadingactivecount-in-python
