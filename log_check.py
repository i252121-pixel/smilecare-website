import csv
import os

def check_suspicious_logs(filename="submissions.csv"):
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found in the current directory.")
        return

    print(f"[*] Scanning '{filename}' for suspicious inputs (containing '<' or '>')...\n")
    
    suspicious_count = 0

    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row_num, row in enumerate(reader, start=1):
            row_content = f"{row.get('timestamp', '')} {row.get('ip_address', '')} {row.get('name', '')} {row.get('email', '')} {row.get('message', '')}"
            
            if '<' in row_content or '>' in row_content:
                suspicious_count += 1
                print(f"[!] SUSPICIOUS ENTRY FOUND (Row {row_num})")
                print(f"    Timestamp : {row.get('timestamp')}")
                print(f"    IP Address: {row.get('ip_address')}")
                print(f"    Name      : {row.get('name')}")
                print(f"    Email     : {row.get('email')}")
                print(f"    Message   : {row.get('message')}")
                print("-" * 60)

    print(f"\n[*] Scan complete. Total suspicious entries flagged: {suspicious_count}")

if __name__ == "__main__":
    check_suspicious_logs()
