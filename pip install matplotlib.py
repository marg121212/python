import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm



dataset_name = 'co2'
start_year = 1958
end_year = 1980

# Загрузка набора данных
data = sm.datasets.co2.load_pandas()
df = data.data

# Преобразование DatetimeIndex в столбец 'date'
df['date'] = df.index.to_series() # Явное преобразование в Series
df = df.set_index('date')

# Ограничение временного промежутка
df['year'] = df.index.year # Создаем столбец 'year'
df = df[(df['year'] >= start_year) & (df['year'] <= end_year)]

# Построение графика
plt.figure(figsize=(12, 6))
plt.plot(df['co2'], label='CO2 уровень')  # Только один временной ряд: 'co2'

plt.xlabel('Дата')
plt.ylabel('Уровень CO2')
plt.title(f'Уровень CO2 ({start_year}-{end_year})')
plt.legend()
plt.grid(True)
plt.show()