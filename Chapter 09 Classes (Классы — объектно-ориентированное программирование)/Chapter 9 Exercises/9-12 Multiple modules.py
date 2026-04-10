import class_admin_privileges

alexey = class_admin_privileges.Admin('alexey', 'polyachenko', 33, 'male')
alexey.privileges.privileges = ['разрешено добавлять сообщения',
                        'разрешено удалять пользователей',
                        'разрешено банить пользователей']
alexey.privileges.show_privileges()