import os
from os.path import exists
import shutil

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #Path to HTMCODE Repository
# path to path /website 
pathWebsite = path + "/website"

def createRepository():
    # create /website repository if it does not exist
    if not exists(pathWebsite):
        os.makedirs(pathWebsite)
        # print("website repository created")
    else:
        #erase all files in /website repository and create website repository
        shutil.rmtree(pathWebsite)
        os.makedirs(pathWebsite)
        # print("website repository created")



def newPage(page):
    pathPage = pathWebsite + "/" + page
    if not exists(pathPage):
        os.makedirs(pathPage)
        #Create index.html file
        f = open(pathPage + "/index.html", "w")
        f.write('<!DOCTYPE html>\n<html>\n<head>\n\t<link rel="stylesheet" href="styles.css">\n\t<title>' + page + '\t</title>\n</head>\n<body>\n\t')
        f.close()
        #Create style.css file
        f = open(pathPage + "/styles.css", "w")
        f.write('body {\nbackground-color: #f0f0f5;\n}\n')
        f.close()
        #Create index.js file
        f = open(pathPage + "/index.js", "w")
        f.write('console.log("Hello World!");\n')
        f.write('console.log("Aqui podras añadir el codigo necesario para tu pagina");\n')
        f.close()
        # print("page created")
    else:
        #erase all files in /page repository and create page repository
        shutil.rmtree(pathPage)
        os.makedirs(pathPage)
        f = open(pathPage + "/index.html", "w")
        f.write('<!DOCTYPE html>\n<html>\n<head>\n\t<title>' + page + '\t</title>\n</head>\n<body>\n\t')
        # f.write('<!DOCTYPE html>\n<html>\n<head>\n<title>' + page + '</title>\n</head>\n<body>\n</body>\n</html>')
        f.close()
        #Create style.css file
        f = open(pathPage + "/style.css", "w")
        f.write('body {\nbackground-color: #f0f0f5;\n}\n')
        f.close()
        #Create index.js file
        f = open(pathPage + "/index.js", "w")
        f.write('console.log("Hello World!");\n')
        f.close()
        # print("page created")

def endBody(page):
    # append </body> to index.html
    pathPage = pathWebsite + "/" + page
    f = open(pathPage + "/index.html", "a")
    #Add script tag
    f.write('\t<script src="index.js"></script>\n')
    f.write('</body>\n')
    f.close()

def startDiv(page):
    # append <div> to index.html
    pathPage = pathWebsite + "/" + page
    f = open(pathPage + "/index.html", "a")
    f.write('\t<div>\n\t')
    f.close()

def endDiv(page):
    # append </div> to index.html
    pathPage = pathWebsite + "/" + page
    f = open(pathPage + "/index.html", "a")
    f.write('\t</div>\n')
    f.close()

def startForm(page):
    # append <form> to index.html
    pathPage = pathWebsite + "/" + page
    f = open(pathPage + "/index.html", "a")
    f.write('\t<form>\n\t')
    f.close()

def endForm(page):
    # append </form> to index.html
    pathPage = pathWebsite + "/" + page
    f = open(pathPage + "/index.html", "a")
    f.write('\t</form>\n')
    f.close()

def endPage(page):
    # append </html> to index.html
    pathPage = pathWebsite + "/" + page
    f = open(pathPage + "/index.html", "a")
    f.write('</html>')
    f.close()
    
def newUl(page):
    # append <ul> to index.html
    pathPage = pathWebsite + "/" + page
    f = open(pathPage + "/index.html", "a")
    f.write('\t<ul>\n\t')
    f.close()

def endUl(page):
    # append </ul> to index.html
    pathPage = pathWebsite + "/" + page
    f = open(pathPage + "/index.html", "a")
    f.write('\t</ul>\n')
    f.close()

def newOl(page):
    # append <ol> to index.html
    pathPage = pathWebsite + "/" + page
    f = open(pathPage + "/index.html", "a")
    f.write('\t<ol>\n\t')
    f.close()

def endOl(page):
    # append </ol> to index.html
    pathPage = pathWebsite + "/" + page
    f = open(pathPage + "/index.html", "a")
    f.write('</ol>\n')
    f.close()

def newLi(page):
    # append <li> to index.html
    pathPage = pathWebsite + "/" + page
    f = open(pathPage + "/index.html", "a")
    f.write('\t\t<li>\n\t\t')
    f.close()

def endLi(page):
    # append </li> to index.html
    pathPage = pathWebsite + "/" + page
    f = open(pathPage + "/index.html", "a")
    f.write('\t</li>\n\t')
    f.close()

