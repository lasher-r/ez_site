from dirTree import dirTree
from content import MdInterperter
from web import myhtml, css
from publish import publishGit

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
    
    sideBarHtml = dirTree.path_to_html(path)

def as_page(path):
    # get files
    files_dict = dirTree.path_to_dict(path)
    ff = flatten_files(files_dict)

    # make content html
    contentDivs = MdInterperter.translate_files(path, ff)
    contentHtml = myhtml.wrap_content(contentDivs)

    # header
    headerHtml = MdInterperter.translate_header(path)
    
    # make sidebar
    sideBarHtml = dirTree.path_to_html(path)

    # wrap sidebar and content together
    sidebarContentHtml = myhtml.wrap_sb_contnet(sideBarHtml, contentHtml)

    # build html
    html = "<!DOCTYPE html>"
    html += "\n<html>"
    html += myhtml.head()
    html += "\n<body>"
    html += headerHtml
    html += sidebarContentHtml
    html += myhtml.script()
    html += "\n</body>"
    html +="\n</html>"

    return html

if __name__ == "__main__":
    tempdir = '/tmp/pn'
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--build", help="build webpage files")
    parser.add_argument("-p", "--publish", help="create webpage")
    args = parser.parse_args()

    if args.build and os.path.isdir(args.build):
        print('creating page for %s' % args.build)
        html = as_page(os.path.abspath(args.build)) #'/Users/richard/Documents/lasher_dev')
        with open(os.path.join(tempdir,"index.html"), "w") as f:
            f.write(html)
        css.save_css(tempdir)
        css.save_custom_css(tempdir, os.path.abspath(args.build))
        print('\n\nto preview with docker run:')
        print('\tdocker run -it -p 8080:80 -v /tmp/pn/:/usr/local/apache2/htdocs/ httpd:2.4')
        print('and navigate to localhost:8080\n\n')
    elif args.publish:
        print('pushing website to %s' % args.publish)
        publisher = publishGit.GitPublish('/tmp/pn', args.publish)
        publisher.publish()
        print('\n\nIt may take a minute for github pages to reflect changes\n\n')
