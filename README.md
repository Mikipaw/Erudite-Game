# Erudite game
I'm so sorry, but English version of `README.md` will be created after verification by 
my teacher [David](https://github.com/oxygeniswonderful). 

# Игра "Эрудит"

"Эрудит" - это игра, в которой игроку нужно за ограниченное время составлять как можно более сложные слова из букв,
 которые предоставляет компьютер.

## Установка

Для игры "Эрудит" необходимо установить Python версии 3.7 или выше.


## Запуск игры

Для запуска игры нужно запустить файл `erudite_game_vs_comp.py`. Для этого откройте терминал или командную строку в папке с игрой и выполните следующую команду:

```
python erudite_game_vs_comp.py
```


## Правила игры

1. Игрокам предоставляется набор букв.
2. Игроки должны составлять слова из предоставленных букв.
3. За каждое правильно составленное слово игрок получает определенное количество очков.
4. Игра заканчивается, когда заканчиваются буквы или когда время хода истекает.
5. Побеждает игрок с наибольшим количеством очков.

## Как играть

1. Запустите игру, следуя инструкциям в разделе "Запуск игры".
2. Игра начнется автоматически.
3. Введите слово из предоставленных букв и нажмите Enter.
4. Если слово верно, то вы получите определенное количество очков.
5. Если слово неверно, то вы не получите очков и должны ввести новое слово.
6. Игра закончится, когда закончится время или когда закончатся буквы.
7. После окончания игры будет выведено сообщение о победителе и количестве набранных очков.

## Настройки игры

* Если вы хотите изменить количество букв, выдаваемых вам компьютером в каждом раунде, 
измените значение глобальной переменной `HAND_SIZE`.
* Если вы хотите поменять язык в игре, поместите файл со словами вашего языка в директорию проекта
 и поменяйте значение переменной `WORDLIST_FILENAME` с `words.txt` на название своего файла, а также
не забудьте поменять алфавит (глобальные переменные `CONSONANTS` и `VOWELS`).
* Изменить стоимость каждой буквы можно с помощью изменения списка `SCRABBLE_LETTER_VALUES`.
* Также можно изменить количество бонусных очков и времени раунда 
через глобальные переменные `BONUS_PTS` и `DEFAULT_TIME` соответственно. 

## Лицензия

Этот проект распространяется на условиях лицензии GNU. Подробности смотрите в файле LICENSE.
