from bs4 import BeautifulSoup
from collections import Counter
from wordcloud import WordCloud
import os
import shutil
from datetime import datetime
import re
import csv

class TagCounter():

    #タグ名リスト
    tags = ['html', 'head', 'title', 'base', 'link', 'style', 'meta', 'body', 'article', 'section', 'nav', 'aside', 'h1', 'h6', 'hgroup', 'header', 'footer', 'address', 'p', 'hr', 'pre', 'blockquote', 'ol', 'ul', 'li', 'dl', 'dt', 'dd', 'figure', 'figcaption', 'main', 'div', 'a', 'em', 'strong', 'small', 's', 'cite', 'q', 'dfn', 'abbr', 'code', 'var', 'samp', 'kbd', 'data', 'sub', 'sup', 'time', 'i', 'b', 'u', 'mark', 'ruby', 'rb', 'rt', 'rtc', 'rp', 'bdi', 'bdo', 'span', 'br', 'wbr', 'ins', 'del', 'img', 'picture', 'iframe', 'embed', 'object', 'param', 'video', 'audio', 'track', 'source', 'map', 'area', 'table', 'caption', 'colgroup', 'col', 'tbody', 'thead', 'tfoot', 'tr', 'td', 'th', 'form', 'fieldset', 'legend', 'label', 'input', 'select', 'option', 'optgroup', 'textarea', 'button', 'datalist', 'keygen', 'output', 'progress', 'meter', 'script', 'noscript', 'template', 'canvas', 'details', 'summary', 'menu', 'menuitem', 'command']

    #初期値は「htmlコード」と「csvファイル化するか否か」
    def __init__(self, data=None, create_file=False):
        self.data = data
        self.create_file = create_file
        self.results = []

    #タグをカウントし、可視化する
    def counter(self):

        block_word = "hoge_"
        self.data = self.data.replace(block_word, "")

        tag_objs = {}
        wordcloud_list = []
        text_list = []

        soup = BeautifulSoup(self.data, "html.parser")

        for tag in TagCounter.tags:
            tag_objs[tag] = soup.select(tag)
            result = {"TagName":tag, "TagCount":len(tag_objs[tag])}
            if len(tag_objs[tag]) > 0:
                for _ in range(len(tag_objs[tag])):
                    text_list.append(tag)
                    wordcloud_list.append(tag+"_tag")
            self.results.append(result)

        output_text = Counter(text_list).most_common()

        word_cloud_text = " ".join(wordcloud_list)

        wordcloud = WordCloud(background_color="white", width=600, height=400).generate(word_cloud_text)

        now = str(datetime.now()).split(".")[0].replace(":", "-").replace(" ", "")
        savepath = "app/static/input/"+now+".png"

        if not "input" in os.listdir("app/static"):
            os.mkdir("app/static/input")
        else:
            shutil.rmtree("app/static/input/")
            os.mkdir("app/static/input")

        wordcloud.to_file(savepath)

        image_path = "../static/input/"+now+".png"

        if self.create_file:
            csv_path = self.create_csv(tag_objs)
            return (output_text, image_path, csv_path)
        else:
            return (output_text, image_path, None)

    #クラスとID名を取得し、CSV化する
    def create_csv(self, tag_objs):
        #resultsにクラス名とid名を追加する
        #現在のresultsの中身
        """
        [{'TagCount': 0, 'TagName': 'html'}, {'TagCount': 0, 'TagName': 'head'}...]
        """
        #期待するresultsの中身
        #複数ある場合はスラッシュで区切る
        #存在しない場合はNoneを放り込む
        """
        [{'TagCount': 0, 'TagName': 'html', 'ClassName': 'main-html/sub-html', 'IdName': None},
         {'TagCount': 0, 'TagName': 'head', 'ClassName': None, 'IdName': 'header'}...]
        """
        for tag in self.results:
            if tag["TagCount"] != 0:
                temp_class = []
                temp_id = []
                for obj in tag_objs[tag["TagName"]]:
                    try:
                        temp_class.append("/".join(obj["class"]))
                    except:
                        pass
                    try:
                        temp_id.append("/".join(obj["id"].split(" ")))
                    except:
                        pass
                if temp_class:
                    tag["ClassName"] = "/".join(temp_class)
                else:
                    tag["ClassName"] = None
                if temp_id:
                    tag["IdName"] = "/".join(temp_id)
                else:
                    tag["IdName"] = None
            else:
                tag["ClassName"] = None
                tag["IdName"] = None

        with open("app/static/input/tag_html.csv","wt") as csvfile:
            fieldnames = ["TagName", "TagCount", "ClassName", "IdName"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for value in self.results:
                writer.writerow(value)

        path = "../static/input/tag_html.csv"

        return path

if __name__ == "__main__":
    html = """
<!DOCTYPE html>
<html lang="ja">
  <head id="dummy">
    <meta charset="utf-8">
    <title>{% block title %}{% endblock %} | Log</title>
    <link rel="stylesheet" href ="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <script src=" https://code.jquery.com/jquery-3.2.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
  </head>
  <body class="bg-light">
    <div class="container">
      <header>
      <nav class="navbar navbar-expand-lg navbar-light rounded">
        <a class="text-white navbar-brand" href="{{ url_for('index') }}">Log</a>
          <ul class="nav navbar-nav navbar-right">
            {% if not session.logged_in %}
            <li class="nav-item dropdown">
              <a href="#" class="nav-link dropdown-toggle text-white" role="button" data-toggle="dropdown" id="navbarDropdownMenuLink" aria-haspopup="true" aria-expanded="false">制作物</a>
              <div id="dummy-id" class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                <a class="dropdown-item" href="{{ url_for('display_gettweet') }}">ツイートを過去から遡る</a>
                <a class="dropdown-item" href="{{ url_for('display_getimage') }}">ツイッター画像を過去から遡る</a>
              </div>
            </li>
            <li class="nav-item">
              <a class="text-white nav-link" href="{{ url_for('login') }}">ログイン</a>
            </li>
            {% else %}
            <li class="nav-item dropdown">
              <a href="#" class="nav-link dropdown-toggle text-white" role="button" data-toggle="dropdown" id="navbarDropdownMenuLink" aria-haspopup="true" aria-expanded="false">制作物</a>
              <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                <a class="dropdown-item" href="{{ url_for('display_gettweet') }}">ツイートを過去から遡る</a>
                <a class="dropdown-item fake-class" href="{{ url_for('display_getimage') }}">ツイート画像を過去から遡る</a>
              </div>
            </li>
            <li>
              <a id="dummy_id testing-id" class="text-white nav-link" href="{{ url_for('post_menu') }}">新規投稿</a>
            </li>
            <li>
              <a class="text-white nav-link" href="{{ url_for('logout') }}">ログアウト</a>
            </li>
            {% endif %}
          </ul>
      </nav>
      </header>

      {% for message in get_flashed_messages() %}
      <div class="alert alert-info" role="alert">
        {{ message }}
      </div>
      {% endfor %}

      {% block login %}
      {% endblock %}

      {% block body %}
      {% endblock %}
      <!--end of container-->
    </div>
  </body>
</html>
    """
    test = TagCounter(html, create_file=True)
    output_text, image_path, csv_path = test.counter()
    print("OUTPUT_TEXT: ", output_text)
    print("IMAGE_PATH: ", image_path)
    print("CSV_PATH: ", csv_path)
