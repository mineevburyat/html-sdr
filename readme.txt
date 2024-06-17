Дата: 08 Сен 2018 14:14:29 · Поправил: DVE (08 Сен 2018 14:15:49) #  

Sinus, спасибо, интересно. А есть примеры с реальными спектрами, лучше оно получается чем простое FFT?

2 All:
Может кому интересно, добавил поддержку "свистка" в программу сохранения спектра, теперь можно сохранять спектр любой ширины.
Ссылка:
https://www.dropbox.com/s/qf9upcmypg3blpo/Waterfall2ImgV1.0b7.zip?dl=0

Написана на python, для работы требуется пакет SoapySDR (инсталлятор под Windows http://downloads.myriadrf.org/builds/PothosSDR/?C=M;O=D )

Пример использования: спектр авиадиапазона за 20 минут:
Команда:
python3 wf2img.py --fStart=118000000 --fEnd=137000000 --sr=2048000 --sdr=rtlsdr --average=1 --imagewidth=512 --sdrgain="TUNER:26"

(imagewidth - ширина одного "куска", соответствующий полосе sr, average - усреднение, fStart, fEnd - частоты)

Результат (уменьшено иначе не влезает в "копилку"):

Увеличить

Известные недоработки:
- не очень понятно как выравнивать уровни если сигналы в разных окнах сильно отличаются по мощности
- нет временных меток на спектре


+++++++++++++++++++++++++++++++++++++
Коллеги, обращаюсь с дилетантским вопросом. На спектрограммах, вычисленных по I/Q типичная шкала - в децибеллах ослабления сигнала. Т.е. от 0 и далее в отрицательную сторону.

Возьмем пример. I/Q поток разрядностью 16 бит на канал. Т.е. значения и мнимой и реальной частей от -215 до +215. Посчитали спектр допустим с окном в 1024.

Как теперь получить эти самые отрицательные децибелы?

20*log10(val) ?

Наберите в гугле fft to decibel, будет много полезных ссылок.

https://www.radioscanner.ru/forum/topic44541-35.html

https://ru.dsplib.org/

python src/pyspectrum.py -isoapy:hackrf -s20e6 -c2.462e9

ELRS
https://github.com/aerror2/erfly6
https://www.youtube.com/watch?v=55v1r1wTus4

https://www.youtube.com/watch?v=5fdJDCO51hc

DDC SDR
http://www.cqham.ru/forum/showthread.php?26291-%D7%F2%EE-%F2%E0%EA%EE%E5-DDC-SDR-%EB%E8%EA%E1%E5%E7-%E4%EB%FF-%ED%E0%F7%E8%ED%E0%FE%F9%E8%F5&s=82040d3cd80e96a1f304d4d575671ccd
https://ru.dsplib.org/content/complex/complex.html
https://habr.com/ru/articles/204310/

https://www.youtube.com/watch?v=c5mG7jv0JgA&list=PLmu_y3-DV2_kpP8oX_Uug0IbgH2T4hRPL&index=12