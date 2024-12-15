import csv

class Client:
    def __init__(self, name, sex, age, bill, device_type, browser, region):
        self.name = name
        self.sex = sex
        self.age = age
        self.bill = bill
        self.device_type = device_type
        self.browser = browser
        self.region = region

    def get_gender(self):

        return 'женского' if self.sex.lower() == 'female' else 'мужского'

    def get_description(self):

        gender = self.get_gender()
        return (f"Пользователь {self.name} {gender} пола, {self.age} лет совершил(а) покупку на "
                f"{self.bill} у.е. с {self.device_type} браузера {self.browser}. Регион, из которого совершалась покупка: {self.region}.")


class ClientDataProcessor:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def load_csv(self):
        clients = []
        try:
            with open(self.input_file, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                print("Заголовки в файле:", reader.fieldnames)
                for row in reader:
                    client = Client(
                        name=row['name'],
                        sex=row['sex'],
                        age=row['age'],
                        bill=row['bill'],
                        device_type=row['device_type'],
                        browser=row['browser'],
                        region=row['region']
                    )
                    clients.append(client)
        except FileNotFoundError:
            print(f"Ошибка: Файл {self.input_file} не найден.")
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
        return clients

    def save_descriptions_to_txt(self, descriptions):

        try:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                for description in descriptions:
                    f.write(description + '\n')
            print(f"Описание успешно сохранено в {self.output_file}")
        except Exception as e:
            print(f"Ошибка при записи в файл: {e}")

    def process(self):

        clients = self.load_csv()
        descriptions = [client.get_description() for client in clients if client]
        self.save_descriptions_to_txt(descriptions)


if __name__ == "__main__":
    input_file = 'web_clients_correct.csv'  # Путь к файлу CSV
    output_file = 'clients_descriptions.txt'  # Путь к файлу для записи текстов
    processor = ClientDataProcessor(input_file, output_file)
    processor.process()
