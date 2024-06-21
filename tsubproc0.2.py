from subprocess import Popen, PIPE, DEVNULL, STDOUT
from time import sleep, mktime, strptime
from datetime import datetime
import numpy as np

# product
process = Popen(['hackrf_sweep', '-w 200000', '-f 110:6000', '-a 1'], stdout=PIPE, stderr=DEVNULL)
# debug
# out = Popen(['hackrf_sweep', '-f 200:6000', '-1'], stdout=PIPE)

run_str = ['|', '/', '-', '\\']
indx = 0
print('start hackrf_sweep.....')

SNR = 25 # dB
scan_analiz = {}
history = {}
count = 0
try:

    # while process.stderr:
    #     print(process.stderr.readline())
    while process.poll() is None:
        print('\r',run_str[indx], count, end='')
        # print(process.stderr.readline())
        line = process.stdout.readline().split(b', ')
        if len(line) > 2:
            ch_count = len(line) - 6
            powers = np.array([float(item) for item in line[6:]])
            # max_power = powers.max()
            # min_power = powers.min()
            avg = powers.mean()
            # (print(max_power, avg, min_power))
            t = mktime(strptime(line[0].decode() + ', ' + line[1].decode(),
                        "%Y-%m-%d, %H:%M:%S.%f"))
            for index, power in enumerate(powers):
                if power > avg + SNR:
                    freq = float(line[2]) + float(line[4]) * index
                    if freq not in history:
                        history[freq] = [(t, power)]
                    else:
                        history[freq].append((t, power))
                    
                    old_power = scan_analiz.get(freq)

                    if old_power and power > old_power:
                        scan_analiz[freq] = power
                    else:
                        scan_analiz[freq] = power
                        
                    count += 1
        indx = (indx + 1) % len(run_str)
except KeyboardInterrupt:
    sleep(1)
    print('\nstop hackrf.')
for freq, power in scan_analiz.items():
    print(freq/1e6, 'Mhz : ', power, 'dB')

# for freq, t_line in history.items():
#     print(freq/1e6, 'Mhz: ')
#     for stamp in t_line:
#         t_value = datetime.fromtimestamp(stamp[0])
#         print('\t', t_value.strftime("%Y-%m-%d %H:%M:%S"), ': ', stamp[1])

                    