# Log file parser
path = "Module_1/W2/assets/"
def parse_log_file(log_file, output_file):
    """Parse a log file and extract error messages"""
    try:
        with open(log_file, 'r') as infile, open(output_file, 'w') as outfile:
            error_count = 0
            warning_count = 0
            
            for line_num, line in enumerate(infile, 1):
                if 'ERROR' in line:
                    outfile.write(f"Line {line_num}: {line.strip()}\n")
                    error_count += 1
                elif 'WARNING' in line:
                    warning_count += 1
            
            outfile.write(f"\nSummary:\n")
            outfile.write(f"Total Errors: {error_count}\n")
            outfile.write(f"Total Warnings: {warning_count}\n")
            
            print(f"Parsed {log_file}. Found {error_count} errors and {warning_count} warnings.")
            
    except FileNotFoundError:
        print("Log file not found!")
    except Exception as e:
        print(f"Error: {e}")

# Test the function
parse_log_file(path+'app.log', path+'errors.txt')