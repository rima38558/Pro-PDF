#!/usr/bin/env python3
"""Seed default plans into the database.

Usage: python backend/scripts/seed_plans.py
"""
from app import models
from app.database import engine, SessionLocal
from sqlalchemy.exc import IntegrityError


def seed():
    db = SessionLocal()
    try:
        defaults = [
            {"name": "free", "price_cents": 0, "currency": "INR", "monthly": True},
            {"name": "pro", "price_cents": 1999, "currency": "INR", "monthly": True},
        ]
        for p in defaults:
            exists = db.query(models.Plan).filter_by(name=p["name"]).first()
            if exists:
                print(f"Plan '{p['name']}' already exists, skipping")
                continue
            plan = models.Plan(**p)
            db.add(plan)
        db.commit()
        print("Seeding complete.")
    except IntegrityError as e:
        db.rollback()
        print("Integrity error while seeding:", e)
    finally:
        db.close()


if __name__ == '__main__':
    # ensure tables exist
    models.Base.metadata.create_all(bind=engine)
    seed()
