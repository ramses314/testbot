# Тестовое задание

[Telegram-bot](https://t.me/mitty44bot) на асинхронной библиотеке aiogram. 

Служит для сбора информации от пользователя и дальшейшего заполнения формы обратной связи на сайте.

## Как установить бота

Данный бот был размещен на типовом VPS сервере (vdsina). Сервер на ubuntu 20.04.

## Первоначальная настройка и виртуальное окружение

Сначала вам нужно зарегистрировать своего бота в @BotFather, после чего получите уникальный токен,
который нужно будет вписать в файл .env в главной директории проекта (в переменную TOKEN)

Выполнить в консоле сервера при первом включении:

```
$ apt update
$ apt install -y htop git build-essential libssl-dev libffi-dev python3-pip python3-dev python3-setuptools python3-venv 
```

Создать пользователя и переключиться на него:

```
$ adduser someuser
$ su - someuser
```

Клонировать репозиторий:

```
$ cd /home/someuser
$ git clone https://github.com/ramses314/testbot.git
```

Создать вирутальное окружение:

```
$ cd /home/someuser/testbot
$ python3 -m venv .venv
```

Активировать вирутальное окружение и установить пакеты:

```
$ source /home/someuser/testbot/.venv/bin/activate
$ pip install -r /home/someuser/testbot/pip-requirements.txt
```

Использовать конфиг для автоматического запуска "tgbot.service". Мы копируем конфиг из кореквой директории проекта и перемещаеи ее в нужную папку (из-под root)

```
$ sudo cp /home/someuser/testbot/tgbot3.service /etc/systemd/system/tgbot3.service
```
Запустить/остановить/статус бота:
```
$ sudo systemctl start tgbot3
$ sudo systemctl stop tgbot3
$ sudo systemctl status tgbot3
```

## Установка postgres
```
sudo apt -y install postgresql
```
Далее вам нужно зайти в БД postgres под юзером postgres (они создаются автоматически при установке), и установить пароль для БД

Примечание, если вы установите пароль отличный от того что представлен ниже, то не забудьте указать его в файе data/config.py
```
$ sudo -u postgres psql postgres

$ ALTER USER postgres WITH PASSWORD 'gtx97';
```

## Установка хром

Телеграм-бот отправлякт форму на сайте с помощью пакета selenium, которому необходимо установить релевантный браузер.

```
$ wget https://dl.google.com/linux/direct/google-chrome-stable_current_i386.deb
$ sudo dpkg -i google-chrome-stable_current_i386.deb
```
### Примечание

Не подойдет самая слабая конфигурация сервера (1 ядро, 1гб ОЗУ), так как хром берет на себя достаточное количество ресурсов, чтобы выскочила ошибка: Out of memory: killed procecc ... .



## Contacts

- E-Mail: forwotk31415@gmail.com
- Telegram: [@lipp260](https://t.me/lipp260)

 
