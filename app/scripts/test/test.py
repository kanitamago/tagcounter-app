import re
from bs4 import BeautifulSoup
from pprint import pprint

#タグ名リスト
tags = ['html', 'head', 'title', 'base', 'link', 'style', 'meta', 'body', 'article', 'section', 'nav', 'aside', 'h1', 'h6', 'hgroup', 'header', 'footer', 'address', 'p', 'hr', 'pre', 'blockquote', 'ol', 'ul', 'li', 'dl', 'dt', 'dd', 'figure', 'figcaption', 'main', 'div', 'a', 'em', 'strong', 'small', 's', 'cite', 'q', 'dfn', 'abbr', 'code', 'var', 'samp', 'kbd', 'data', 'sub', 'sup', 'time', 'i', 'b', 'u', 'mark', 'ruby', 'rb', 'rt', 'rtc', 'rp', 'bdi', 'bdo', 'span', 'br', 'wbr', 'ins', 'del', 'img', 'picture', 'iframe', 'embed', 'object', 'param', 'video', 'audio', 'track', 'source', 'map', 'area', 'table', 'caption', 'colgroup', 'col', 'tbody', 'thead', 'tfoot', 'tr', 'td', 'th', 'form', 'fieldset', 'legend', 'label', 'input', 'select', 'option', 'optgroup', 'textarea', 'button', 'datalist', 'keygen', 'output', 'progress', 'meter', 'script', 'noscript', 'template', 'canvas', 'details', 'summary', 'menu', 'menuitem', 'command']


string = "<html class='test-html' id='test-id'></html>"

test_html = """
    <!DOCTYPE html>
    <html lang="ja">
      <head id="header" class="header-class main-head">
        <meta id="metameta" charset="utf-8">
        <title>{% block title %}{% endblock %}|Tag Counter</title>
        <link rel="stylesheet" href="../static/css/style.css">
      </head>
      <body id="main-body">
        <div class="input-file">
          <form id="file-form main-form" action="{{ url_for('show_result') }}" method="post" enctype="multipart/form-data">
            <input id="input-file" type="file" name="data">
            <button class="btn" id="submit-btn" type="submit" name="button">カウント</button>
          </form>
        </div>
        {% block result %}
        {% endblock %}
      </body>
    </html>
    """
"""
print("HTML: \n", test_html)

print("="*100)

results = {}

soup = BeautifulSoup(test_html, "html.parser")

for tag in tags:
    tag_objs = soup.select(tag)
    temp_result = {}
    if tag_objs:
        for i in range(len(tag_objs)):
            try:
                temp_result["class_name"] = tag_objs[i]["class"]
            except:
                temp_result["class_name"] = None
            try:
                temp_result["id_name"] = tag_objs[i]["id"]
            except:
                temp_result["id_name"] = None
        results[tag] = temp_result

pprint(results.keys())
"""
"""
pattern_class = "class=\'(.*)\'"
pattern_id = "id=\'(.*)\'"

result1 = re.search(pattern_class, string)
result2 = re.search(pattern_id, string)

print(result1)
print(result2)
"""

test = 0
test_bool = bool(test)
print(test_bool)
