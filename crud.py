from sqlalchemy.orm import Session

import models, schemas


def get_message(db: Session, message_id: int):
    return db.query(models.Messages).filter(models.Messages.id == message_id).first()


def get_message_by_contact(db: Session, contact_name: str):
    return db.query(models.Messages).filter(models.Messages.contact_name == contact_name)


def get_messages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Messages).offset(skip).limit(limit).all()


def create_message(db: Session, message: schemas.MessageCreate):
    db_message = models.Messages(
        contact_name=message.contact_name,
        user_name=message.user_name,
        client_phone=message.client_phone,
        owner_phone=message.owner_phone,
        is_group=message.is_group,
        message_time=message.message_time
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message