import os
import glob
import time

def run():
    os.system('~/dev/flent/run-flent rtt_fair_up -l 60 -H p1 -H p3 -H p4 -H p5 -L logs')
    time.sleep(5)
    target = glob.glob('*.gz')[0]
    os.system(f'mv logs {target}.log')
    os.system('mv *.gz *.log stock/rtt_fair_up_cs0')


if __name__ == '__main__':
    for i in range(5):
        run()

