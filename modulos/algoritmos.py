from sklearn import tree 
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_recall_fscore_support

def DecisionTree(x_train, y_train, y_test, x_test, test_df):
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(x_train, y_train)

    y_pred = clf.predict(x_test)

    # print("Acurácia:", accuracy_score(y_test, y_pred))
    # print("\nRelatório de Classificação:\n", classification_report(y_test, y_pred))
    # print("\nMatriz de Confusão:\n", confusion_matrix(y_test, y_pred))

    acuracia = accuracy_score(y_test, y_pred)

    precision, recall, f1, suporte = precision_recall_fscore_support(y_test, y_pred, zero_division=0)

    # Para acessar os valores de cada classe:
    # Classe 0:
    prec_0 = precision[0]
    rec_0 = recall[0]
    f1_0 = f1[0]
    # Classe 1:
    prec_1 = precision[1]
    rec_1 = recall[1]
    f1_1 = f1[1]


    cm = confusion_matrix(y_test, y_pred)

    # cm[0][0] = verdadeiros negativos
    # cm[0][1] = falsos positivos
    # cm[1][0] = falsos negativos
    # cm[1][1] = verdadeiros positivos

    vn, fp, fn, vp = cm[0][0], cm[0][1], cm[1][0], cm[1][1]

    hits = vp + vn
    misses = fp + fn
    specificity = vn / (vn + fp)
    class_percent = (y_test.sum() / len(y_test)) * 100

    # Simulação de retorno

    # Resultados onde o modelo acertou e errou
    test_results = test_df.copy()
    test_results['y_pred'] = y_pred
    test_results['acertou'] = test_results['Target'] == test_results['y_pred']

    gain_return = test_results[test_results['acertou']]['Retorno_real'].mean()
    loss_return = test_results[~test_results['acertou']]['Retorno_real'].mean()
    net_return = gain_return - abs(loss_return)

    return {
        'accuracy': acuracia,
        'precision': prec_1,
        'recall': rec_1,
        'f1_score': f1_1,
        'specificity': specificity,
        'class_percent': class_percent,
        'hits': hits,
        'misses': misses,
        'gain_return': gain_return,
        'loss_return': loss_return,
        'net_return': net_return,
        'y_pred': y_pred
    }

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


# def simular_retorno_financeiro(test_df, y_pred, investimento_por_trade=1000):
#     df = test_df.copy()
#     df['y_pred'] = y_pred
#     df['acertou'] = df['y_pred'] == df['Target']

#     # Considerar apenas onde o modelo previu alta
#     df_entradas = df[df['y_pred'] == 1].copy()

#     df_entradas['retorno_percentual'] = df_entradas['Retorno_real'] / 100
#     df_entradas['resultado'] = df_entradas['retorno_percentual'] * investimento_por_trade

#     # Capital inicial e acumulado
#     capital_inicial = 10000
#     capital = capital_inicial

#     for lucro in df_entradas['resultado']:
#         capital += lucro

#     lucro_total = capital - capital_inicial
#     retorno_percentual = (lucro_total / capital_inicial) * 100

#     return {
#         'capital_final': capital,
#         'lucro_total': lucro_total,
#         'retorno_percentual': retorno_percentual,
#         'quantidade_operacoes': len(df_entradas),
#         'acertos': df_entradas['acertou'].sum(),
#         'erros': (~df_entradas['acertou']).sum()
#     }

def simular_retorno_financeiro(test_df, y_pred, investimento_por_trade=1000):
    df = test_df.copy()
    df['y_pred'] = y_pred
    df['acertou'] = df['y_pred'] == df['Target']

    # Considerar apenas onde o modelo previu alta
    df_entradas = df[df['y_pred'] == 1].copy()

    df_entradas['retorno_percentual'] = df_entradas['Retorno_real'] / 100
    df_entradas['resultado'] = df_entradas['retorno_percentual'] * investimento_por_trade

    # Capital inicial e acumulado
    capital_inicial = 10000
    capital = capital_inicial

    for lucro in df_entradas['resultado']:
        capital += lucro

    lucro_total = capital - capital_inicial
    retorno_percentual = (lucro_total / capital_inicial) * 100

    # Cálculo dos retornos médios
    gain_return = df_entradas[df_entradas['acertou']]['Retorno_real'].mean()
    loss_return = df_entradas[~df_entradas['acertou']]['Retorno_real'].mean()

    return {
        'capital_final': capital,
        'lucro_total': lucro_total,
        'retorno_percentual': retorno_percentual,
        'quantidade_operacoes': len(df_entradas),
        'acertos': df_entradas['acertou'].sum(),
        'erros': (~df_entradas['acertou']).sum(),
        'gain_return': gain_return,
        'loss_return': loss_return
    }
