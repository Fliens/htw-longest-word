import glob
import os
import re
import time
from pathlib import Path
from dataclasses import dataclass
import asyncio
import aiofiles

@dataclass
class WordAnalysis:
    language: str
    longest_word: str

ROOTPATH = "data"

def find_longest_word(text: str) -> str:
    words = re.findall(r'\w+', text)
    longest_word = max(words, key=len)
    return longest_word

def gather_files(directory: str, suffix: str = ".txt") -> list[Path]:
    file_paths = glob.glob(os.path.join(directory, "**", f"*{suffix}"), recursive=True)
    return [Path(file_path) for file_path in file_paths]

async def read_file(path: Path) -> str:
    async with aiofiles.open(path, "r") as file:
        return await file.read()

def update_languages(languages: list[WordAnalysis], language: str, longest_word: str):
    existing_language = next((lang for lang in languages if lang.language == language), None)
    if existing_language:
        if len(longest_word) > len(existing_language.longest_word):
            existing_language.longest_word = longest_word
    else:
        languages.append(WordAnalysis(language=language, longest_word=longest_word))

async def load_files(paths: list[Path]) -> dict[Path, str]:
    file_contents = {}
    async with asyncio.TaskGroup() as tg:
        for path in paths:
            file_contents[path] = await tg.create_task(read_file(path))
    return file_contents

def analyze_files(file_contents: dict[Path, str]) -> list[WordAnalysis]:
    languages: list[WordAnalysis] = []
    for path, text in file_contents.items():
        language = path.parts[-2]  # Extract language from path
        longest_word = find_longest_word(text)
        update_languages(languages, language, longest_word)
    return languages

def sort_analysis(languages: list[WordAnalysis]) -> list[WordAnalysis]:
    return sorted(languages, key=lambda x: len(x.longest_word), reverse=True)

async def main():
    print("Gathering files...")
    files = gather_files(ROOTPATH)
    print(f"Found {len(files)} files.")

    print("Loading files...")
    file_contents = await load_files(files)
    print("Files loaded.")

    print("Analyzing files...")
    time_measurement = time.time()
    analyzes = analyze_files(file_contents)
    time_measurement = time.time() - time_measurement
    print("Files analyzed.")

    print("Sorting analysis results...")
    sorted_analysis = sort_analysis(analyzes)
    print("Analysis results sorted.")

    print(sorted_analysis)
    print(f"Analysis took {time_measurement:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())