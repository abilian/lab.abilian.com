https://en.wikipedia.org/wiki/General-purpose_macro_processor
https://github.com/fyngyrz/aa_macro
https://pyexpander.sourceforge.io/index.html

A general-purpose macro processor, also known as a general-purpose preprocessor, serves as a versatile tool for text manipulation and transformation, independent of any specific programming language or software application. Unlike macro processors tightly integrated with a particular language or software, these tools offer a broader scope of functionality and applicability.

At its core, a macro processor operates by taking input text, often referred to as a stream, and systematically replacing specified patterns with predefined substitutions as it processes the text. These substitutions can range from simple textual replacements to more complex transformations involving decision-making logic. 

One of the primary functions of a macro processor is language expansion. This involves defining new language constructs or functionalities that can be expressed using existing components of a given language. By enabling developers to extend the language in this way, macro processors facilitate the creation of domain-specific languages or the enhancement of existing ones, making them more expressive and tailored to specific tasks or domains.

Furthermore, macro processors excel in facilitating systematic text replacements that require conditional or context-dependent decision-making. For instance, they can be employed to selectively extract or modify sections of text based on predefined criteria, enabling users to automate tasks such as data extraction, content filtering, or formatting.

Moreover, macro processors are invaluable tools for text reformatting tasks, where they can be used to enforce consistent styling, layout, or structure across documents or codebases. For example, in the context of web development, macro processors can assist in conditionally including or excluding content from HTML files based on parameters such as device type, user preferences, or environmental variables.

Macro processors can manifest in various forms, ranging from embedded components within other software tools such as assemblers and compilers to standalone programs designed to process arbitrary text. Regardless of their implementation, the flexibility and power of macro processors make them indispensable assets in the arsenal of developers, system administrators, and content creators seeking to automate and streamline text manipulation tasks across diverse domains and contexts.

## Usage

Here are some examples illustrating the use of a general-purpose macro processor:

1. **Language Extension**:
   - **C Preprocessor (cpp)**: The C preprocessor is a classic example of a macro processor tightly integrated with the C programming language. However, its capabilities extend beyond C itself. Developers often use cpp to define macros and perform text substitutions that extend the syntax of C, enabling features such as conditional compilation, code generation, and header file inclusion.

2. **Systematic Text Replacements**:
   - **Search and Replace Operations**: A macro processor can be used to perform bulk search and replace operations across multiple files or documents. For example, replacing outdated function names with updated ones in a codebase.
   - **Data Extraction**: Extracting specific data from structured text files, such as log files or CSV files, based on predefined patterns or criteria.

3. **Text Reformatting**:
   - **HTML Templating**: Using a macro processor to create HTML templates with placeholders for dynamic content, allowing for easy generation of consistent web pages.
   - **Code Formatting**: Automatically formatting code according to predefined style guidelines, such as indentations, line breaks, and spacing.

4. **Code Generation**:
   - **Code Templates**: Generating boilerplate code or repetitive constructs using macros to increase productivity and maintain consistency across projects.
   - **Automatic Documentation**: Generating documentation from annotated source code by extracting comments and metadata using macros.

5. **Domain-Specific Language (DSL) Development**:
   - **Custom Configuration Files**: Creating DSLs for configuring software systems, where macros are used to define domain-specific constructs and behaviors.
   - **Rule-based Systems**: Implementing rule-based systems for decision-making or inference engines using macros to express rules and conditions.

6. **Conditional Text Manipulation**:
   - **Feature Toggling**: Including or excluding features in software applications based on configuration settings or compile-time flags using conditional macros.
   - **Content Filtering**: Selectively including or excluding sections of text in documents or reports based on specified criteria.

7. **Documentation Generation**:
   - **Static Site Generation**: Using a macro processor to generate static websites from templates, where macros are used to insert dynamic content or apply site-wide changes.
   - **API Documentation**: Automatically generating API documentation from annotated source code, where macros extract metadata and format it into documentation templates.

## Examples

1. **GNU m4**:
   - **Description**: GNU m4 is an implementation of the m4 macro processor, which is a powerful general-purpose macro processor widely used in software development, system administration, and text processing tasks.
   - **Features**: It supports macro expansion, conditional text processing, recursion, file inclusion, and other advanced text manipulation capabilities.
   - **Link**: [GNU m4 on GNU Project](https://www.gnu.org/software/m4/)

2. **Jinja2**:
   - **Description**: Jinja2 is a modern and designer-friendly templating engine for Python programming language. While primarily designed for web development, Jinja2 can be used for general-purpose text processing and template rendering.
   - **Features**: Jinja2 supports template inheritance, macros, control structures, and automatic escaping, making it suitable for generating dynamic content in web applications, configuration files, and documentation.
   - **Link**: [Jinja2 on GitHub](https://github.com/pallets/jinja)

3. **Apache FreeMarker**:
   - **Description**: Apache FreeMarker is a template engine for Java-based web applications and other text-processing tasks. It provides a flexible and extensible framework for generating dynamic content based on templates.
   - **Features**: FreeMarker supports macros, conditionals, loops, and other control structures, along with integration with Java objects and data models.
   - **Link**: [Apache FreeMarker on Apache Software Foundation](https://freemarker.apache.org/)

4. **Mustache**:
   - **Description**: Mustache is a logic-less template syntax implemented in various programming languages. It aims to provide a simple and straightforward way to generate dynamic content without introducing complex programming constructs.
   - **Features**: Mustache templates are language-agnostic and support variable interpolation, sections, and partials, making them suitable for a wide range of applications.
   - **Link**: http://mustache.github.io/ (→ specifications and implementations in many languages)

5. **Handlebars.js**:
   - **Description**: Handlebars.js is a JavaScript templating engine inspired by Mustache. It simplifies the process of generating HTML markup dynamically in web applications by providing a familiar syntax and powerful features.
   - **Features**: Handlebars.js supports template inheritance, helpers, partials, and data binding, enabling developers to build dynamic and interactive user interfaces with ease.
   - **Link**: [Handlebars.js on GitHub](https://github.com/handlebars-lang/handlebars.js/)
