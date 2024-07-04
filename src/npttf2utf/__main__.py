import pymupdf
#from . import main
import npttf2utf
from base.txthandler import TxtHandler

"""
if __name__ == "__main__":
    main()
"""

doc = pymupdf.open("/Users/connorlee/Documents/loomaProgramsML/Looma24/nepali-1-2464 (dragged).pdf") # open a document
out = open("text.txt", "wb") # create a text output
for page in doc: # iterate the document pages
    text = page.get_text().encode("utf8") # get plain text (is in UTF-8)
    out.write(text) # write text of page
    out.write(bytes((12,))) # write page delimiter (form feed 0x0C)
out.close()

converter = TxtHandler("./map.json")
converter.map_fonts("text.txt", output_file_path="out.txt", from_font="Preeti", to_font="unicode", components=[], known_unicode_fonts=[])