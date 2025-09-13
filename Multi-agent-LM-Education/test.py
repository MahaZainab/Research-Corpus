python - <<'PY'
import os, re, textwrap, requests

OWNER="MahaZainab"
REPO="Research-Corpus"
PATH="Multi-agent-LM-Education"

api=f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{PATH}"
tok=os.getenv("GITHUB_TOKEN")
headers={"Accept":"application/vnd.github+json"}
if tok: headers["Authorization"]=f"Bearer {tok}"

resp=requests.get(api, headers=headers, timeout=30)
resp.raise_for_status()
items=resp.json()

# Collect files only (skip subfolders), prefer PDFs/links/MD
def rank(name):
    name_lower=name.lower()
    # Prefer pdf > md > everything else
    if name_lower.endswith(".pdf"): return (0, name_lower)
    if name_lower.endswith(".md"):  return (1, name_lower)
    return (2, name_lower)

files=[(it["name"], it.get("download_url") or it.get("html_url"))
       for it in items if it.get("type")=="file"]

files=sorted(files, key=lambda x: rank(x[0]))

# Keep first 7 items; pad if fewer than 7
MAX=7
if len(files) < MAX:
    files=files + [("TBD", "")]
files=files[:MAX]

# Build new table rows
rows=[]
for i,(name,url) in enumerate(files, start=1):
    label = f"[{name}]({url})" if url else name
    rows.append(f"| **Day {i}** | {label} | Deep read + notes | `notes/day{i}.md` |")

# Load README.md from cwd, replace the table block
with open("README.md","r",encoding="utf-8") as f:
    readme=f.read()

pattern=r"(\\| Day \\| Paper \\| Task \\| Deliverable \\|[\\s\\S]*?\\n)\\n---"
# Build replacement table header + rows
table_header = textwrap.dedent("""\
| Day | Paper | Task | Deliverable |
|-----|-------|------|-------------|
""")
new_table = table_header + "\n".join(rows)
readme = re.sub(r"\\| Day \\| Paper \\| Task \\| Deliverable \\|[\\s\\S]*?\\n\\n---",
                new_table + "\n\n---",
                readme,
                count=1)

with open("README.md","w",encoding="utf-8") as f:
    f.write(readme)

print("Updated README.md with papers from GitHub.")
PY
