from sklearn import tree 
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def DecisionTree(x_train, y_train, y_test, x_test):
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(x_train, y_train)

    y_pred = clf.predict(x_test)

    print("Acurácia:", accuracy_score(y_test, y_pred))
    print("\nRelatório de Classificação:\n", classification_report(y_test, y_pred))
    print("\nMatriz de Confusão:\n", confusion_matrix(y_test, y_pred))

def RamdomForest(x_train, y_train, y_test, x_test):
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

    # Instanciar o modelo
    rf_model = RandomForestClassifier(n_estimators=100, max_depth=7, random_state=42)

    # Treinar
    rf_model.fit(x_train, y_train)

    # Prever
    y_pred_rf = rf_model.predict(x_test)

    # Avaliar
    print("Acurácia RF:", accuracy_score(y_test, y_pred_rf))
    print("\nRelatório RF:\n", classification_report(y_test, y_pred_rf))
    print("\nMatriz de Confusão RF:\n", confusion_matrix(y_test, y_pred_rf))
