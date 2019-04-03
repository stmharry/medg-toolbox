import json
import os
import pandas as pd
import schedule
import subprocess
import time


hosts = ['nightingale', 'harrison', 'gray']
tsv_path = 'log.tsv'


def main():
    print(time.time())
    for host in hosts:
        print(host)

        json_str = subprocess.check_output(['ssh', f'stmharry@{host}.csail.mit.edu', 'gpustat --json']).decode()
        json_obj = json.loads(json_str)

        df = pd.io.json.json_normalize(
            json_obj,
            ['gpus', 'processes'],
            [
                'hostname',
                'query_time',
                ['gpus', 'index'],
                ['gpus', 'name'],
                ['gpus', 'uuid'],
                ['gpus', 'memory.total'],
                ['gpus', 'memory.used'],
                ['gpus', 'temperature.gpu'],
                ['gpus', 'utilization.gpu'],
                ['gpus', 'enforced.power.limit'],
                ['gpus', 'power.draw'],
            ],
        )
        print(df)

        flag = os.path.isfile(tsv_path)
        df.to_csv(
            tsv_path,
            mode='a' if flag else 'w',
            header=not flag,
            index=False,
            sep='\t',
        )


schedule.every(10).seconds.do(main)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)
