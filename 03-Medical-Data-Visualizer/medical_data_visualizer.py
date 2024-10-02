import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Importar os dados
df = pd.read_csv('03-Medical-Data-Visualizer/medical_examination.csv')

# Adicionar a coluna 'overweight' (sobrepeso)
BMI = df['weight']/((df['height']/100)**2)
df['overweight'] = pd.Series(BMI > 25, dtype='int64')

# normaliza os dados, indicando 0 sempre bom e 1 sempre ruim. Se o valor de cholesterol ou gluc for 1, faça o valor 0. Se o valor for maior que 1, faça o valor 1.
df['cholesterol'] = pd.Series(df['cholesterol'] > 1, dtype='int64')
df['gluc'] = pd.Series(df['gluc'] > 1, dtype='int64')

# Desenhar o gráfico categórico (categorical Plot)
def draw_cat_plot():
    # Criar o DataFrame para o gráfico categórico usando `pd.melt`, utilizando apenas os valores de 'cholesterol', 'gluc', 'smoke', 'alco', 'active', e 'overweight'.
    list_vars = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
    df_cat = pd.melt(df, id_vars='cardio', value_vars=list_vars)

    # agrupar e reformatar os dados para dividir por cardio 
    df_cat = pd.concat([df_cat.loc[df_cat['cardio'] == 0], df_cat.loc[df_cat['cardio'] == 1]])


    frames = []
    for j in range(2):
        for k in range(2):
            for i in list_vars:
            
                frames.append(pd.DataFrame({'cardio': [j], 'variable': i, 'value': k, 'total': [df_cat.loc[(df_cat['cardio'] == j) & (df_cat['variable'] == i) & (df_cat['value'] == k)].shape[0]]}))
    
    df_cat = pd.concat(frames)

    # plota o gráfico categórico 
    fig = sns.catplot(x="variable", y="total", hue="value", kind="bar", data=df_cat, col_wrap=2, col='cardio')

    # linhas para não mexer
    fig.savefig('catplot.png')
    return fig


# plota o heatmap
def draw_heat_map():

    # limpeza os dados
    df_heat = df.drop(df.index[
    # remove os valores de pressão arterial sistólica (ap_hi) menores ou iguais a pressão arterial diastólica (ap_lo)
     (df['ap_lo'] > df['ap_hi']) | 
    # remove outliers na altura e peso
     (df['height'] < df['height'].quantile(0.025)) |
     (df['height'] > df['height'].quantile(0.975)) |
     (df['weight'] < df['weight'].quantile(0.025)) |
     (df['weight'] > df['weight'].quantile(0.975))
     
     ])

    # calcular a matriz de correlação
    corr = df_heat.corr()

    # gerar uma máscara para o triângulo superior
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # configurar a figura do matplotlib
    fig, ax = plt.subplots()

    # Desenhar o mapa de calor com 'sns.heatmap()'
    with sns.axes_style("white"):
        ax = sns.heatmap(corr, mask=mask, square=True, annot=True, fmt=".1f")

    fig.set_size_inches(15, 15)

    # linhas para não mexer
    fig.savefig('heatmap.png')
    return fig
