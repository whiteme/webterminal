import logging
import telnetlib
import time


if __name__ == '__main__':
    tn = telnetlib.Telnet()
    tn.open("47.105.39.117",port=18182)

    tn.write(b'ls\r\n')
    datas = tn.read_all()
    print(datas)