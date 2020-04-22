import markdown2
import os

def sanitize_name(name):
    return name.replace('/', '_')

def translate_file(path, root='/'):
    filename, file_extension = os.path.splitext(os.path.basename(path))
    localPath = path[path.find(root) + len(root):path.find(filename):]
    localPath = sanitize_name(localPath)
    if file_extension == ".md":
        html = markdown2.markdown_path(path)
        html = "<div id=\"settup_content\" class=\"w3-hide\">\n%s\n</div>" % html
        return html
    else:
        return None

if __name__ == "__main__":
    html = translate_file('/Users/richard/Documents/lasher_dev/cheatsheats/utils.md', root='lasher_dev')
    with open("content.html", "w") as f:
        f.write(html)