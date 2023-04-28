from path_to_op_list import PATH
from utils import get_last_operations, show_operations


def main():
    client_name = input('Пожалуйста, введите Ваше имя:\n')
    print(f'Приветствую, {client_name} в приложении нашего банка!')
    count_op_user_input = int(input('Пожалуйста, введите количество операций, которые необходимо вывести:\n'))
    requsted_operations = get_last_operations(PATH, count_op_user_input)
    print(f'Ваши последние {count_op_user_input} выполненных операций:\n')
    print(show_operations(requsted_operations))


if __name__ == '__main__':
    main()