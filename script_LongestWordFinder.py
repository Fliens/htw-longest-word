import glob
import os
import re
import time
from pathlib import Path
from dataclasses import dataclass

ROOTPATH = "data"

@dataclass
class WordAnalysis:
    language: str
    longest_word: str

def find_longest_word(text: str) -> str:
    words = re.findall(r'\w+', text)
    longest_word = max(words, key=len)
    return longest_word

def gather_files(directory: str, suffix: str = ".txt") -> list[Path]:
    file_paths = glob.glob(os.path.join(directory, "**", f"*{suffix}"), recursive=True)
    return [Path(file_path) for file_path in file_paths]

def read_file(path: Path) -> str:
    with open(path, "r") as file:
        return file.read()

def update_languages(languages: list[WordAnalysis], language: str, longest_word: str):
    existing_language = next((lang for lang in languages if lang.language == language), None)
    if existing_language:
        if len(longest_word) > len(existing_language.longest_word):
            existing_language.longest_word = longest_word
    else:
        languages.append(WordAnalysis(language=language, longest_word=longest_word))

def process_files(paths: list[Path]) -> list[WordAnalysis]:
    languages: list[WordAnalysis] = []
    for path in paths:
        language = path.parts[-2]   # Extract language from path
        with open(path, "r") as file:
            text = file.read()
        longest_word = find_longest_word(text)
        update_languages(languages, language, longest_word)
    return languages

def sort_analysis(languages: list[WordAnalysis]) -> list[WordAnalysis]:
    return sorted(languages, key=lambda x: len(x.longest_word), reverse=True)

if __name__ == "__main__":
    time_measurement = time.time()
    files = gather_files(ROOTPATH)
    analyzes = process_files(files)
    sorted_analyzes = sort_analysis(analyzes)
    
    time_measurement = time.time() - time_measurement
    
    print(sorted_analyzes)
    print(f"Elapsed time: {time_measurement:.2f} seconds")