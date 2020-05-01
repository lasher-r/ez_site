def head():
    return '''
<head>
    <meta charset="utf-8"/>
    <link rel="stylesheet" href="page.css">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css" />
<link rel="stylesheet" href="custom.css">
</head>
'''


def script():
    return '''
    <script>
      function hideContent(param) {
        let div = document.getElementById("content");

        for (var i=0; i<div.children.length; i++) {
          var child = div.children[i];
          child.className = child.className.replace(" w3-show", "");
        }

        let content = document.getElementById(param);
        content.className += " w3-show";

      }

      var toggler = document.getElementsByClassName("caret");
      var i;

      for (i = 0; i < toggler.length; i++) {
        toggler[i].addEventListener("click", function () {
          this.parentElement
            .querySelector(".nested")
            .classList.toggle("active");
          this.classList.toggle("caret-down");
        });
      }
    </script>
    '''


def fake_script():
    return '''
    <script>

      function hideContent(param) {
        alert(param)
      }

      var toggler = document.getElementsByClassName("caret");
      var i;

      for (i = 0; i < toggler.length; i++) {
        toggler[i].addEventListener("click", function () {
          this.parentElement
            .querySelector(".nested")
            .classList.toggle("active");
          this.classList.toggle("caret-down");
        });
      }
    </script>
    '''


def wrap_content(contentPages):
  contentHtml = "\n<div id=\"content\" class=\"w3-container w3-cell\">"
  for content in contentPages:
      contentHtml += "\n%s" % content
  contentHtml += "\n</div>"

  return contentHtml

def wrap_sb_contnet(sideBarHtml, contentHtml):
    html = "\n<div id=\"sb_content\" class=\"w3-cell-row\">"+sideBarHtml+contentHtml+"\n</div>"
    return html