# StasGorelik-QAP-Diplom
Diplom

## Запуск тестов в Docker

1. Проверить, что API-сервер запущен локально на порту 8000. и докер запущен
2. Собрать образ:
   ```bash
   docker build -t my-tests .
3. Использовать команду образ:
   ```bash
   запускает тесты и удаляет образ
   docker run --rm -v ${PWD}/.allure-results:/app/.allure-results my-tests

   открыть отчет
   allure serve ./.allure-results

   удалить созданный образ
   docker rmi my-tests