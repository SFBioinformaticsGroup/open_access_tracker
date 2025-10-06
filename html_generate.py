import csv
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(BASE_DIR, "data", "journals_normalized.csv")
html_file = os.path.join(BASE_DIR, "index.html")
output_file = os.path.join(BASE_DIR, "index.html")

with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    headers = reader.fieldnames
    rows = []
    for row in reader:
        row_data = [row.get(col, "").strip() for col in headers]

        if "Hybrid?" in headers:
            idx = headers.index("Hybrid?")
            row_data[idx] = "Sí" if row_data[idx] in ["Yes", "Sí", "✅", "Hybrid", "✅*"] else "No"
        if "Free Closed‑Access Option" in headers:
            idx = headers.index("Free Closed‑Access Option")
            row_data[idx] = "Sí" if row_data[idx] in ["Yes", "Sí", "✅"] else "No"

        if "Link" in headers:
            idx = headers.index("Link")
            if row_data[idx] not in ["", "Link"]:
                row_data[idx] = f'<a href="{row_data[idx]}" target="_blank">Enlace</a>'
            else:
                row_data[idx] = ""

        rows.append(row_data)

table_rows_html = ""
for r in rows:
    table_rows_html += "<tr>\n"
    for cell in r:
        table_rows_html += f"  <td>{cell}</td>\n"
    table_rows_html += "</tr>\n"

thead_html = "<thead>\n<tr>\n"
for h in headers:
    thead_html += f"  <th>{h}</th>\n"
thead_html += "</tr>\n</thead>"

with open(html_file, encoding='utf-8') as f:
    html_content = f.read()

html_content = re.sub(r'<thead>.*?</thead>', thead_html, html_content, flags=re.DOTALL)
html_content = re.sub(r'(<tbody>).*?(</tbody>)', f'\\1{table_rows_html}\\2', html_content, flags=re.DOTALL)

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"HTML table updated! Output: {output_file}")
