from dirTree import dirTree
from content import MdInterperter
import myhtml

import argparse
import os

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
    contentHtml = myhtml.wrap_content(contentPages)
    
    # make sidebar
    sideBarHtml = dirTree.path_to_html("/Users/richard/Documents/lasher_dev")

    # wrap sidebar and content together
    sidebarContentHtml = myhtml.wrap_sb_contnet(sideBarHtml, contentHtml)

    # build html
    html = "<!DOCTYPE html>"
    html += "\n<html>"
    html += myhtml.head()
    html += "\n<body>"
    html += sidebarContentHtml
    html += myhtml.script()
    html += "\n</body>"
    html +="\n</html>"

    return html

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--publish", help="create webpage")
    args = parser.parse_args()

    if os.path.isdir(args.publish):
        print('creating page %s' % args.publish)
        html = as_page(args.publish) #'/Users/richard/Documents/lasher_dev')
        with open("page.html", "w") as f:
            f.write(html)
