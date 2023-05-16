import sys
from pathlib import Path

parent_folder = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_folder))

import dotenv
dotenv.load_dotenv()

import argparse
from domains.authentication.services.position_service import create_position
from domains.authentication.schemas.position_schema import CreatePositionRequestSchema, PositionResponseSchema


parser = argparse.ArgumentParser(description="Create a new position")

parser.add_argument("--role", required=True, help="Role")

args = parser.parse_args()

def main():
    create_position(CreatePositionRequestSchema(
        role=args.role
    ))

if __name__ == '__main__':
    main()
