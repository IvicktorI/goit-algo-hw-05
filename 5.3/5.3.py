from pathlib import Path
from prettytable import PrettyTable
import sys

def load_logs(path: str) -> list:
    log_list=[]
    try:
        with open(path, "r", encoding='utf-8') as f:
            log_list=[parse_log_line(el.strip()) for el in f.readlines()]
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print (f"Error: {e}")

    return log_list

def parse_log_line(line: str) -> dict:

    temp=[]
    temp=line.split(' ', 3)
    log={'date':temp[0],'time':temp[1],'level':temp[2],'comments':temp[3]}
    return  log

def filter_logs_by_level(logs: list, level: str) -> list:

    filtered_list = filter(lambda x: x.get('level').lower()==level.lower(), logs)

    return list(filtered_list)

def count_logs_by_level(logs: list) -> dict:

    temp = [el['level'] for el in logs]
    temp_dict=dict.fromkeys(temp,0)
    for el in logs:
        temp_dict[el['level']]+=1

    return temp_dict

def display_log_counts(counts: dict):

    table = PrettyTable()
    table.field_names = ["Level", "Counts"]
    for key in counts:
        table.add_row([key,counts[key]])

    str_out = str(table)
    print(str_out)

def main():
    
    try:
        path=sys.argv[1]
        log_list=load_logs(path)
        if len(sys.argv)==2:
            display_log_counts(count_logs_by_level(log_list))
        else:
            filter=sys.argv[2]
            display_log_counts(count_logs_by_level(log_list))
            filtered_list=filter_logs_by_level(log_list,filter)
            if len(filtered_list)!=0:
                print(f'Info be level {filter}:')
                for el in filtered_list:
                    print(f"{el['date']} {el['time']} - {el['comments']}")
            else:
                print(f'Not found logs with level {filter}')


    except Exception as e:
        print('Incorect path  ',e)
        
    

if __name__ == "__main__":
    main()