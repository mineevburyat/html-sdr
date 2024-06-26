# python_hackrf

python_hackrf is a cython wrapper for hackrf (https://github.com/greatscottgadgets/hackrf).

You can install this library using
```
pip install python_hackrf
```
Or assemble it manually using the following steps:

In order to build the library you need to go to the python_hackrf directory
```
cd python_hackrf
```
call
```
python setup.py build_ext --inplace.
```
If the build fails, you will need to specify the paths for the libusb library.
```
CFLAGS="-I/path to libusb.h" \
LDFLAGS="-L/path to libusb-1.0.so" \
python setup.py build_ext --inplace
```
## Requirements:
* libusb-1.0 (https://github.com/libusb/libusb)
* Cython==0.29.36
* Numpy>=1.26
* Scipy (optional, for faster work)
* pyFFTW (optional, for faster work)

## hackrf:
Almost all the functionality of the standard library is implemented. Some features will be added later. (operacake).

## hackrf tools:
* hackrf_clock.c (Not implemented)
* hackrf_cpldjtag.c (Not implemented)
* hackrf_debug.c (Not implemented. But functions for this are implemented)
* hackrf_info.c (Implemented + additionally added output of only serial numbers)
* hackrf_operacake.c (Not implemented and the functions are also not implemented. Will be added in the future)
* hackrf_spiflash.c (Not implement. I won’t implement them because this is a dangerous zone)
* hackrf_sweep.c (Implemented)
* hackrf_transfer.c (Not implemented. Will be added in the future)

## usage
```
usage: python_hackrf [-h] {info, sweep, operacake} ...

python_hackrf is a Python wrapper for libhackrf and hackrf-tools.

options:
  -h, --help            show this help message and exit

Available commands:
  {info,operacake,sweep}
    info                Read device information from HackRF such as serial number and firmware version.
    operacake           Specify either list, mode, or GPIO test option.
    sweep               a command-line spectrum analyzer.
```
```
usage: python_hackrf info [-h] [-f] [-s]

options:
  -h, --help            show this help message and exit
  -f, --full            show info like in hackrf_info
  -s, --serial_numbers  show only founded serial_numbers
```
```
usage: python_hackrf sweep [-h] [-d] [-a] [-f] [-p] [-l] [-g] [-w] [-1] [-N] [-B] [-s] [-SR] [-BF] [-r]

options:
  -h, --help  show this help message and exit
  -d          serial_number. serial number of desired HackRF
  -a          amp_enable. RX RF amplifier. If specified = Enable
  -f          freq_min:freq_max. minimum and maximum frequencies in MHz start:stop or start1:stop1,start2:stop2 (MAX_SWEEP_RANGES = 10)
  -p          antenna_enable. Antenna port power. If specified = Enable
  -l          gain_db. RX LNA (IF) gain, 0 - 40dB, 8dB steps
  -g          gain_db. RX VGA (baseband) gain, 0 - 62dB, 2dB steps
  -w          bin_width. FFT bin width (frequency resolution) in Hz, 245-5000000 Depends on sample rate min= sample rate * 1e6 / 8180, max = sample_rate
              * 1e6 / 4
  -1          one shot mode. If specified = Enable
  -N          num_sweeps. Number of sweeps to perform
  -B          binary output. If specified = Enable
  -s          sweep style ("L" - LINEAR, "I" - INTERLEAVED). Default is INTERLEAVED
  -SR         sample rate in Hz (2, 4, 6, 8, 10, 12, 14, 16, 18, 20). Default is 20000000
  -BF         baseband filter bandwidth in Hz (1.75, 2.5, 3.5, 5.0, 5.5, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 15.0 20.0, 24.0, 28.0). Default is
              15000000
  -r          filename. output file
```
```
usage: python_hackrf operacake [-h] [-d] [-o] [-m] [-a] [-b] [-f] [-t] [-w] [-l] [-g]

options:
  -h, --help       show this help message and exit
  -d               serial_number. serial number of desired HackRF
  -o , --address   specify a particular Opera Cake by address. Default is 0
  -m , --mode      specify switching mode [options: manual, frequency, time]
  -a               set port connected to port A0
  -b               set port connected to port B0
  -f               <port:min:max> or <port:min:max>,<port:min:max> automatically assign <port> for range <min:max> in MHz.
  -t               <port:dwell> or <port:dwell>,<port:dwell> in time mode, dwell on <port> for <dwell> samples. Specify only <port> to use the default
                   dwell time (with -w).
  -w               set default dwell time in samples for time mode
  -l, --list       list available Opera Cake boards
  -g, --gpio_test  test GPIO functionality of an Opera Cake
```
## Note
This library can work on android. To do this, go to the android directory and download two recipes for p4a.
## Examples
Examples will be added later.
