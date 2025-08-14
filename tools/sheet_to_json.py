#!/usr/bin/env python3
import csv, json, sys


if len(sys.argv) < 3:
    print("Usage: sheet_to_json.py input.csv output.json")
    sys.exit(1)

inp, outp = sys.argv[1], sys.argv[2]
rows = []
with open(inp, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for r in reader:
        # Expect columns: type,name,lat,lon,address,phone,hours,languages (comma-separated)
        r['lat'] = float(r.get('lat', 0) or 0)
        r['lon'] = float(r.get('lon', 0) or 0)
        if 'languages' in r and r['languages']:
            r['languages'] = [x.strip() for x in r['languages'].split(',') if x.strip()]
        else:
            r['languages'] = []
        rows.append(r)
with open(outp, 'w', encoding='utf-8') as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)
print(f"Wrote {len(rows)} records to {outp}")
