import numpy as np

# Replacing max value with zero.
def replacemax(y):

    print(np.where(y==np.max(y,axis=1).reshape(-1,1),0,y))



# Main
def main():
    x = np.random.randint(1, 20, 15)
    print(x)
    y = x.reshape(3, 5)
    print(y)
    replacemax(y)

if __name__=="__main__":
    main()







