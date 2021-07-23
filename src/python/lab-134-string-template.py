#
# filename    : lab-134-string-template.py
# Description :
# Docs        :
#               * https://docs.python.org/3/library/string.html
#               * https://docs.python.org/3/library/datetime.html
# Requirements:
#               *
#

from string import Template
from datetime import datetime

with open('file-14-template-html.html', 'r') as html:
    template = Template(html.read())
    dt_now = datetime.now().strftime('%d/%m/%Y')
    content = template.safe_substitute(name='Josemar F. A. Silva', data=dt_now)
    with open('file-15-template-html.html', 'w') as html_output:
        html_output.write(content)

