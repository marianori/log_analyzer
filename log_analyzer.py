def log_analyzer(filename):
    try:
        with open(filename, 'r') as file:
            logs = file.readlines()
        
        result = {
            'ERROR': [],
            'WARNING': [],
            'INFO': []
        }

        for line in logs:
            line = line.strip()
            if line.startswith('[ERROR]'):
                result['ERROR'].append(line)
            elif line.startswith('[WARNING]'):
                result['WARNING'].append(line)
            elif line.startswith('[INFO]'):
                result['INFO'].append(line)
        
        return result
    
    except FileNotFoundError:
        print(f"File {filename} is not found. Please check the file path.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
