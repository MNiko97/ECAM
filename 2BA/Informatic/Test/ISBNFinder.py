import os, openpyxl, json
from isbnlib import isbn_from_words, meta, config
from isbntools.app import config, ISBNToolsException
ROOT = os.path.abspath(os.getcwd()) + "/2BA/Informatic/res/"
FILE = "Michel's Library.xlsx"
SHEET = 'Books'

config.add_apikey('goob','AIzaSyBGHXp1MEELSeTW7YfuzE_lyilgEWg6tkc>')
book = openpyxl.load_workbook(ROOT+FILE)
sheet = book.get_sheet_by_name(SHEET)
max_row = sheet.max_row 
data = []
for i in range(2, max_row+1):
    title = sheet.cell(row = i, column = 1).value
    authors = sheet.cell(row = i, column = 2).value
    data.append([title.replace(" ", "+"), authors.replace(" ", "+")])

isbn_list=[]
a = len(data)
errors = [41, 225, 226, 227, 228, 296, 353, 354]

for i in range(a):
    query = data[i][0] + "+" + data[i][1]
    if i not in errors :
        try:
            isbn = isbn_from_words(query)
            res = [i+2, isbn, data[i][0].replace("+", " "), data[i][1].replace("+", " ")]
        except UnboundLocalError:
            res = [i+2, 'ISBN NOT FOUND', data[i][0].replace("+", " "), data[i][1].replace("+", " ")]
            isbn_list.append(res)
            pass
        isbn_list.append(res)
    print(str(i+1)+'/'+str(a))

json_data = []
b = len(isbn_list)
for i in range(b):
    row = isbn_list[i][0]
    original_title = isbn_list[i][2]
    original_authors = isbn_list[i][3]
    original_book = 'row: '+ str(row) + "/"+ str(a+1) + " BOOK : " + original_title + " FROM " + original_authors
    if isbn_list[i][1] == 'ISBN NOT FOUND':
        metadata = 'ISBN NOT FOUND'
        book = {original_book: metadata}
        json_data.append(book)
        pass
    else:
        try:
            metadata = meta(isbn_list[i][1], service='goob')
        except KeyError:
            metadata = {'ISBN ERROR: search mannualy': isbn_list[i][1]}
            book = {original_book: metadata}
            json_data.append(book)
            pass
        book = {original_book: {'isbn': None, 'title': None, 'authors': None, 'publisher': None, 'year': None, 'language': None}}
        if metadata:
            for key, value in metadata.items():
                if key == 'ISBN-13':
                    isbn = value
                    book[original_book]['isbn'] = isbn
                if key == 'Title':
                    title = value
                    book[original_book]['title'] = title
                if key == 'Authors':
                    authors = value
                    book[original_book]['authors'] = authors
                if key == 'Publisher':
                    publisher = value
                    book[original_book]['publisher'] = publisher
                if key == 'Year':
                    year = value
                    book[original_book]['year'] = year
                if key == 'Language':
                    language = value
                    book[original_book]['language'] = language
        else:
            metadata = {'ISBN ERROR: search mannualy': isbn_list[i][1]}
            book = {original_book: metadata}
        json_data.append(book)
    print(str(i+1)+'/'+str(b))

with open(ROOT + 'data.json', 'r+', encoding='utf8') as outfile:
    json_file = json.load(outfile)
    for book in json_data:
        json_file.update(book)
        outfile.seek(0)
        json.dump(json_file, outfile, ensure_ascii=False, indent=2)