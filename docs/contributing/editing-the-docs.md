# Editing the Docs

The Hercules docs could always use help. It is an ever changing repository of useful information related to Hercules, such as configuration, connecting, setting up, Compiling and scripting. However, please follow the below points when trying to edit.

1. Do not create pages or guides for custom content. Base client specific content is OK, as this is the main point behind Hercules. However, leave patchers, custom patches or plugins, setup of custom items or mobs, or control panels out.
2. Be sure you write in proper and complete English.
3. For code examples, be sure you follow [Hercules' Coding Style](./coding-style.md). 


## Contributting
Hercules docs is completely based on the repository files, in order to contribute to it, simply
submit a [Pull request](./creating-pull-requests.md) to the [Hercules-docs repository](https://github.com/HerculesWS/hercules-docs).


## Setup
Hercules docs uses mkdocs-material.

You will need to have Python3 installed, and install `mkdocs-material` and our lexer packages.

You can install it with:
```SH
pip install mkdocs-material
pip install -e ./hercscript-lexer # Optional, required for HercScript highlighting
```

or perform the same commands with `pip3`.

For more information about installing mkdocs-material, and other alternatives,
see [Mkdocs Material's getting started](https://squidfunk.github.io/mkdocs-material/getting-started/#installation)

After installing mkdocs-material, in order to run hercules docs in your machine, you will have to:

1. Clone hercules-docs repository to your local machine
2. Open a terminal in the folder and run `mkdocs serve`
3. The documentation should be running at http://localhost:8000


## Editing
The documentation is entirely written in Markdown, with some extensions from mkdocs and mkdocs-material.

If you are new to markdown or want to know about the extended syntax from mkdocs, please check the following links:

- [Markdown Syntax](https://www.markdownguide.org/basic-syntax/)
- [Mkdocs Material Reference](https://squidfunk.github.io/mkdocs-material/reference/)
