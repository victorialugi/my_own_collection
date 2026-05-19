# Yandex Cloud ELK Collection
Домашнее задание к занятию "Создание собственных модулей" - Лугинина Виктория
## Содержимое 

- **Модуль**: `my_own_module` — создаёт файл на удалённом хосте
- **Роль**: `create_file` — использует мой модуль для создания файла

## Использование

```yaml
- name: Create file
  hosts: localhost
  roles:
    - create_file

## Автор
Victoria Luginina

## Версия
1.0.0
