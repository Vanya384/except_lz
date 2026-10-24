import os
import pandas as pd

class Data_check():

  def __init__(self, file_path: str):  #file_path означает,что необходимо передать путь к файлу в виде строки
    self.file_path = file_path  #любой объект класса сможет получить доступ к пути через self
    self.expected_schema = {'A': 'any', 'B': 'object', 'C': 'float'}  #создаем колонки нашей схемы :A-элементы любого типа данных;
                                                             #B-тип данных object;
                                                              #C- вещественные числа;


  def process(self):
    if not os.path.exists(self.file_path):  #os.path проверяет наличие файла(по указанному пути),в нашем случае если файла нет,
                                             #то при помощи if мы его инвертируем и получаем какое-то действие далее
      error = FileNotFoundError(2, f"Файл,по указанному адресу не найден: '{self.file_path}\n'")  #FileNotFoundError-встроенный класс ошибки(срабатывает,когда файл не найден)
                                                                                                 #2-код ошибки(файл не найден)
                                                                                                  #далее идет описание ошибки
      print(f'Возникла следующая ошибка: [Errno 2] {error.strerror}\n')
      return

    try:
      df = pd.read_csv(self.file_path)  #сохраняем полученную таблицу в df

      if df.empty:  #проверка таблицы на пустоту(шапка таблицы в счет не идет)
        print('Возникла следующая ошибка: Датафрейм пуст\n')
        return
      
      errors = []  #создаем список(сюда будем закидывать все найденные ошибки или несоответствия)
      actual_columns = list(df.columns)  #все названия столбцов(действительные) заносим в переменную actual_columns
      expected_columns = list(self.expected_schema.keys()) #метод .keys() собирает все названия('A','B' и т.д.)
                                                            #и записываем через list аналогично предыдущей строке их в переменную ожидаемых столбцов

      if actual_columns != expected_columns: #если названия действительные не совпали с ожидаемыми,то выводим ошибку
        errors.append('- Названия столбцов не совпадают.'f"Ожидаемые: {expected_columns}\n"f'Фактические: {actual_columns}\n')

      for col, expected_type in self.expected_schema.items():  #items() разбивает expected_schema таким образом,что col берет в себя названия колонок('A'),
                                                                #а expected_type соответственно тип данных этой колонки(any)

        if col in df.columns:   #проверка,находится ли колонка col среди всех колонок или нет
          actual_type = str( df[col].dtype )  #находим через df[col] колонку кол в таблице, далее смотрим какой тип данных там лежит и записываем его в действительный
          
          if expected_type == 'object':  #если ожидается тип object
          
            display_expected = 'str'     #то надо записать текст str
          else:
            display_expected=expected_type #иначе запишем ожидаемый тип как есть

          if actual_type == 'object':  #если действительный тип object
            display_actual = 'object'  #то запишем object
          
          else:
            display_actual = actual_type #иначе запишем действительный тип как есть

          if actual_type != expected_type and expected_type != 'any':  #сравниваем действительные типы и ожидаемые(а затем инвертируем),а также проверяем ,чтобы в ожидаемом типе был any
            errors.append(f"- В столбце '{col}' тип данных не соответствует ожидаемому.\n"f'Ожидается: {display_expected},\n Фактически: {display_actual}\n')  #выводим ошибку

      if errors: #если errors не пуста
        print('Структура датафрейма не соответствует ожидаемой:')
        print('\n'.join(errors)) #для вывода каждой ошибки с новой строки(.join() выводит ошибки через разделить указанный до него)
        return

      print('\n Чтение датафрейма завершено успешно')
    except pd.errors.EmptyDataError: #срабатывает в случае существования файла,но пустоты внутри(то есть его размер равен 0)
      print('Возникла следующая ошибка: Датафрейм пуст\n')
    except Exception as e:  #если в программе будет некоторая ошибка,которую я не учел,она универсально выведется через e
      print(f'Возникла следующая ошибка: {e}\n')

processor = Data_check('var1.csv')
processor.process()