import fitz  
import csv

filename = 'Card_Scan.pdf'
doc = fitz.open(filename)  # open PDF with PyMuPDF

page = doc[0]
page.set_rotation(90)

#offsets
card1offset = 4
card2offset = 148
card3offset = 292
card4offset = 435

#TODO : Figure out max length of First + Last Name, add check to not print on top of other info
#TODO : Add check for length of address line 1, ensure does not print over member number



def printRow(page, offset, name, addr1, addr2, addr3, LM, SC, ML, member):

    # **** First Card ****
    # Name
    point = fitz.Point(58 + offset, 757)  # insertion start point
    page.insert_text(point, name, rotate=90)  # insert the text
    # Address Line 1
    point = fitz.Point(70 + offset, 757) 
    page.insert_text(point, addr1, rotate=90)

    #Check if address has line 2
    if (addr2 != ""):
        #address Line 2
        point = fitz.Point(82 + offset, 757) 
        page.insert_text(point, addr2, rotate=90)
        #City, State, Town
        point = fitz.Point(94 + offset, 757) 
        page.insert_text(point, addr3, rotate=90)
    else:
        #City, State, Town
        point = fitz.Point(82 + offset, 757) 
        page.insert_text(point, addr3, rotate=90)

    #Check if Senior Citizen
    if (SC):
        point = fitz.Point(58 + offset, 595) 
        page.insert_text(point, "SC", rotate=90)

    #Check if Life Member
    if (LM):
        point = fitz.Point(58 + offset, 615) 
        page.insert_text(point, "LM", rotate=90)

    #Check if Military
    if (ML):
        point = fitz.Point(58 + offset, 575) 
        page.insert_text(point, "ML", rotate=90)

    #Member Number
    point = fitz.Point(82 + offset, 620) 
    page.insert_text(point, member, rotate=90, fontsize = 20)

    # **** Second Card ****
    # Name
    point = fitz.Point(92 + offset, 508) 
    page.insert_text(point, name, rotate=90)  # insert the text

    #Check if Senior Citizen
    if (SC):
        point = fitz.Point(92 + offset, 390) 
        page.insert_text(point, "SC", rotate=90)

    #Check if Life Member
    if (LM):
        point = fitz.Point(92 + offset, 370) 
        page.insert_text(point, "LM", rotate=90)

    #Check if Military
    if (ML):
        point = fitz.Point(92 + offset, 350) 
        page.insert_text(point, "ML", rotate=90)

    #Member Number
    point = fitz.Point(92 + offset, 330) 
    page.insert_text(point, member, rotate=90)


    # **** Third Card ****
    # Name
    point = fitz.Point(90 + offset, 267) 
    page.insert_text(point, name, rotate=90)  # insert the text

    #Check if Senior Citizen
    if (SC):
        point = fitz.Point(65 + offset, 120) 
        page.insert_text(point, "SC", rotate=90)

    #Check if Life Member
    if (LM):
        point = fitz.Point(65 + offset, 100) 
        page.insert_text(point, "LM", rotate=90)

    #Check if Military
    if (ML):
        point = fitz.Point(65 + offset, 80) 
        page.insert_text(point, "ML", rotate=90)

    #Member Number
    point = fitz.Point(65 + offset, 170) 
    page.insert_text(point, member, rotate=90, fontsize = 20)

with open('jr-members.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    i = 0
    print(page.rect.width, page.rect.height)
    for r,g,b,a in zip(*[iter(spamreader)]*4):
        # print(r,g,b,a)
        # print("Group of 4")
        printRow(page, card1offset, f'{r[1]} {r[3]}', r[4], r[5], f'{r[6]}, {r[7]} {r[8]}', False, False, False, "")
        printRow(page, card2offset, f'{g[1]} {g[3]}', g[4], g[5], f'{g[6]}, {g[7]} {g[8]}', False, False, False, "")
        printRow(page, card3offset, f'{b[1]} {b[3]}', b[4], b[5], f'{b[6]}, {b[7]} {b[8]}', False, False, False, "")
        printRow(page, card4offset, f'{a[1]} {a[3]}', a[4], a[5], f'{a[6]}, {a[7]} {a[8]}', False, False, False, "")
        i = i+1
        page = doc._newPage(height=775,width=595)
        
        page.set_rotation(90)



doc.save("output.pdf")