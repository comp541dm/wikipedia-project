# Make into one line per article
for i in disk*txt; do
    sed -i .bak $'s/<title>[^<]*<\/title>/\
/g' $i && rm $i.bak
done

# Remove all non alpha characters
for i in disk*.txt; do
    sed -i .bak 's/[^[:alpha:]\ ]//g' $i && rm $i.bak
done

# Remove all duplicate spaces
# Not sure if needed but saves some bytes
for i in disk*.txt; do
    tr -s '[:space:]' < $i | tr '[:upper:]' '[:lower:]' > $i.bak && mv $i.bak $i
done

# Hopefully remove talk articles
for i in disk*.txt; do
    sed -i .bak '/wikipedia/d' $i && rm $i.bak
done

for i in disk*.txt; do
    sed -i .bak '/talk/d' $i && rm $i.bak
done
