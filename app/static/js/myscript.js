window.onload = function() {
  slider();
  fileCheck();
  showForm();
  blockAvoidance();
};

function slider(){
  var img = $(".slide-photo"),
      num = img.length,
      count = 0,
      interval = 5000;

  img.eq(0).addClass("show");

  setTimeout(slide, interval);

  function slide() {
    img.eq(count).removeClass("show");
    count++;
    if(count >= num) {
      count = 0;
    }
    img.eq(count).addClass("show");
    setTimeout(slide, interval);
  }
};

function fileCheck(){
  var fileObj = $("#file-data");
  fileObj.on("change", function() {
      var file = this.files[0];
      if(file != null) {
        $("#label-text").text("ファイル選択中");
        $("#item-label").css({"background-color": "#6A5ACD"});
      };
  });
};

function showForm(){
  var switch_key = $(".switch");
  for (var i = 0; i < switch_key.length; i++) {
    switch_key[i].onclick = function(){
      var key = this.getAttribute("data-show");
      if (key == "file") {
        this.classList.add("selected-form");
        document.getElementById("code-show").classList.remove("selected-form");
        document.getElementById("file-items").classList.add("show-items");
        document.getElementById("item-text-word").textContent = "対象ファイル";
        document.getElementById("file-default-check").checked = true;
        document.getElementById("code-items").classList.remove("show-items");
      }else{
        this.classList.add("selected-form");
        document.getElementById("file-show").classList.remove("selected-form");
        document.getElementById("code-items").classList.add("show-items");
        document.getElementById("item-text-word").textContent = "対象コード";
        document.getElementById("code-default-check").checked = true;
        document.getElementById("file-items").classList.remove("show-items");
      };
    };
  };
};

function blockAvoidance(){
  var btn = document.getElementById("submit-btn");
  btn.onclick = function(){
      var pre_code = document.getElementById("code-data");
      var new_code = pre_code.value.replace(/script/g, "hoge_script").replace(/iframe/g, "hoge_iframe")
      pre_code.value = new_code;
  };
};
