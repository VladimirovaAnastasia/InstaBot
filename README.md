# Инструмент для конкурсов в Instagram

Скрипт проверяет выполнение стандартных правил участия в конкурсе в Instagram для пользователей:
- Подписался ли пользователь на аккаунт, 
- Поставил ли он лайк,
- Отметил друга.

## Как запустить
 Устанавливаем необходимые библиотеки
 ``pip install requarements.txt`` 
 
 Вводим свои данные от аккаунта Instagram
 ``bot.login(username="YOUR_LOGIN", password="YOUR_PASSWORD")``
 
 Запускаем скрипт
  ``python script.py POST_LINK ACCOUNT_NAME``
  
 POST_LINK - ссылка на пост с конкурсом (обязательный параметр)
 ACCOUNT_NAME - аккаунт, в котором проводится конкурс (необязательный параметр, по умолчанию [kvartal_vocal](https://www.instagram.com/kvartal_vocal/))
 
## Цель проекта
 Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/modules/) 
  
 
  
