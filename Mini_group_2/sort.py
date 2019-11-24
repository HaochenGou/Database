import os
os.system("sort -u recs.txt -o recs.txt")
os.system(" perl break.pl < recs.txt | db_load -T -t hash re.idx")

os.system("sort -u terms.txt -o terms.txt")
os.system("perl break.pl < terms.txt | db_load -c duplicates=1 -T -t btree te.idx")

os.system("sort -u emails.txt -o emails.txt")
os.system("perl break.pl < emails.txt | db_load -c duplicates=1 -T -t btree em.idx")

os.system("sort -u dates.txt -o dates.txt") 
os.system("perl break.pl < dates.txt | db_load -c duplicates=1 -T -t btree da.idx")