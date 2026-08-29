from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Trade(Base):
    __tablename__ = "trades"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    broker: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    symbol: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    side: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
    )

    quantity: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    entry_price: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    exit_price: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    initial_stop_price: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    initial_target_price: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    pnl: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    setup: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="OPEN",
    )

    opened_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    closed_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )