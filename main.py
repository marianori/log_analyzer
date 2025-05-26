from log_analyzer import log_analyzer  


result = log_analyzer("server_logs.txt")
if result:
    print("Log Analysis Report")
    print("===================")
    for key in result:
        entries = result[key]
        print(f"{key} ({len(entries)} entries):")
        for line in entries:
            print(line)
        print()
