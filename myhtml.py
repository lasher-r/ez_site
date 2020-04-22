def head():
    return '''
<head>
    <style>
        html {
        height: 100%;
        }
        body {
        min-height: 100%;
        }

        /* Remove default bullets */
        ul,
        #myUL {
        list-style-type: none;
        }

        /* Remove margins and padding from the parent ul */
        #myUL {
        margin: 0;
        padding: 0;
        }

        /* Style the caret/arrow */
        .caret {
        cursor: pointer;
        user-select: none; /* Prevent text selection */
        }

        /* Create the caret/arrow with a unicode, and style it */
        .caret::before {
        content: "\\25B6";
        color: black;
        display: inline-block;
        margin-right: 6px;
        }

        /* Rotate the caret/arrow icon when clicked on (using JavaScript) */
        .caret-down::before {
        transform: rotate(90deg);
        }

        /* Hide the nested list */
        .nested {
        display: none;
        }

        /* Show the nested list when the user clicks on the caret/arrow (with JavaScript) */
        .active {
        display: block;
        }
    </style>
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css" />
</head>
'''


def script():
    return '''
    <script>
      function hideContent(param) {
          alert(param)
        var x = document.getElementById("settup_content");
        if (x.className.indexOf("w3-show") == -1) {
          x.className += " w3-show";
        } else {
          x.className = x.className.replace(" w3-show", "");
        }
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
