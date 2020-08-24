import pymysql.cursors


def getConnection():
    connection = pymysql.connect(host='localhost',
                                 user='mysql',
                                 password='mysql',
                                 db='sql_work',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


# Подключиться к базе данных.
connection = getConnection()

print("Connect successful!")

# SQL
sql = '''
    SELECT lessons.id,lessons.event_id,lessons.subject,lessons.scheduled_time,participants.user_id,users.role,quality.tech_quality
    FROM lessons,participants,users,quality
    WHERE lessons.subject = ' phys'
    AND lessons.event_id = participants.event_id
    AND participants.user_id = users.id
    AND users.role = ' tutor'
    AND lessons.id = quality.lesson_id
    ORDER BY `lessons`.`scheduled_time` DESC
'''

try:

    with connection.cursor() as cursor:

        # Выполнить команду запроса (Execute Query).
        cursor.execute(sql)

        date = []
        tutors = []
        avr = []
        summator = []

        for row in cursor:
            if row['scheduled_time'] in date:
                if row['user_id'] not in tutors:
                    if 'tutor' in row['role']:
                        tutors.append(row['user_id'])
                else:
                    if row['tech_quality'].isdigit():
                        avr.append(int(row['tech_quality']))
            else:
                date.append(row['scheduled_time'])
                if sum(avr) != 0:
                    summator.append([[row['scheduled_time']], [row['user_id']], [sum(avr)/len(avr)]])

        for i in summator:
            print(i)



finally:
    # Закрыть соединение (Close connection).
    connection.close()
