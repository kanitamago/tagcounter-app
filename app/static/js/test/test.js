window.onload = function(){
  showForm();
  blockAvoidance();
};

function showForm(){
  var show_key = $(".show");
  for (var i = 0; i < show_key.length; i++) {
    show_key[i].onclick = function(){
      var key = this.getAttribute("data-show");
      if (key == "file") {
        this.classList.add("selected-form");
        document.getElementById("code-show").classList.remove("selected-form");
        document.getElementById("file-items").classList.add("show-items");
        document.getElementById("code-items").classList.remove("show-items");
      }else{
        this.classList.add("selected-form");
        document.getElementById("file-show").classList.remove("selected-form");
        document.getElementById("code-items").classList.add("show-items");
        document.getElementById("file-items").classList.remove("show-items");
      };
    };
  };
};

function blockAvoidance(){
  var btn = document.getElementById("check-btn");
  btn.onclick = function(){
      var pre_code = document.getElementById("code-data");
      var new_code = pre_code.value.replace(/script/g, "hoge_script");
      pre_code.value = new_code;
  };
};
