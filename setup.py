import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:

    long_description = fh.read()
setuptools.setup(
  name = "freeAI",
  version = "1.0",
  description = "this is a python package to use the completely free chatGPT and more models.",
  long_description = README,
  url = "https://github.com/HotDrify/freeAI",
  author = "HotDrify",
  license = "Apache License 2.0",
  keywords = [
    "chatBot",
    "freeAI",
    "freeGPT",
    "freeChatGPT",
    "gptfree",
    "freeAPI",
    "python",
    "api",
  ],
  python_requires = ">=3.8",
  classifiers = [

        "Programming Language :: Python :: 3",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",