def newBr(page):
    # append <br> to index.html
    pathPage = pathWebsite + "/" + page
    f = open(pathPage + "/index.html", "a")
    f.write('\t\t<br>\n')
    f.close()

def startTable(page):
    # append <table> to index.html
    pathPage = pathWebsite + "/" + page
    f = open(pathPage + "/index.html", "a")
    f.write('\t<table>\n\t')
    f.close()

def endTable(page):
    # append </table> to index.html
    pathPage = pathWebsite + "/" + page
    f = open(pathPage + "/index.html", "a")
    f.write('\t</table>\n')
    f.close()

def startTr(page):
    # append <tr> to index.html
    pathPage = pathWebsite + "/" + page
    f = open(pathPage + "/index.html", "a")
    f.write('\t\t<tr>\n\t\t')
    f.close()

def endTr(page):
    # append </tr> to index.html
    pathPage = pathWebsite + "/" + page
    f = open(pathPage + "/index.html", "a")
    f.write('\t\t</tr>\n\t')
    f.close()

def startNav(page):
    # append <nav> to index.html
    pathPage = pathWebsite + "/" + page
    f = open(pathPage + "/index.html", "a")
    f.write('\t<nav>\n\t')
    f.close()

def endNav(page):
    # append </nav> to index.html
    pathPage = pathWebsite + "/" + page
    f = open(pathPage + "/index.html", "a")
    f.write('\t</nav>\n')
    f.close()

def newP(page,text):
    # append <p> to index.html
    pathPage = pathWebsite + "/" + page
    f = open(pathPage + "/index.html", "a")
    f.write('\t\t<p>' + text + '</p>\n')
    f.close()

def newLabel(page,text):
    # append <label> to index.html
    pathPage = pathWebsite + "/" + page
    f = open(pathPage + "/index.html", "a")
    f.write('\t\t<label>' + text + '</label>\n')
    f.close()

def newB(page,text):
    # append <b> to index.html
    pathPage = pathWebsite + "/" + page
    f = open(pathPage + "/index.html", "a")
    f.write('\t\t<b>' + text + '</b>\n')
    f.close()

def newI(page,text):
    # append <i> to index.html
    pathPage = pathWebsite + "/" + page
    f = open(pathPage + "/index.html", "a")
    f.write('\t\t<i>' + text + '</i>\n')
    f.close()

def newU(page,text):
    # append <u> to index.html
    pathPage = pathWebsite + "/" + page
    f = open(pathPage + "/index.html", "a")
    f.write('\t\t<u>' + text + '</u>\n')
    f.close()

def newA(page,src,text):
    # append <a> to index.html
    pathPage = pathWebsite + "/" + page
    # f = open(pathPage + "/index.html", "a")
    # f.write('\t\t<a href="#">' + text + '</a>\n')
    # f.close()
    # if src contains http
    if src[0:4] == "http":
        f = open(pathPage + "/index.html", "a")
        f.write('\t\t<a href="' + src + '"' + 'target="_blank" ' '>' + text + '</a>\n')
        f.close()
    else:
        f = open(pathPage + "/index.html", "a")
        capital= src[0].upper() + src[1:]
        # ../About/about.html
        f.write('\t\t<a href="../' + capital + '/' + 'index.html">' + text + '</a>\n')
        f.close()

def newImg(page,src):
    # append <img> to index.html
    pathPage = pathWebsite + "/" + page
    f = open(pathPage + "/index.html", "a")
    f.write('\t\t<img src="' + src + '"' + ' style="width:100px" >\n')
    f.close()

def newButton(page,text):
    # append <button> to index.html
    pathPage = pathWebsite + "/" + page
    f = open(pathPage + "/index.html", "a")
    f.write('\t\t<button>' + text + '</button>\n')
    f.close()

def newTh(page,text):
    # append <th> to index.html
    pathPage = pathWebsite + "/" + page
    f = open(pathPage + "/index.html", "a")
    f.write('\t\t\t<th>' + text + '</th>\n')
    f.close()

def newTd(page,text):
    # append <td> to index.html
    pathPage = pathWebsite + "/" + page
    f = open(pathPage + "/index.html", "a")
    f.write('\t\t\t<td>' + text + '</td>\n')
    f.close()

def newHeader(page,size,text):
    # append <h1> to index.html
    pathPage = pathWebsite + "/" + page
    f = open(pathPage + "/index.html", "a")
    f.write('\t\t<h' + str(size) + '>' + text + '</h' + str(size) + '>\n')
    f.close()

def newInput(page,type, id):
    # append <input> to index.html
    pathPage = pathWebsite + "/" + page
    f = open(pathPage + "/index.html", "a")
    f.write('\t\t<input type="' + type + '" id="' + id + '">\n')
    f.close()