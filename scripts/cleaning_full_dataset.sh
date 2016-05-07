# Make into one line per article
for i in disk*txt; do
    sed -i .bak $'s/<title>[^<]*<\/title>/\
/g' $i && rm $i.bak
done

# Remove all non alpha characters
for i in disk*.txt; do
    sed -i .bak 's/[^[:alpha:]\ ]//g' $i && rm $i.bak
done
