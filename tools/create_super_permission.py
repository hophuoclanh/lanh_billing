import sys
import os
from pathlib import Path

parent_folder = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_folder))

import dotenv
dotenv.load_dotenv()

import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from domains.authentication.services.permission_service import create_permission
from domains.authentication.schemas.permission_schema import CreatePermissionRequestSchema, PermissionResponseSchema


parser = argparse.ArgumentParser(description="Create a new permission")

parser.add_argument("--action", required=True, help="Action")
parser.add_argument("--resource", required=True, help="Resource")

args = parser.parse_args()

DATABASE_URL = os.getenv('DATABASE_URL')

def main():
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    with SessionLocal() as db:
        create_permission(CreatePermissionRequestSchema(
            action=args.action,
            resource=args.resource
        ), db)

if __name__ == '__main__':
    main()
