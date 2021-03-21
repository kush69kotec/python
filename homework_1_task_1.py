duration=int(input('Введите количество секунд: '))
if duration < 60:
    print(duration, 'секунд')
elif duration < 3600:
    print((duration // 60), 'минут', (duration % 60), 'секунд')
elif duration <= 86400:
    print((duration) // 3600, 'часов', ((duration % 3600) // 60), 'минут', ((duration % 3600) % 60), 'секунд')
elif duration > 86400:
    print((duration // 86400), 'дней', (((duration) % 86400) // 3600), 'часов', ((duration % 3600) // 60), 'минут', ((duration % 3600) % 60), 'секунд')
