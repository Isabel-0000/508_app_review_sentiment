import sys

def get_lines_from_file(filename):
   line_list = []
   with open(filename) as fp:
      line = fp.readline()
      while (line):
         line_list.append(line.rstrip("\n"))
         line = fp.readline()
   return line_list

def main():
   line_list = get_lines_from_file(sys.argv[1])
   print(line_list)
if __name__ == "__main__":
   main() 
