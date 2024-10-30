import logging
import sys
from textwrap import TextWrapper

import datasets
import huggingface_hub
import matplotlib.font_manager as font_manager
import matplotlib.pyplot as plt
import torch
import transformers
from IPython.display import set_matplotlib_formats

is_gpu_available = torch.cuda.is_available()


def display_library_version(library):
    print(f"Using {library.__name__} v{library.__version__}")


def setup():
    # Check if we have a GPU
    if not is_gpu_available:
        print("No GPU was detected! This notebook can be *very* slow without a GPU 🐢")
    # Give visibility on versions of the core libraries
    display_library_version(transformers)
    display_library_version(datasets)
    # Disable all info / warning messages
    transformers.logging.set_verbosity_error()
    datasets.logging.set_verbosity_error()


def wrap_print_text(print):
    """Adapted from: https://stackoverflow.com/questions/27621655/how-to-overload-print-function-to-expand-its-functionality/27621927"""

    def wrapped_func(text):
        if not isinstance(text, str):
            text = str(text)
        wrapper = TextWrapper(
            width=80,
            break_long_words=True,
            break_on_hyphens=False,
            replace_whitespace=False,
        )
        return print("\n".join(wrapper.fill(line) for line in text.split("\n")))

    return wrapped_func


print = wrap_print_text(print)
