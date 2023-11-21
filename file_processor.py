
import argparse
from file_handling import process_files, process_links
from utils import create_directories

def main():
    parser = argparse.ArgumentParser(description='File and Web Content to GPT Knowledge Converter')
    parser.add_argument('--files', type=str, help='Input directory containing files')
    parser.add_argument('--links', type=str, help='Text file containing URLs')
    args = parser.parse_args()

    create_directories(['./tmp', './output'])

    if args.files:
        process_files(args.files, './tmp', './output')
    elif args.links:
        process_links(args.links, './tmp', './output')
    else:
        print("No input provided. Please use --files or --links to specify input.")

if __name__ == '__main__':
    main()
