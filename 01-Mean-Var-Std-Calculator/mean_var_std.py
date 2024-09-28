import numpy as np

def calculate(lista):
    
    # Verificar se a lista tem exatamente 9 elementos
    if len(lista) != 9:
        raise ValueError("A lista deve conter 9 números.")

    # Converte a lista em um array NumPy 3x3
    array = np.array(lista).reshape(3,3)
    
    # Calcula a média
    média = [list(np.mean(array, axis=0)), list(np.mean(array, axis=1)), np.mean(array).tolist()]
    
    # Calcula a variância
    variância = [list(np.var(array, axis=0)), list(np.var(array, axis=1)), np.var(array).tolist()]
    
    # Calcula o desvio padrão
    std_dev = [list(np.std(array, axis=0)), list(np.std(array, axis=1)), np.std(array).tolist()]
    
    # Encontra o valor máximo
    max_value = [list(np.max(array, axis=0)), list(np.max(array, axis=1)), np.max(array).tolist()]
    
    # Encontra o valor mínimo
    min_value = [list(np.min(array, axis=0)), list(np.min(array, axis=1)), np.min(array).tolist()]
    
    # Calcula a soma
    sum_value = [list(np.sum(array, axis=0)), list(np.sum(array, axis=1)), np.sum(array).tolist()]

    # Retorna os resultados dos cálculos
    calculations = {
        'média': média,
        'variance': variância,
        'standard deviation': std_dev,
        'max': max_value,
        'min': min_value,
        'sum': sum_value
    }


    return calculations