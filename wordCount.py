import os

# Function to count words from a file
def wordcountfun(filename):
    with open(filename, 'rb') as file:
        text = file.read().decode('utf-8')
        words = text.split()
        return len(words)

#counting the words in a text file
files = os.listdir('/home/data')
word_count=[]
for file in files:
    filepath = os.path.join('/home/data', file)
    word_count.append(wordcountfun(filepath))
    if file == 'IF.txt':
        with open(filepath, 'rb') as f:
            text = f.read().decode('utf-8')
            words = text.split()
            word_freq = {}
            for word in words:
                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1

        # Get the top 3 words by frequency
        top_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:3]

#getting the ipaddress
import socket
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

# Writing the output to a result text file
with open('/home/output/result.txt', 'w') as file:
    file.write("files in the location: \n")
    for textfile in files:
        file.write(f'{textfile}\n')
    file.write("\n\n")
    file.write("word count: \n")
    for i in range(len(word_count)):
        file.write(f'{files[i]} - {word_count[i]}\n')
    file.write(f'Total number of words: {sum(word_count)}\n\n')
    file.write('Top 3 words with frequency in IF.txt:\n')
    for word, freq in top_words:
        file.write(f'{word}: {freq}\n')
    file.write(f'\nIP address of the machine: {ip_address}')
    
# printing the output to console
with open('/home/output/result.txt', 'rb') as file:
    print(file.read().decode('utf-8'))
