import pandas as pd
from Data_checking import Data_check

def main():
    import pandas as pd
# Импортируем класс Data_check из вашего файла Data_checking.py
from Data_checking import Data_check

def main():
    pd.DataFrame({'A': [1, 'текст', 3.4],'B': ['привет', 'мир', 'тест'],'C': [1.5, 2.3, 4.0]}).to_csv('var1.csv', index=False)
    pd.DataFrame(columns=['A', 'B', 'C']).to_csv('empty.csv', index=False)
    pd.DataFrame({'Unnamed: 0':, 'A':, 'B':,'C': ['текст'],'D': [True]}).to_csv('broken.csv', index=False)
    print("Тестовые файлы успешно сгенерированы.\n")
    print("Демонстрируем вывод ошибок\n")
    print("1. Пример сообщения об ошибке с отсутствием файла:")
    check_missing = Data_check('var18.csv')
    check_missing.process()
    print("\n 2. Пример сообщения об ошибке пустого файла:")
    check_empty = Data_check('empty.csv')
    check_empty.process()
    print("\n 3. Пример сообщения об ошибке формата файла:")
    check_broken = Data_check('broken.csv')
    check_broken.process()
    print("\n 4. Пример успешного завершения программы:")
    check_success = Data_check('var1.csv')
    check_success.process()


if __name__=="__main__":
    main()
