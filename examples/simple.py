"""Simple Example."""

from argparse_dantic import ArgumentParser, BaseModel, Field

class Arguments(BaseModel):
    """Simple Command-Line Arguments."""

    # Required Args
    string: str = Field(description="a required string", aliases=["-s"])
    integer: int = Field(description="a required integer", aliases=["-i"])
    flag: bool = Field(description="a required flag", aliases=["-f"])

    # Optional Args
    second_flag: bool = Field(False, description="an optional flag")
    third_flag: bool = Field(True, description="an optional flag")


def main() -> None:
    """Simple Main Function."""
    # Create Parser and Parse Args
    parser = ArgumentParser(
        model_class=Arguments,
        prog="Example Program",
        description="Example Description",
        version="0.0.1",
        epilog="Example Epilog",
    )
    args = parser.parse_typed_args()

    # Print Args
    print(args)


if __name__ == "__main__":
    main()
