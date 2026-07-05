"""Subscription and Payment models"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Enum, Date
from sqlalchemy.orm import relationship
from datetime import datetime, date
import enum

from app.db.base import Base


class SubscriptionPlan(str, enum.Enum):
    """Subscription plan enumeration"""

    MONTHLY = "monthly"
    ANNUAL = "annual"
    LIFETIME = "lifetime"
    FREE = "free"


class PaymentStatus(str, enum.Enum):
    """Payment status enumeration"""

    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    REFUNDED = "refunded"


class Subscription(Base):
    """Subscription model for user subscriptions"""

    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    plan = Column(Enum(SubscriptionPlan), default=SubscriptionPlan.FREE)
    stripe_subscription_id = Column(String, nullable=True, unique=True)
    status = Column(String, default="active")  # active, cancelled, expired
    start_date = Column(Date, default=date.today)
    end_date = Column(Date, nullable=True)
    auto_renew = Column(Integer, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="subscriptions")
    payments = relationship(
        "Payment", back_populates="subscription", cascade="all, delete-orphan"
    )


class Payment(Base):
    """Payment model for tracking payment transactions"""

    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    subscription_id = Column(Integer, ForeignKey("subscriptions.id"), nullable=False)
    stripe_payment_id = Column(String, nullable=True, unique=True)
    amount = Column(Float, nullable=False)
    currency = Column(String, default="BRL")
    status = Column(Enum(PaymentStatus), default=PaymentStatus.PENDING)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    subscription = relationship("Subscription", back_populates="payments")
