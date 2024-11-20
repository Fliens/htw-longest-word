#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Imports


# In[2]:


import os


# In[3]:


import findspark
findspark.init()


# In[4]:


import re


# In[5]:


from pyspark import SparkConf, SparkContext


# In[6]:


# Initialize


# In[7]:


conf = SparkConf().setMaster("local[*]").setAppName("LongestWordFinder")


# In[8]:


sc = SparkContext(conf=conf)


# In[9]:


# Function to find the longest word in an RDD
def find_longest_word(file_path):
    rdd = sc.textFile(file_path)
    longest_word = (
        rdd.flatMap(lambda t: re.findall(r"\w+", t))         # Tokenize words -> r in findall means raw string
        .map(lambda w: (w, len(w)))                          # Map: Pair each word with its length
        .reduce(lambda a, b: a if a[1] > b[1] else b)        # Reduce: Find the longest word
    )
    return longest_word


# In[10]:


# Load text files from this folder
parent_folder = "/Users/sophia1/Desktop/texts"


# In[11]:


results = []


# In[12]:


# Loop through each language folder
for language_folder in os.listdir(parent_folder):
    language_path = os.path.join(parent_folder, language_folder)

    # if it's a directory (it is a language folder) -> get all txt files
    if os.path.isdir(language_path):
        text_files = os.path.join(language_path, "*.txt")

        # Find the longest word in this language and save it
        longest_word, length = find_longest_word(text_files)
        results.append((language_folder, longest_word, length))


# In[13]:


# Sort results by the length of the longest word
sorted_results = sorted(results, key=lambda x: x[2], reverse=True)


# In[14]:


for language, word, length in sorted_results:
    print(f"{language} – {word} – {length}")


# In[ ]:




