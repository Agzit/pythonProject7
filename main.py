import csv


def load_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        print("Заголовки в файле:", reader.fieldnames)
        return [row for row in reader]


def parse_client_data(client_data):
    full_name = client_data['name']
    gender = 'женского' if client_data['sex'].lower() == 'female' else 'мужского'
    age = client_data['age']
    amount_spent = client_data['bill']
    device = client_data['device_type']
    browser = client_data['browser']
    region = client_data['region']

    description = (f"Пользователь {full_name} {gender} пола, {age} лет совершил(а) покупку на "
                   f"{amount_spent} у.е. с {device} браузера {browser}. Регион, из которого совершалась покупка: {region}.")
    return description


def save_descriptions_to_txt(descriptions, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for description in descriptions:
            f.write(description + '\n')


def main(input_file, output_file):
    clients_data = load_csv(input_file)

    descriptions = [parse_client_data(client) for client in clients_data]

    save_descriptions_to_txt(descriptions, output_file)


if __name__ == "__main__":
    input_file = 'web_clients_correct.csv'  # Путь к файлу CSV
    output_file = 'clients_descriptions.txt'  # Путь к файлу для записи текстов
    main(input_file, output_file)
