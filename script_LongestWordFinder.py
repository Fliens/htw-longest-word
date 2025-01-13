import glob
import os
import re
import time
from pathlib import Path
from dataclasses import dataclass

ROOTPATH = "/Users/sophia1/Desktop/Texte8mal"

@dataclass
class WordAnalysis:
    # Dataclass to store the analysis results
    language: str
    longest_word: str

def gather_files(directory: str, suffix: str = ".txt") -> list[Path]:
    """
    Gather all files with the given suffix in the directory and its subdirectories
    """

    file_paths = glob.glob(os.path.join(directory, "**", f"*{suffix}"), recursive=True)
    return [Path(file_path) for file_path in file_paths]

def read_file(path: Path) -> str:
    """
    Read the content of the file
    """
    with open(path, "r") as file:
        return file.read()

def process_files(files: dict[Path, str]) -> list[WordAnalysis]:
    """
    Process the files and find the longest word in each language
    """
    languages: list[WordAnalysis] = []  # List to store the results
    for path, content in files.items():
        language = path.parts[-2]   # Get the language from path
        longest_word = find_longest_word(content)

        # Check if the language is already in the list
        existing_language = next((lang for lang in languages if lang.language == language), None)
        if existing_language:   # If the language is already in the list
            # Update the longest word if the new one is longer
            if len(longest_word) > len(existing_language.longest_word):
                existing_language.longest_word = longest_word
        else:
            # Add the new language to the list since it's not there
            languages.append(WordAnalysis(language=language, longest_word=longest_word))
    return languages

def find_longest_word(text: str) -> str:
    """
    Find the longest word in the text
    """
    words = re.findall(r'\w+', text)
    longest_word = max(words, key=len)
    return longest_word

def sort_analysis(languages: list[WordAnalysis]) -> list[WordAnalysis]:
    """
    Sort the analysis results by the length of the longest word
    """
    return sorted(languages, key=lambda x: len(x.longest_word), reverse=True)

if __name__ == "__main__":
    start_time = time.time()
    file_paths = gather_files(ROOTPATH)
    gather_time = time.time() - start_time
    print(f"Found {len(file_paths)} files to process in {gather_time:.2f} seconds.")
    
    # Read all files first
    start_time = time.time()
    files = {path: read_file(path) for path in file_paths}
    read_time = time.time() - start_time
    print(f"Finished reading all files in {read_time:.2f} seconds.")
    
    # Measure time for finding the longest words
    start_time = time.time()
    analyzed_languages = process_files(files)
    process_time = time.time() - start_time
    print(f"Elapsed time for finding longest words: {process_time:.2f} seconds")

    start_time = time.time()
    sorted_results = sort_analysis(analyzed_languages)
    sort_time = time.time() - start_time
    print(f"Elapsed time for sorting results: {sort_time:.2f} seconds")
    
    print("Analysis results:")
    for result in sorted_results:
        print(f"{result.language} - {result.longest_word} - {len(result.longest_word)}")
    
    print(f"Total elapsed time: {gather_time + read_time + process_time + sort_time:.2f} seconds")