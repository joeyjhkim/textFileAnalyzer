from collections import Counter
#Counter is used to count the frequency of items (like words in a file)

#this import statement is needed to let me use the os.path.isdir() to 
# check whether the provided filename is a directory or a file
import os

def textFileAnalyzer(filename):
    
    #using a try block to handle cases where the file might not exist
    try:
        
        #this checks if the provided filename is a directory or a .txt file
        if os.path.isdir(filename):
            print("The path you entered is a directory, not a file. Please enter a valid file path.")
            return
        
        
        #the 'r' opens the file in read mode
        #the 'with' automatically closes the file when done
        with open(filename, 'r') as file:
            
            #reads the file content into a variable. Also converts it to lowercase
            text = file.read().lower()
            
            #splitting the text into a list of words using whitespace as the delimiter
            words = text.split()
            
            #printing the total number of words using len(words)
            print (f"Total words: {len(words)}")
            
            #printing total number of characters using len(text) including spaces and punctuation
            print (f"Total characters: {len(text)}")
            
            #printing the header most common words
            print("Most common words:")
            
            #returning a list of the 5 most common words and their counts
            for word, count in Counter(words).most_common(5):
                print(f"{word}: {count}")
                
    except FileNotFoundError:
        #if the file is not found, this message will be printed
        print("File not found. Please check the filename and try again.")
        
#usage
filename = input("Enter path to a .txt file: ")
textFileAnalyzer(filename)




#Notes
#importing Counter from collections allows me to write code like this
# Counter.(<..>) instead of collections.counter(<..>)
#However, both are still valid ways

#the .read() method is built into the file object
# .read() reads the entire file content as a string
# .readline() reads the file line by line
# .readlines() reads all lines as a list

# .most_common(5) returns a list of the 5 most common words and their counts which is why 
# we have both word and count in the for loop