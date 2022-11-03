-link# Тестовое задание


Telegram-bot на асинхронной библиотеке aiogram. 

Служит для сбора информации от пользователя и дальшейшего заполнения формы обратной связи на сайте.

## How to Start

Данный бот был размещен на типовом VPS сервере (vdsina). Сервер на ubuntu 20.04.

## Первоначальная настройка и виртуальное окружение

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

Использовать конфиг для автоматического запуска "tgbot.service"

Мы копируем конфиг из кореквой директории проекта и перемещаеи ее в нужную папку (из-под root)

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


## Установка хром

### Примечание

Не подойдет самая слабая конфигурация сервера (1 ядро, 1гб ОЗУ), так как хром берет на себя достаточное количество ресурсов, чтобы выскочила ошибка: Out of memory: killed procecc ... .



## Contacts

- E-Mail: [forwotk31415@gmail.com](mailto:andrew.kachanov@gmail.com)
- Telegram: [@lipp260](https://t.me/lipp260)

  
  ```
$ flutter packages pub run build_runner build --delete-conflicting-outputs
$ cd data && docker-compose up -d
```
