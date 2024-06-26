# Bitcoin Sync Progress Script

This Python script provides a visual representation of the Bitcoin node synchronization progress. 
It displays a text-based progress bar in the console, along with the percentage of completion and an estimated time to completion.

## Features

- Real-time progress bar
- Percentage of completion
- Estimated Time of Arrival (ETA) for sync completion
- Updates every minute

## Requirements

- Python 3.6 or higher
- `bitcoin-cli` accessible from the command line
- A running Bitcoin node

## Installation

1. Ensure you have Python 3 installed on your system. You can check by running:
   ```
   python3 --version
   ```

2. If Python is not installed, you can install it on Raspberry Pi OS Lite with:
   ```
   sudo apt update
   sudo apt install python3
   ```

3. Clone this repository or download the `bitcoin_sync_progress.py` file.

4. Make the script executable:
   ```
   chmod +x bitcoin_sync_progress.py
   ```

## Usage

1. Ensure your Bitcoin node is running and fully operational.

2. Run the script:
   ```
   ./bitcoin_sync_progress.py
   ```

   Or, if you prefer:
   ```
   python3 bitcoin_sync_progress.py
   ```

3. The script will display a progress bar and update every minute:
   ```
   Bitcoin Sync Progress:
   [||||||||||                                        ] 20.00% ETA: 2d 5h 30m
   ```

4. The script will automatically terminate once the sync reaches 99.99% completion.

## Notes

- The ETA calculation becomes more accurate over time as more data points are collected. It may fluctuate significantly at the beginning of the sync process.
- Ensure that `bitcoin-cli` is in your system's PATH or provide the full path to `bitcoin-cli` in the script.

## Troubleshooting

If you encounter any issues:

1. Ensure your Bitcoin node is running and `bitcoin-cli` is operational.
2. Check that you have the necessary permissions to run `bitcoin-cli`.
3. If you get a "command not found" error, ensure `bitcoin-cli` is in your system's PATH or update the script with the full path to `bitcoin-cli`.

## Contributing

Contributions, issues, and feature requests are welcome. 

## License

[MIT](https://choosealicense.com/licenses/mit/)
