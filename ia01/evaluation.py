def partition_train_val(X, y, r=0.2):
    n = len(X)
    K = round(1 / r)
    X_train, y_train = [], []
    X_val, y_val = [], []
    for i in range(n):
        if i % K == 0:
            X_val.append(X[i])
            y_val.append(y[i])
        else:
            X_train.append(X[i])
            y_train.append(y[i])
    return X_train, y_train, X_val, y_val

def partition_val_croisee(X, y, K=5):
    n = len(X)
    X_K, y_K = [], []
    for k in range(K):
        X_K.append([])
        y_K.append([])
    for i in range(n):
        X_K[i % K].append(X[i])
        y_K[i % K].append(y[i])
    return X_K, y_K