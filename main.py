from dirTree import dirTree
from content import MdInterperter
import myhtml

def flatten_files(root, files=[]):
    for path in root['children']:
        if not path:
            continue
        if path['type'] == 'file':
            files.append(path['path'])
        else:
            flatten_files(path, files)
    return files

def run(path):
    # get files
    files_dict = dirTree.path_to_dict(path)
    ff = flatten_files(files_dict)
    # make content html
    contentPages = []
    for f in ff:
        page = MdInterperter.translate_file(f, path)
        if page:
            contentPages.append(page)
    
    sideBarHtml = dirTree.path_to_html("/Users/richard/Documents/lasher_dev")

def as_page(path):
    # get files
    files_dict = dirTree.path_to_dict(path)
    ff = flatten_files(files_dict)
    # make content html
    contentPages = []
    for f in ff:
        page = MdInterperter.translate_file(f, path)
        if page:
            contentPages.append(page)
    
    # make sidebar
    sideBarHtml = dirTree.path_to_html("/Users/richard/Documents/lasher_dev")

    # build html
    html = "<!DOCTYPE html>"
    html += "\n<html>"

    html += myhtml.head()

    html += "\n<body>"

    html += "\n<div id=\"sb_content\" class=\"w3-cell-row\">"
    html += sideBarHtml

    html += "\n<div id=\"content\" class=\"w3-container w3-cell\">"

    for content in contentPages:
        html += "\n%s" % content

    html += "\n</div>"

    html += myhtml.fake_script()

    html += "\n</body>"

    html +="</html>"

    return html




if __name__ == "__main__":
    html = as_page('/Users/richard/Documents/lasher_dev')
    with open("page.html", "w") as f:
        f.write(html)
