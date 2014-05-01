#!/usr/bin/env python

import os.path, json
from argparse import ArgumentParser
from PyPDF2 import PdfFileMerger


if __name__ == '__main__':
    
    ap = ArgumentParser()
    ap.add_argument('pdf', help='the input PDF')
    ap.add_argument('bookmarks', help='JSON list of bookmarks')
    ap.add_argument('offset', help='page offset to use')
    
    pdf_path = ap.parse_args().pdf
    bookmarks_path = ap.parse_args().bookmarks
    page_offset = ap.parse_args().offset
    
    pdf = open(pdf_path, 'rb')
    
    output_pdf = PdfFileMerger()
    output_pdf.merge(position=0, fileobj=pdf)

    bookmarks = json.load(open(bookmarks_path))
    
    for name, page in bookmarks:
        output_pdf.addBookmark(name, page + int(page_offset) - 2)
    
    output_pdf_path = os.path.splitext(pdf_path)[0] + '-bookmarked.pdf'
    output_pdf.write(open(output_pdf_path, 'wb'))

    