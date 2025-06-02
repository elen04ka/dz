def generate_message(data, lessons_db):
    greeting = data.get("greeting", "Добрий день, шановні батьки!")
    absents = data.get("absents", "").strip()
    course = data.get("course")
    lesson_name = data.get("lesson")
    homework = data.get("homework", "").strip()
    custom_text = data.get("custom_text", "").strip()

    # Знайти урок
    lesson = next((l for l in lessons_db[course] if l["name"] == lesson_name), None)
    topic = lesson["topic"] if lesson else ""
    goal = lesson["goal"] if lesson else ""

    msg = f"""{greeting}

"""

    if absents:
        msg += f"На уроці були відсутні: {absents}, прошу на наступне заняття доєднатися на 30 хв раніше.\n\n"

    msg += f"💡 На уроці ми вивчили тему: {topic}\n\n"
    msg += f"Метою уроку було: {goal}\n\n"

    if custom_text:
        msg += custom_text + "\n\n"

    msg += "📕 ДОМАШНЄ ЗАВДАННЯ:\n\n"
    msg += homework + "\n\n"

    msg += """❗️  Нагадую, що практику потрібно зробити до наступного заняття.
🕧  Якщо щось не зрозуміло або потрібна допомога, мені можна писати в особисті повідомлення.
✅  За день до наступного заняття я перевіряю домашнє завдання на платформі.

Бажаю всім продуктивного тижня!🌟✨"""

    return msg
