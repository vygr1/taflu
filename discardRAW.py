import os

basepath = os.getcwd()
jpegList = []
discardCount = 0
duplicateDiscards = []
jpeg = ['.jpeg', '.jpg', '.JPG', '.JPEG']
raw = ['.raw', '.RAW', '.cr2', '.CR2']

# List all jpegs in the current working directory
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        if (os.path.splitext(entry)[1] in jpeg):
            jpegList.append(os.path.splitext(entry)[0])

# Move raw files with no corresponding jpeg to a discards directory
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        if (os.path.splitext(entry)[1] in raw):
            if ((os.path.splitext(entry)[0]) not in jpegList):
                if not os.path.exists('discards'):
                    os.makedirs('discards')
                try:
                    os.rename(os.path.join(basepath, entry), os.path.join(basepath, 'discards', entry))
                except FileExistsError:
                    duplicateDiscards.append(entry)
                discardCount +=1

print(str(len(jpegList)) + ' jpeg file' + 's'[:len(jpegList)!=1])
print(str(discardCount) + ' raw file' + 's'[:discardCount!=1] + ' discarded')

if (len(duplicateDiscards)):
    print("\nThe following files already existed in the discards directory and were not moved:")
    print(*duplicateDiscards, sep = '\n')
