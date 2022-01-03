# SF28_Final_test_task_Skillfactory
Финальный тестовый проект SkillFactory курса QAP

Автоматизированное тестирование UI сайта: https://besttea.ru/ с использованием PyTest и Selenium.
____________________________________________________________________________________________________

1. С тест-кейсами можно ознакомиться по ссылке: https://docs.google.com/spreadsheets/d/1ivsgIKMrdE2ECkFyFxpjPVEXgecPAIRF6Vv8-AXlkj4/edit?usp=sharing

2. В папке **pages** в файле **base_page.py** находится конструктор webdriver и общие для всех тестируемых страниц методы.
3. В папке **pages** в файлах **cart_page.py, main_page.py, search_page.py** находятся методы для соответствующих тестируемых страниц.
4. В папке **pages** в файле **"locators.py** находятся все локаторы.

5. В корне проекта в файле **conftest.py** находится фикстура с функцией открытия и закрытия браузера.
Для запуска тестов необходимо поменять путь до webdriver на свой.
6. В корне проекта в файле **pytest.ini** зарегистрированны метки маркеровок тестов.
7. В корне проекта в файле **requirements.py** описаны используемые библиотеки.
8. В корне проекта в файлах **test_cart_page.py, test_main_page.py, test_search_page.py** находятся тесты.
Все тесты помечены номером который совпадает с номером тест-кейса в файле: https://docs.google.com/spreadsheets/d/1ivsgIKMrdE2ECkFyFxpjPVEXgecPAIRF6Vv8-AXlkj4/edit?usp=sharing
Во всех файлах с тестами находятся закомментированные команды для запуска тестов из командной строки (#  pytest -v --tb=line test_main_page.py)


