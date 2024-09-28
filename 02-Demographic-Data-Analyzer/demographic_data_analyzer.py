import pandas as pd

def calculate_demographic_data(print_data=True):
    
    df = pd.read_csv('02-Demographic-Data-Analyzer/adult.data.csv')

    # 1. Quantas pessoas de cada raça estão representadas neste conjunto de dados?
    race_count = df['race'].value_counts()

    # 2. Qual é a idade média dos homens?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # 3. Qual a porcentagem de pessoas que possuem um diploma de Bacharelado?
    percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100

    # 4. Qual a porcentagem de pessoas com educação avançada que ganham mais de 50K?
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_rich = (higher_education['salary'] == '>50K').mean() * 100

    # 5. Qual a porcentagem de pessoas sem educação avançada que ganham mais de 50K?
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_rich = (lower_education['salary'] == '>50K').mean() * 100

    # 6. Qual é o número mínimo de horas que uma pessoa trabalha por semana?
    min_work_hours = df['hours-per-week'].min()

    # 7. Qual a porcentagem das pessoas que trabalham o número mínimo de horas por semana e ganham mais de 50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = (num_min_workers['salary'] == '>50K').mean() * 100

    # 8. Qual país tem a maior porcentagem de pessoas que ganham mais de 50K?
    country_salary = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_total = df['native-country'].value_counts()
    highest_earning_country = (country_salary / country_total * 100).idxmax()
    highest_earning_country_percentage = (country_salary / country_total * 100).max()

    # 9. Qual a ocupação mais popular para as pessoas que ganham mais de 50K na Índia?
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # Mostrar resultados se print_data for True
    if print_data:
        print(f"Contagem por raça: \n{race_count}")
        print(f"Idade média dos homens: {average_age_men}")
        print(f"Porcentagem com diploma de Bacharelado: {percentage_bachelors}%")
        print(f"Porcentagem com educação avançada que ganham >50K: {higher_education_rich}%")
        print(f"Porcentagem sem educação avançada que ganham >50K: {lower_education_rich}%")
        print(f"Tempo mínimo de trabalho: {min_work_hours} horas/semana")
        print(f"Porcentagem de ricos entre aqueles que trabalham menos horas: {rich_percentage}%")
        print(f"País com maior porcentagem de ricos: {highest_earning_country} ({highest_earning_country_percentage}%)")
        print(f"Ocupaçao mais comum na Índia entre os que ganham >50K: {top_IN_occupation}")

    # Retornar os resultados
    return {
        'race_count': race_count,
        'average_age_men': round(average_age_men, 1),
        'percentage_bachelors': round(percentage_bachelors, 1),
        'higher_education_rich': round(higher_education_rich, 1),
        'lower_education_rich': round(lower_education_rich, 1),
        'min_work_hours': min_work_hours,
        'rich_percentage': round(rich_percentage, 1),
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': round(highest_earning_country_percentage, 1),
        'top_IN_occupation': top_IN_occupation
    }
