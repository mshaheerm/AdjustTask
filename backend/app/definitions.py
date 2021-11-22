from enum import Enum


class GroupBy(Enum):
    """
    Types of column to be grouped by
    """

    date = "date"
    channel = "channel"
    country = "country"
    os = "os"


class SumBy(Enum):
    """
    Types of column to be summed by
    """

    impressions = "impressions"
    clicks = "clicks"
    installs = "installs"
    spend = "spend"
    revenue = "revenue"


class OrderDir(Enum):
    """
    The direction to be sorted by
    """

    asc = "asc"  # ascending
    desc = "desc"  # descending

