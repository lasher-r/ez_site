import os

css = '''
html {
height: 100%;
}
body {
height: 100%;
}

header {
text-align: justify;
letter-spacing: 1px;
height: 8em;
padding: 2em 10%;
background: #ccc;
text-align: center;
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

#sb_content {
height: 100%
}
'''

def save_css(dest):
    with open(os.path.join(dest,"page.css"), "w") as f:
        f.write(css)

def save_custom_css(dest, path):
    css_file = os.path.join(path, '__css__.css')
    if not os.path.isfile(css_file):
        return
    with open(css_file) as f:
        customCss = f.read()
        with open(os.path.join(dest,"custom.css"), "w") as f:
            f.write(customCss)