import matplotlib.pyplot as plt

# Дані
days = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]
temperature = [20, 22, 24, 26, 28, 25, 23]
feels_like = [21, 21, 26, 28, 30, 27, 24]
wind_speed = [13, 18, 11, 16, 14, 13, 15]
humidity = [75, 64, 55, 55, 59, 65, 60]

# Лінійні графіки
fig1, ax1 = plt.subplots()
ax1.plot(days, temperature, label='Температура', linestyle='-', color='red')
ax1.plot(days, feels_like, label='Як відчувається', linestyle='--', color='blue')
ax1.set_title('Температура та як відчувається температура - Австрія, Відень')
ax1.set_xlabel('День')
ax1.set_ylabel('Температура (°C)')
ax1.legend()

fig2, (ax2_1, ax2_2) = plt.subplots(2, 1)
ax2_1.plot(days, temperature, label='Температура', linestyle='-', color='red')
ax2_1.set_title('Температура - Австрія, Відень')
ax2_1.set_xlabel('День')
ax2_1.set_ylabel('Температура (°C)')
ax2_1.legend()
ax2_2.plot(days, feels_like, label='Як відчувається', linestyle='--', color='blue')
ax2_2.set_title('Як відчувається температура - Австрія, Відень')
ax2_2.set_xlabel('День')
ax2_2.set_ylabel('Температура (°C)')
ax2_2.legend()
plt.tight_layout()


# Стовпчаста діаграма
fig3, ax3 = plt.subplots()
ax3.bar(days, wind_speed, color='green')
ax3.set_title('Швидкість вітру - Австрія, Відень')
ax3.set_xlabel('День')
ax3.set_ylabel('Швидкість вітру (м/с)')


# Кругова діаграма
explode = [0, 0, 0, 0, 0, 0.1, 0.1]
fig4, ax4 = plt.subplots()
wedges, texts, autotexts = ax4.pie(humidity, labels=days, autopct='%1.1f%%', startangle=90,
                                   wedgeprops={'edgecolor': 'white'}, explode=explode)
for i in range(len(days)):
    if days[i] in ["Субота", "Неділя"]:
        wedges[i].set_edgecolor('black')
ax4.set_title('Вологість (%) - Австрія, Відень')
plt.show()
