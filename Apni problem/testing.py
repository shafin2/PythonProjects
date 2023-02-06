# from csv import writer
# lstOfRunner=['3\nI Spy A Diva\nDavid Bass\n1.04\n$232\n1.05\n$58\n1.06\n$40\n1.07\n$188\n1.08\n$355\n1.09\n$32', '5\nUrban Soldier\nH Cobden\n13\n$16\n14\n$39\n48\n$42\n50\n$12', '7\nOoh Betty\nBen Jones\n44\n$13\n48\n$32\n990\n$11',]
# with open('testingFile.csv', 'w', encoding='utf8', newline='') as f:
#     thewriter = writer(f)
#     header = ['Title', 'Location', 'Price', 'Area']
#     thewriter.writerow(header)
#     for runner in lstOfRunner:
#         data = runner.split("\n")
#         thewriter.writerow(data)
# import datetime
#
# print(datetime.datetime.strptime('November 10, 2003', '%B %d, %Y').strftime('%d/%m/%Y'))

import re
str='''
    
Author: F. J. Cross

Release Date: November 9, 2003 [EBook #10024]

Language: English

Character set encoding: ASCII

*** START OF THIS PROJECT GUTENBERG EBOOK BENEATH THE BANNER ***




Produced by Imran Ghory, Stan Goodman, Josephine Paolucci
and PG Distributed Proofreaders


'''
data=str.split("*** START")
print(data[0])