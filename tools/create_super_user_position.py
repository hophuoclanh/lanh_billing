import sys
from pathlib import Path

parent_folder = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_folder))

import dotenv
dotenv.load_dotenv()

import argparse
from domains.authentication.services.user_position_service import create_user_position, get_user_by_id, get_position_by_id
from domains.authentication.schemas.user_position_schema import CreateUserPositionResponseSchema, CreateUserPositionRequestSchema
from repository import SessionLocal

parser = argparse.ArgumentParser(description="Create a new user position")

parser.add_argument("--user_id", required=True, help="User_id")
parser.add_argument("--position_id", required=True, help="Position_id")

args = parser.parse_args()

def main():
    # Initiate a new session
    db = SessionLocal()
    try:
        create_user_position(CreateUserPositionRequestSchema(
            user_id=args.user_id,
            position_id=args.position_id
        ), db)
    except Exception as e:
        print(e)
    finally:
        db.close()

if __name__ == '__main__':
    main()
