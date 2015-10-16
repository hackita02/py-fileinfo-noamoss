import sys
from pathlib import Path 
from collections import defaultdict

if __name__ == '__main__':
	if len(sys.argv)==1:            # print instruction for empty input
		print("""usage: ext_info.py path \n displays number of files and total size of files per extension in the specified path""")

	else:
		def create_dict():
			return {
				'size':0
			}

		result_dict= defaultdict(create_dict)

		folder = Path(sys.argv[1])       #path to explore
		for item in folder.iterdir():
			if item.is_file():
				if item.suffix=="":
					ext="."
				else:
					ext = item.suffix[1:]                 # get items' extension
				result_dict[ext]['size']+=item.stat().st_size         # add items size to result dict

		for ext, size in sorted(result_dict.items()):
			print("{0}: {1}".format(ext,size['size']))