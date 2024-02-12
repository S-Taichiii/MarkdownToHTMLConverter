import sys
import os
import markdown

class FileConverter:
    def __init__(self):
        self.argv = None
        self.convert()

    def validArgv(self):
        # Length of input command must be 4
        if len(self.argv) != 4:
            print('Your input command is wrong.')
            return False

        # Name of command is 'markdown'
        markdown = sys.argv[1]
        if markdown != 'markdown':
            print("Your input command is wrong.")
            return False

        # Check validity of input file
        inputFile = sys.argv[2]
        if os.path.exists(inputFile):
            input_ext = os.path.splitext(inputFile)[1]
            if input_ext != ".md":
                print('Input file is in the wrong format.')
                return False
        else:
            print('Input file does not exist.')
            return False
        
        # Check validity of output file
        outputFile = sys.argv[3]
        if os.path.exists(outputFile):
            output_ext = os.path.splitext(outputFile)[1]
            if output_ext != ".html":
                print('Output file is in the wrong format.')
                return False
        else:
            print('Output file does not exist.')
            return False
        
        return True
        
    def convert(self):
        self.argv = sys.argv

        if not self.validArgv():
            self.close()

        input_path = sys.argv[2]
        output_path = sys.argv[3]
        contents_md = ""
        with open(input_path, 'r') as f:
            contents_md = f.read()
        with open(output_path, 'w') as f:
            contents_html = markdown.markdown(contents_md)
            f.write(contents_html)
        
        print('Succesfully converted!!')


    def close(self):
        print('Closing thie program.')
        sys.exit(1)

if __name__ == '__main__':
    FileConverter()