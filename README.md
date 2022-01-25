# wordle_solver
An efficient solver for viral game Worldle!

Worlde solver uses a dictionary of top 5k frequent 5 digit words.<br>
It predicts top 20 words possible based on digit character frequencies and lists top 5 by word frequency.<br>
All of this numbers can be changed on constants.py.

An example run for 'sugar' on 25.01.2022

```
You should predict one of the following:
1. tales: 3410.0 831
2. males: 3406.0 1001
3. bones: 3386.0 1079
4. lanes: 3443.0 1311
5. fares: 3508.0 1374
Your prediction: tales
Result: .-..-
You should predict one of the following:
1. spain: 127.0 281
2. sharp: 126.0 491
3. shark: 131.0 1251
4. sparc: 120.0 1280
5. scary: 123.0 1298
Your prediction: spain
Result: +.-..
You should predict one of the following:
1. sugar: 19.0 513
2. squad: 23.0 999
3. scuba: 22.0 1201
4. sdram: 19.0 1471
5. skoda: 18.0 2944
Your prediction: sugar
Result: +++++
Congratulations you found the word!
```
