from faker import Faker
from file_operations import render_template
import random

NUMBER_OF_CARDS = 10

fake = Faker("ru_RU")

SKILLS = ["Стремительный прыжок",
          "Электрический выстрел",
          "Ледяной удар",
          "Стремительный удар",
          "Кислотный взгляд",
          "Тайный побег",
          "Ледяной выстрел",
          "Огненный заряд"]

LETTERS_MAPPING = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}


def main(number_of_cards):
    for j in range(number_of_cards):
        random_first_name = fake.first_name()
        random_last_name = fake.last_name()
        random_job = fake.job()
        random_city = fake.city()
        random_skills = random.sample(SKILLS, 3)
        rune_skills = []
        for i in range(len(random_skills)):
            rune_skills.append(random_skills[i])
            for original, rune in LETTERS_MAPPING.items():
                rune_skills[i] = rune_skills[i].replace(original, rune)
        context = {
                    "first_name": random_first_name,
                    "last_name": random_last_name,
                    "town": random_city,
                    "job": random_job,
                    "strength": random.randint(3, 18),
                    "agility": random.randint(3, 18),
                    "endurance": random.randint(3, 18),
                    "intelligence": random.randint(3, 18),
                    "luck": random.randint(3, 18),
                    "skill_1": rune_skills[0],
                    "skill_2": rune_skills[1],
                    "skill_3": rune_skills[2]
        }

        input_pass = "src/charsheet.svg"
        output_pass = """output/svg/{j}.{f_name}{l_name}.svg\
                        """.format(j=j,
                                   f_name=random_first_name,
                                   l_name=random_last_name)
        render_template(input_pass, output_pass, context)


if __name__ == '__main__':
    main(NUMBER_OF_CARDS)
