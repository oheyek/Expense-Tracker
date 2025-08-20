from setuptools import setup

setup(
    name="expense-tracker",
    version="0.1",
    py_modules=["main"],
    entry_points={
        "console_scripts": [
            "expense-tracker = main:main",
        ],
    },
)