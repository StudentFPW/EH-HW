import requests


def main():
    file_extensions = []
    url = "https://www.hackthissite.org/"
    extension = "/"
    file_name = "./common-files.txt"
    found_links = []

    while True:
        name = input("Введите расширение файла - (нажмите Enter для завершения):\t")
        if name:
            file_extensions.append(name)
        else:
            break

    print("Введенные расширения файлов:", file_extensions)

    try:
        file = open(file_name, "rt")
        links = file.readlines()
        file.close()
    except Exception as e:
        print(f"Ошибка: {e}")

    if not links:
        print("Нет ссылок для проверки")
        return

    for link in links:
        link = link.strip()

        for ext in file_extensions:
            if link.endswith(ext):
                full_link = f"{url}{link}{extension}"
                print(f"Вариант - {full_link}")

                try:
                    response = requests.get(full_link)
                    if response.status_code != 404:
                        print(f"Существует - {full_link}")
                        found_links.append(full_link)
                except requests.RequestException as e:
                    print(f"Ошибка при запросе {full_link}: {e}")

    if found_links:
        try:
            result_file = open("file.txt", "w")
            for found_link in found_links:
                result_file.write(found_link + "\n")
            result_file.close()
            print("Результаты успешно сохранены в file.txt")
        except Exception as e:
            print(f"Ошибка: {e}")
    print("Пробуйте снова!")


if __name__ == "__main__":
    main()
