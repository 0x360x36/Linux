import os

def read_log_file(filepath):
    try:
        with open(filepath, 'r') as file:
            return file.readlines()
    except IOError as e:
        print(f"Error reading {filepath}: {e}")
        return []

def extract_suspicious_log_entries(log_data):
    suspicious_entries = []
    suspicious_keywords = ['failed', 'invalid', 'error', 'unauthorized', 'root']
    
    for line in log_data:
        if any(keyword in line.lower() for keyword in suspicious_keywords):
            suspicious_entries.append(line)
    
    return suspicious_entries

def analyze_logs(log_files):
    all_suspicious_entries = []
    
    for log_file in log_files:
        log_data = read_log_file(log_file)
        suspicious_entries = extract_suspicious_log_entries(log_data)
        all_suspicious_entries.extend(suspicious_entries)
    
    return all_suspicious_entries

if __name__ == "__main__":
    log_files = [
        '/var/log/auth.log',
        '/var/log/syslog',
        '/var/log/messages'
    ]
    
    suspicious_entries = analyze_logs(log_files)
    
    print("Suspicious Log Entries:")
    for entry in suspicious_entries:
        print(entry.strip())
