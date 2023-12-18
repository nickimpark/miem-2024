# Achievement #2: Линейная клиент-серверная архитектура

## Постановка задачи

**Задача которую должна выполнять система:**

- Обрабатывать HTTP POST запрос в котором передается натуральное число от 0 до N, в ответ на запрос отправлять число увеличенное на единицу.
- Обрабатывать исключительную ситуацию #1: если число уже поступало то выводить ошибку в ответ и лог.
- Обрабатывать исключительную ситуацию #2: если поступившее число на единицу меньше уже обработанного числа то выводить ошибку в ответ и лог.

**Стандартная сложность** - разработать диаграмму компонентов для системы на языке UML (Component diagram).

**Средняя сложность** - выполнить задание стандартной сложности. Разработать диаграмму последовательностей для системы на языке UML (Sequence diagram).

**Высокая сложность** - выполнить задание средней сложности. Разработать систему на одном из языков программирования PYTHON/PHP/JS.

## Решение
### 1. Диаграмма компонент (стандартная сложность)
![image](https://github.com/nickimpark/miem-2024/blob/main/distributed-computing-course/achievement-2/component_diagram_1.png?raw=true)

### 2. Диаграмма последовательностей (средняя сложность)
![image](https://github.com/nickimpark/miem-2024/blob/main/distributed-computing-course/achievement-2/sequence_diagram_1.png?raw=true)

### 3. Система на языке Python (высокая сложность)
Python3 + PostgreSQL (with psycopg2)

Flask App: <a href="https://github.com/nickimpark/miem-2024/blob/main/distributed-computing-course/achievement-2/main.py">main.py</a>

```
docker build -t number-increment .
docker run --env-file=env.txt --network=host -p 5000:5000  number-increment
```

(Дополнительно) Создание пустой таблицы для примера: <a href="https://github.com/nickimpark/miem-2024/blob/main/distributed-computing-course/achievement-2/create_table.py">create_table.py</a>
