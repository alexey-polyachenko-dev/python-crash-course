import import_class as ic

alexey = ic.Admin('alexey', 'polyachenko', 33, 'male')
alexey.privileges.privileges = ['разрешено добавлять сообщения',
                        'разрешено удалять пользователей',
                        'разрешено банить пользователей']
alexey.privileges.show_privileges()