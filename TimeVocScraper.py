# import section
from bs4 import BeautifulSoup # can be obtained from <http://www.crummy.com/software/BeautifulSoup/>
import csv
import urllib2

# TimeVocScraper written by Gerrit Holz, 22.08.2012

# connect to the website and read table's rows
raw = urllib2.urlopen('http://www.digicult-museen.net/xtree_2_vocnet/makeTableTimeVokDDB.php')
raw = raw.read()
soup = BeautifulSoup(raw)
rows = soup.findAll("td")

# fetch and trim the headings of the table
head0 = str([rows[0]])
head1 = str([rows[1]])
head2 = str([rows[2]])
head3 = str([rows[3]])
head4 = str([rows[4]])
head5 = str([rows[5]])
head6 = str([rows[6]])

head0 = head0[8:-10]
head1 = head1[8:-10]
head2 = head2[8:-10]
head3 = head3[8:-10]
head4 = head4[8:-10]
head5 = head5[8:-10]
head6 = head6[8:-10]

# define lists with starting elements which will be in the first line of csv
ID = [head0]
notation = [head1]
earliestDate = [head2]
latestDate = [head3]
prefLabelatde = [head4]
prefLabelaten = [head5]
sortOrder = [head6]

# setup indices for rows
a = 7
b = 8
c = 9
d = 10
e = 11
f = 12
g = 13

# fetch data for first column and store it in list "ID"
try:
  for row in rows:
    untrimmed = rows[a]
    untrimmed = str(untrimmed)
    trimmed = untrimmed[4:-5]
    ID.append(trimmed)
    a = a + 7
except IndexError:
  print "end of index for list 'ID'"

# fetch data for second column and store it in list "notation"
try:
  for row in rows:
    untrimmed = rows[b]
    untrimmed = str(untrimmed)
    trimmed = untrimmed[4:-5]
    notation.append(trimmed)
    b = b + 7
except IndexError:
  print "end of index for list 'notation'"

# fetch data for third column and store it in list "earliestDate"
try:
  for row in rows:
    untrimmed = rows[c]
    untrimmed = str(untrimmed)
    trimmed = untrimmed[4:-5]
    earliestDate.append(trimmed)
    c = c + 7
except IndexError:
  print "end of index for list 'earliestDate'"
  
# fetch data for fourth column and store it in list "latestDate"
try:
  for row in rows:
    untrimmed = rows[d]
    untrimmed = str(untrimmed)
    trimmed = untrimmed[4:-5]
    latestDate.append(trimmed)
    d = d + 7
except IndexError:
  print "end of index for list 'latestDate'"
  
# fetch data for fifth column and store it in list "prefLabelatde"
try:
  for row in rows:
    untrimmed = rows[e]
    untrimmed = str(untrimmed)
    trimmed = untrimmed[4:-5]
    prefLabelatde.append(trimmed)
    e = e + 7
except IndexError:
  print "end of index for list 'prefLabelatde'"

# fetch data for sixth column and store it in list "prefLabelaten"
try:
  for row in rows:
    untrimmed = rows[f]
    untrimmed = str(untrimmed)
    trimmed = untrimmed[4:-5]
    prefLabelaten.append(trimmed)
    f = f + 7
except IndexError:
  print "end of index for list 'prefLabelaten'"
  
# fetch data for seventh column and store it in list "sortOrder"
try:
  for row in rows:
    untrimmed = rows[g]
    untrimmed = str(untrimmed)
    trimmed = untrimmed[4:-5]
    sortOrder.append(trimmed)
    g = g + 7
except IndexError:
  print "end of index for list 'sortOrder'"
  
data = zip(ID, notation, earliestDate, latestDate, prefLabelatde, prefLabelaten, sortOrder)
print data

# open file and write tuple's content to it
with open('zeitfacetten.csv', "w") as zeitfacetten:
    csv.register_dialect("custom", delimiter=",", skipinitialspace=True)
    writer = csv.writer(zeitfacetten, dialect="custom")
    for tup in data:
        writer.writerow(tup)
