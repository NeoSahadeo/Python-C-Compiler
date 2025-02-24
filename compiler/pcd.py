# Python Compiler Driver (PCD)
# by Neo Sahadeo
# RtD

from enum import Enum
import argparse
import logging
import datetime
import pathlib
import re

file_log = f"pcd_{datetime.date.today()}_{datetime.datetime.now().time()}".replace(":", "_").replace(".", "_") + ".log"
logger = logging.getLogger(__name__)


class Token(Enum):
    ...


def tokeniser(tokens):
    """
    Creates token objects from token array.

    :param [] tokens: token list
    :returns [] token_objects: token objects
    """


def read_file(file, block_size=10_000):
    """
    Reads in data stream from a file and yields the
    data in blocks.

    :param str file: file stream
    :param optional int file: block size (DEFAULT=10_000)

    :yields block: lines of file stream
    """
    logger.info(f"reading in block: max block_size: {block_size}")
    block = []
    for line in file:
        block.append(line)
        if len(block) == block_size:
            logger.info("block sized reach, yielding block")
            yield block
            block = []
    logger.info("yielding block")
    yield block  # Return if block_size isn't reached


def lexer(file):
    """
    Lexer function that tokenises the inputfile.

    :param str file: file location

    :returns [token]: token array
    :raises FileNotFoundError: file parameter does not exist
    """
    logger.info("running lexer")
    tokens = []
    try:
        logger.info(f"attempting to open: {file}")
        with pathlib.Path(file).open('r') as file:
            logger.info("file opened successfully")
            for block in read_file(file):
                for line in block:
                    logger.info("searching block")
                    matches = re.finditer(r"\b([a-zA-Z]\w*|\d+\b)|(\S)", line, flags=re.MULTILINE)
                    for match in matches:
                        tokens.append(match.group(0))
            return tokens
    except FileNotFoundError:
        logger.error(f"file does not exist: {file}")
        return 1


def parser():
    logger.info("running parser")


def assembler():
    logger.info("running assembler")


if __name__ == "__main__":
    p = argparse.ArgumentParser(
        prog="Python Compiler Driver",
        description="A Compiler Driver for the C programming language. Currently its a wrapper around gcc."
    )
    p.add_argument("inputfile")
    p.add_argument("-o", "--output")
    p.add_argument("--lex", action="store_true", help="run just the lexer")
    p.add_argument("--parser", action="store_true", help="run both the lexer and parser")
    p.add_argument("--codegen", action="store_true", help="run the lexer, parser, and assembler but stop before code emission")
    p.add_argument("--log", help="output logging", action="store_true")
    args = p.parse_args()

    if args.log:
        logging.basicConfig(filename=file_log, level=logging.INFO)
        logger.info(f"started: {datetime.datetime.now()}")

    DEFAULT_NAME = "a.out"
    if args.output:
        DEFAULT_NAME = args.output

    if args.lex:
        lexer(args.inputfile)
    elif args.parser:
        parser()
    elif args.codegen:
        assembler()

    logger.info(f"ended: {datetime.datetime.now()}")
