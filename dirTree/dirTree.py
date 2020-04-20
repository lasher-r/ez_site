import os

def path_to_html(path):
    """Wraps the directory html in a ul that allows collapsing"""
    return "<ul id=\"myUL\">\n"+path_to_html_inner(path)+"</ul>\n"

def path_to_html_inner(path):
    """gets a directory tree and returns it as html ul
    With css/js tags to allow formating and collapsing"""
    tree = path_to_dict(path)
    html = ''
    # for t in tree:
    if tree["type"] == "directory":
        html += "<li><span class=\"caret\">%s</span>\n" % tree["name"]

        html += "<ul class=\"nested\">\n"
        # get children
        for child in tree["children"]:
            if not child:
                continue
            html += path_to_html_inner(os.path.join(path, child["name"]))
        html += "</ul>\n"  # line 12

        html += "</li>\n"  # line 10
    else:
        html = "<li>%s</li>\n" % tree["name"]
    return html

def path_to_dict(path):
    """gets a directory tree and returns it as nested dict"""
    name = os.path.basename(path)
    if name[0] == '.':
        return
    d = {'name': name}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir(path)]
    else:
        d['type'] = "file"
    return d

if __name__ == "__main__":
    html = '''<!DOCTYPE html>
    <html>
    <head>
    <style>
    '''
    with open('dirTree/dirTree.css', 'r') as css:
        html += css.read()
    
    html += '''
    </style>
    </head>
    <body>
    '''

    html += path_to_html("/Users/richard/Documents/lasher_dev")

    html += '''
    </body>

    <script>
    '''

    with open('dirTree/dirTree.js', 'r') as js:
        html += js.read()

    html += '''
    </script>
    '''

    with open("dir.html", "w") as f:
        f.write(html)

