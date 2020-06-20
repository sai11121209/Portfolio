#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
#サーバ開始:runserver192.168.11.9:8000
#app作成:startapp
#app追加1:mysite/setting.py.INSTALLED_APPSに追記
#app追加2:makemigrations
#テーブル作成:migrate

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    #import pymysql
    #pymysql.install_as_MySQLdb()


if __name__ == '__main__':
    main()
