def setup():
    size(800, 800)  # Window size
    background(255)  # White background
    textSize(16)  # Set text size for displaying information

    # createReader() - Creates a BufferedReader object to read from a file
    global reader
    reader = createReader("example.txt")  # Make sure you have an 'example.txt' file in your sketch folder

    # loadBytes() - Loads a file into a byte array
    global byteData
    byteData = loadBytes("example.txt")  # Make sure you have an 'example.txt' file in your sketch folder

    # loadStrings() - Loads a file into an array of strings
    global lines
    lines = loadStrings("example.txt")  # Make sure you have an 'example.txt' file in your sketch folder

    # loadXML() - Loads an XML file and returns an XML object
    global xml
    xml = loadXML("example.xml")  # Make sure you have an 'example.xml' file in your sketch folder

    # parseXML() - Parses a string or file as an XML object
    global parsedXML
    xmlString = """<root><child>Example</child></root>"""
    parsedXML = parseXML(xmlString)

    # selectFolder() - Opens a dialog box to select a folder
    selectFolder("Select a folder", "folderSelected")

    # selectInput() - Opens a dialog box to select a file
    selectInput("Select a file to read", "fileSelected")

def draw():
    background(255)  # Clear background
    fill(0)  # Black text color

    # Display the first line from the reader
    try:
        line = reader.readLine()
        if line:
            text(f"First line: {line}", 10, 20)
    except:
        text("No more lines to read", 10, 20)

    # Display the first byte from the byte array
    if byteData:
        text(f"First byte: {byteData[0]}", 10, 40)

    # Display the first string from the array of strings
    if lines:
        text(f"First line from loadStrings: {lines[0]}", 10, 60)

    # Display the first child element from the loaded XML
    if xml:
        text(f"First XML child: {xml.getChild('child').getContent()}", 10, 80)

    # Display the content of the parsed XML
    if parsedXML:
        text(f"Parsed XML content: {parsedXML.getChild('child').getContent()}", 10, 100)

def folderSelected(selection):
    if selection:
        print("Folder selected:", selection)
    else:
        print("Folder selection was canceled.")

def fileSelected(selection):
    if selection:
        print("File selected:", selection)
    else:
        print("File selection was canceled.")


