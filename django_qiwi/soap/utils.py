#coding:utf8

STATUS_CODE_TEXT = (
    (0, u'Успех'),
    (13, u'Сервер занят, повторите запрос позже'),
    (150, u'Ошибка авторизации (неверный логин/пароль)'),
    (210, u'Счет не найден'),
    (215, u'Счет с таким txn-id уже существует'),
    (241, u'Сумма слишком мала'),
    (242, u'Превышена максимальная сумма платежа – 15 000р.'),
    (278, u'Превышение максимального интервала получения списка счетов'),
    (298, u'Агента не существует в системе'),
    (300, u'Неизвестная ошибка'),
    (330, u'Ошибка шифрования'),
    (370, u'Превышено максимальное кол-во одновременно выполняемых запросов'),
    (50, u'Выставлен'),
    (52, u'Проводится'),
    (60, u'Оплачен'),
    (150, u'Отменен (ошибка на терминале)'),
    (160, u'Отменен'),
    (161, u'Отменен (Истекло время)'),
)
