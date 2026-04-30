from dataclasses import dataclass
from math import ceil
from typing import Generic, Iterable, List, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class PageResult(Generic[T]):
    items: List[T]
    total: int
    page: int
    page_size: int
    total_pages: int


def paginate(items: Iterable[T], page: int, page_size: int) -> PageResult[T]:
    items_list = list(items)
    total = len(items_list)
    safe_page = max(page, 1)
    safe_page_size = max(page_size, 1)
    start = (safe_page - 1) * safe_page_size
    end = start + safe_page_size
    paged_items = items_list[start:end]
    total_pages = max(ceil(total / safe_page_size), 1)
    return PageResult(
        items=paged_items,
        total=total,
        page=safe_page,
        page_size=safe_page_size,
        total_pages=total_pages,
    )
