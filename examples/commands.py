"""Commands Example."""

from argparse_dantic import (
    ArgumentParser, BaseModel, Field, ActionNameBind,
    FilePath, IPvAnyAddress
)

from typing import Optional

class MyBaseModel(BaseModel):
    action_name: ActionNameBind

class BuildCommand(MyBaseModel):
    """Build Command Arguments."""

    # Required Args
    location: FilePath = Field(description="build location")


class ServeCommand(MyBaseModel):
    """Serve Command Arguments."""

    # Required Args
    address: IPvAnyAddress = Field(description="serve address")
    port: int = Field(description="serve port")


class Arguments(MyBaseModel):
    """Command-Line Arguments."""

    # Optional Args
    verbose: bool = Field(False, description="verbose flag")

    # Commands
    build: Optional[BuildCommand] = Field(description="build command")
    serve: Optional[ServeCommand] = Field(description="serve command")


def main() -> None:
    """Main Function."""
    # Create Parser and Parse Args
    parser = ArgumentParser(
        model=Arguments,
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
