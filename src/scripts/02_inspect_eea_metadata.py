
from pathlib import Path

file_path = Path("data/raw/eea/eea_measurements_metadata.csv")

print("Inspecting downloaded EEA file...\n")

if not file_path.exists():
    print("File not found:", file_path.resolve())
else:
    print("File size:", file_path.stat().st_size, "bytes")

    with open(file_path, "r", encoding="utf-8-sig") as file:
        for line_number, line in enumerate(file, start=1):
            if line_number <= 10 or 45 <= line_number <= 52:
                print(f"Line {line_number}: {line.rstrip()[:500]}")
