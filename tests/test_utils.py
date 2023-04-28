from src.operation_class import Operation
from src.utils import get_last_operations, show_operations


def test_get_last_operations():
    assert get_last_operations('src/operations.json', 5)[0].__dict__ == Operation(667307132,
                                                                                  state='EXECUTED',
                                                                                  date="2019-07-13T18:51:29.313309",
                                                                                  amount={
                                                                                      "amount": "97853.86",
                                                                                      "currency": {
                                                                                          "name": "руб.",
                                                                                          "code": "RUB"
                                                                                      }
                                                                                  },
                                                                                  description="Перевод с карты на счет",
                                                                                  sender_acc="Maestro 1308795367077170",
                                                                                  recipient_acc=
                                                                                  "Счет 96527012349577388612"). \
        __dict__ and get_last_operations('src/operations.json', 5)[1].__dict__ == Operation(957763565,
                                                                                            state='EXECUTED',
                                                                                            date="2019-01-05T00:52:30.108534",
                                                                                            amount={
                                                                                                "amount": "87941.37",
                                                                                                "currency": {
                                                                                                    "name": "руб.",
                                                                                                    "code": "RUB"
                                                                                                }
                                                                                            },
                                                                                            description="Перевод со счета на счет",
                                                                                            sender_acc="Счет 46363668439560358409",
                                                                                            recipient_acc=
                                                                                            "Счет 18889008294666828266"). \
               __dict__ and get_last_operations('src/operations.json', 5)[2].__dict__ == Operation(207126257,
                                                                                                   state='EXECUTED',
                                                                                                   date="2019-07-15T11:47:40.496961",
                                                                                                   amount={
                                                                                                       "amount": "92688.46",
                                                                                                       "currency": {
                                                                                                           "name": "USD",
                                                                                                           "code": "USD"
                                                                                                       }
                                                                                                   },
                                                                                                   description="Открытие вклада",
                                                                                                   sender_acc="---",
                                                                                                   recipient_acc=
                                                                                                   "Счет 35737585785074382265"). \
               __dict__ and get_last_operations('src/operations.json', 5)[3].__dict__ == Operation(921286598,
                                                                                                   state='EXECUTED',
                                                                                                   date="2018-03-09T23:57:37.537412",
                                                                                                   amount={
                                                                                                       "amount": "25780.71",
                                                                                                       "currency": {
                                                                                                           "name": "руб.",
                                                                                                           "code": "RUB"
                                                                                                       }
                                                                                                   },
                                                                                                   description="Перевод организации",
                                                                                                   sender_acc="Счет 26406253703545413262",
                                                                                                   recipient_acc=
                                                                                                   "Счет 20735820461482021315"). \
               __dict__ and get_last_operations('src/operations.json', 5)[4].__dict__ == Operation(179194306,
                                                                                                   state='EXECUTED',
                                                                                                   date="2019-05-19T12:51:49.023880",
                                                                                                   amount={
                                                                                                       "amount": "6381.58",
                                                                                                       "currency": {
                                                                                                           "name": "USD",
                                                                                                           "code": "USD"
                                                                                                       }
                                                                                                   },
                                                                                                   description="Перевод организации",
                                                                                                   sender_acc="МИР 5211277418228469",
                                                                                                   recipient_acc=
                                                                                                   "Счет 58518872592028002662").__dict__


def test_show_operations():
    assert show_operations(get_last_operations('src/operations.json', 1)) == '2019.07.13 Перевод с карты на счет\n' \
                                                                             'Maestro 1308 79** **** 7170 -> Счет **8612\n' \
                                                                             '97853.86 руб.\n'
