#5 things I want to do to clean my data
#1. change headings to something more clear
#2. delete columns (first 2, currency, last 4 columns)
#3. change bytes to MB
#4. delete rows with user_rating = 0
#5. compute percentange change in ratings for newest version


#6. UTC change

import csv
import codecs

lines_written, lines_read = 0,0

f = codecs.open("applestore_utf8.csv", "r", "utf-8")
out_file_name = "applestore_out.csv"
t = codecs.open(out_file_name,'w',"utf-8")
writer = csv.writer(t,delimiter=",")

#1. change headings to something more clear
writer = csv.writer(t)
writer.writerow(["App Name", "Size (in MB)", "Price", "Total Ratings (for all versions)", 
                     "Total Ratings (for new version)", "Average User Rating (for all versions)", 
                     "Average User Ratings(for current version)", "Current Version", "Content Rating",
                     "Genre", "Rating Change from Old to New Version (%)"])

#2. delete columns (first 2, currency, last 4 columns)
for line in f:
    lines_read += 1
    data = line.split(",")
    new_data = data[2:4]+data[5:13]
    
    if not new_data[1].isnumeric():
        new_data.remove(new_data[1])
        
    new_data[0] = new_data[0].replace('"', '')
    
#4. delete rows with user_rating = 0

    if new_data[5] == "0" or new_data[0] == '"' or new_data[2] == "USD" or not new_data[1].isnumeric():
        continue
    
#3. change bytes to MB
    if new_data[1].isnumeric():
        new_data[1] = float(new_data[1])/1000000
        new_data[1] = round(new_data[1], 2)


#5. compute percentange change in ratings for newest version

    new_list=[]

    if new_data[6].isnumeric():
        new_list = ((float(new_data[6])-float(new_data[5]))/float(new_data[5]))*100
        new_list = round(new_list, 2)
        new_data.insert(13,new_list)


        writer.writerow(new_data)
        lines_written +=1

        
f.close()
t.close()
