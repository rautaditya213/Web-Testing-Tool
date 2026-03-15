import sys
import os

if len(sys.argv) < 2:
    print("Usage: python main.py <website_url>")
    sys.exit()

url = sys.argv[1]

print("Running automated tests for:", url)

command = f"pytest --url={url} --html=reports/report.html --self-contained-html"

os.system(command)

print("Test report generated in reports/report.html")