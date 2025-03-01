# gateway.py
import requests


def main():
    # Sample text input from [main.py](http://_vscodecontentref_/6) snippet (in Russian)
    text = (
        "Тем не менее, парадигма цифровой экономики открывает новые возможности практического применения цифровых следов граждан. "
        "Соответственно, совокупность сквозных технологий открывает новые возможности универсальной коммодитизации волатильных активов. "
        "Следовательно, программа прорывных исследований несёт в себе риски практического применения государственно-частных партнёрств.  \n\n"
        "Следовательно, ускорение блокчейн-транзакций расширяет горизонты универсальной коммодитизации знаний и компетенций. "
        "Вместе с тем, прагматичный подход к цифровым платформам не оставляет шанса для нормативного регулирования непроверенных гипотез. "
        "Следовательно, прагматичный подход к цифровым платформам повышает вероятность бюджетного финансирования волатильных активов."
    )

    # Call Text Processing Microservice
    response = requests.post(
        "http://localhost:5001/process", json={"text": text})
    sentences = response.json().get('sentences', [])

    # Call Table Builder Microservice with processed sentences
    response_tb = requests.post(
        "http://localhost:5002/build_table", json={"sentences": sentences})
    table = response_tb.json().get('table', [])

    # Print the table directly
    for row in table:
        print(" | ".join(row))


if __name__ == '__main__':
    main()
