import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, log_loss
from sklearn.utils import shuffle
import joblib

# Carichiamo il Dataset
DATASET_PATH = "../../Dataset/ternary_mnist/ternary_mnist.csv"
dataset = np.loadtxt(open(DATASET_PATH, "rb"), delimiter=",")

# Prepariamo i Dati
X = dataset[:,:-1] #bianco e nero 
y = dataset[:,-1:] #classe

X, y = shuffle(X, y)#mescoliamo i dati per non avere di fila tutti 0, poi tutti 1, poi tutti 2
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.6, random_state=0)

X_train=X_train/255
X_test=X_test/255

# Creiamo il Modello
lr = LogisticRegression()
lr.fit(X_train, y_train)

# Valutiamo il Modello
y_pred_train = lr.predict(X_train)
y_pred_train_proba = lr.predict_proba(X_train)
y_pred_test = lr.predict(X_test)
y_pred_test_proba = lr.predict_proba(X_test)

print(accuracy_score(y_train, y_pred_train))
print(accuracy_score(y_test, y_pred_test))
print(log_loss(y_train, y_pred_train_proba))
print(log_loss(y_test, y_pred_test_proba))

# Esportiamo il Modello
joblib.dump(lr, 'ternary_mnist_model.pkl')