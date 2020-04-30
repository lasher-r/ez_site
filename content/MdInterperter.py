import markdown2
import os

def sanitize_name(name):
    return name.replace('/', '_')

def translate_header(path):
    filePath = os.path.join(path, "__HEADER__.md")
    html = markdown2.markdown_path(filePath)
    html = "<header>%s</header>" % html
    return html


def translate_file(path, root='/'):
    filename, file_extension = os.path.splitext(os.path.basename(path))
    localPath = path[path.find(root) + len(root):path.find(filename):]
    localPath = sanitize_name(localPath)
    if filename == '__HEADER__':
        return None
    if file_extension == ".md":
        html = markdown2.markdown_path(path, extras=["fenced-code-blocks"])
        html = "<div id=\"%s\" class=\"w3-hide\">\n%s\n</div>" % (localPath+filename+'.md', html)
        return html
    else:
        return None
