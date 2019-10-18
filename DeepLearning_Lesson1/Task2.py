import warnings
warnings.filterwarnings("ignore")
from keras.models import Sequential
from keras.layers.core import Dense, Activation
import pandas as pd


from sklearn.model_selection import train_test_split
dataset = pd.read_csv("breastcancer.csv")

classes = ['Benign', 'Malignant']

X = dataset.iloc[:, 2:32].values
y = dataset.iloc[:, 1].values

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder_X_1 = LabelEncoder()
y = labelencoder_X_1.fit_transform(y)
print(y)

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.25, random_state=87)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

my_first_nn = Sequential() # create model
my_first_nn.add(Dense(50, input_dim=30, activation='relu')) # hidden layer
my_first_nn.add(Dense(25, activation='softmax')) # hidden layer
my_first_nn.add(Dense(1, activation='sigmoid')) # output layer
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam',metrics=['accuracy'])
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100,verbose=0,
                                     initial_epoch=0)
print(my_first_nn.summary())
print(my_first_nn.evaluate(X_test, Y_test,verbose=0))

