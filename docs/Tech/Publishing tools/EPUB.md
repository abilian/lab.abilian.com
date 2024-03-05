EPUB is an e-book file format that uses the ".epub" file extension. The term is short for electronic publication and is sometimes stylized as ePub. EPUB is supported by many e-readers, and compatible software is available for most smartphones, tablets, and computers. EPUB is a technical standard published by the International Digital Publishing Forum (IDPF). It became an official standard of the IDPF in September 2007, superseding the older Open eBook (OEB) standard. 

EPUB allows for reflowable content, meaning the text can adjust to fit different screen sizes and resolutions. The structure of an EPUB file is essentially that of a zipped folder containing a set of web standards-based files. These files include HTML or XHTML for content, CSS for styling, and SVG for vector images, among others. 

Here's a breakdown of the core components of an EPUB file:

1. **MIME Type File**: A file named `mimetype` that contains a single line specifying the MIME type of the file (`application/epub+zip`). This file must be the first in the ZIP archive and must not be compressed.

2. **META-INF Folder**: Contains metadata and configuration files. The most important file in this directory is `container.xml`, which points to the EPUB file's rootfile (usually the `.opf` file). This file defines the location of the eBook's content within the EPUB file.

3. **OPF (Open Packaging Format) File**: Usually named `content.opf`, this file is located within the EPUB package and contains metadata about the eBook (such as the title, author, and publisher), a manifest listing all the files included in the EPUB file, a spine that specifies the order of the content documents, and a guide that can reference key positions within the text.

4. **Content Documents**: These are primarily XHTML or HTML files that contain the actual content of the eBook, such as chapters, sections, and any embedded images or media. CSS files are used alongside these documents for styling purposes.

5. **Images and Media**: EPUB files can include images, videos, and audio files. These are usually stored in their own directories within the EPUB archive.

6. **NCX (Navigation Control file for XML)**: Although its use is becoming less common in favor of the navigation document in EPUB 3, the NCX file (`toc.ncx`) provides a hierarchical table of contents for the eBook.

7. **Navigation Document**: In EPUB 3, the navigation document (usually an XHTML file) replaces the NCX file, providing navigation information (like the table of contents) in a way that's both human-readable and machine-readable.

8. **Additional Files and Directories**: Depending on the complexity of the eBook, an EPUB file may also include JavaScript files for interactivity, font files for custom typography, and other assets like footnotes, annotations, or special formatting files.

The EPUB format is designed to be both open and flexible, supporting a wide range of content presentations and interactivity. Its structure is standardized by the International Digital Publishing Forum (IDPF), ensuring broad compatibility across different e-readers and software.

## More info

- https://en.wikipedia.org/wiki/EPUB