#!/usr/bin/env python3
import subprocess
import json
import time
from datetime import timedelta

def get_verification_progress():
    try:
        result = subprocess.run(['bitcoin-cli', 'getblockchaininfo'], capture_output=True, text=True)
        blockchain_info = json.loads(result.stdout)
        return blockchain_info['verificationprogress']
    except Exception as e:
        print(f"Error getting blockchain info: {e}")
        return None

def progress_bar(progress, length=50, fill='|'):
    filled_length = int(length * progress)
    bar = fill * filled_length + ' ' * (length - filled_length)
    return f'[{bar}]'

def format_time(seconds):
    days, remainder = divmod(int(seconds), 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, _ = divmod(remainder, 60)
    if days > 0:
        return f"{days}d {hours}h {minutes}m"
    elif hours > 0:
        return f"{hours}h {minutes}m"
    else:
        return f"{minutes}m"

def main():
    print("Bitcoin Sync Progress:")
    start_time = time.time()
    start_progress = get_verification_progress()
    
    if start_progress is None:
        print("Unable to fetch initial progress. Exiting.")
        return

    while True:
        current_progress = get_verification_progress()
        if current_progress is not None:
            percent = current_progress * 100
            bar = progress_bar(current_progress)
            
            elapsed_time = time.time() - start_time
            progress_made = current_progress - start_progress
            if progress_made > 0:
                estimated_total_time = elapsed_time / progress_made
                estimated_remaining_time = estimated_total_time - elapsed_time
                eta = format_time(estimated_remaining_time)
            else:
                eta = "Calculating..."

            print(f'\r{bar} {percent:.2f}% ETA: {eta}      ', end='', flush=True)
            
            if percent >= 99.99:
                print("\nSync completed!")
                break
        else:
            print("\rUnable to fetch progress. Retrying...", end='', flush=True)
        
        time.sleep(60)

if __name__ == "__main__":
    main()
