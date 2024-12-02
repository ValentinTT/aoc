from utils import read_file
from part01 import report_is_safe

def main():
    safe_reports = 0
    reports = read_file()
    
    # for report in reports:
    #    for i in range(len(report)):
    #        if report_is_safe(report[:i] + report[i+1:]):
    #            safe_reports += 1
    #            break 

    for report in reports:
        if check_ommiting(report, 0):
            safe_reports += 1
            continue
        n = len(report)

        for i in range(n-1):
            diff1 = report[i+1] - report[i]
            if abs(diff1) > 3 or abs(diff1) < 1:
                if check_ommiting(report, i) or check_ommiting(report, i+1):
                    safe_reports += 1
                break
            
            if i + 2 >= n:  
                continue         
            diff2 = report[i+2] - report[i+1]
            if (diff1 > 0) == (diff2 > 0):
                continue
            
            if (check_ommiting(report, i) 
                or check_ommiting(report, i+1) 
                or check_ommiting(report, i+2)):
                safe_reports += 1
            break

    return safe_reports

def check_ommiting(report, i):
    return report_is_safe(report[:i] + report[i+1:])

if __name__ == "__main__":
   print(f"number of safe reports: {main()}") # 409