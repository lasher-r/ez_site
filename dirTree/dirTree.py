import os

def path_to_html(path):
    """Wraps the directory html in a ul that allows collapsing"""
    return '''
        <div id="sb" class="w3-container w3-cell w3-rightbar" style="width: 20%;">
            <ul id="myUL">'''+path_to_html_inner(path).replace(path.replace('/','_'), '')+'''</ul>
        </div>
'''

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
        if tree["name"] == '__HEADER__.md' or tree["name"] == "__css__.css":
            html = ""
        else:
            html = "<li onclick=\"hideContent(\'%s\')\">%s</li>\n" % (tree["path"].replace('/','_'), tree["name"].replace('.md', ''))
    return html

def path_to_dict(path):
    """gets a directory tree and returns it as nested dict"""
    name = os.path.basename(path)
    if name[0] == '.':
        return
    d = {'name': name, 'path': path}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir(path)]
    else:
        d['type'] = "file"
    return d


