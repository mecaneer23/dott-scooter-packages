#!/usr/bin/env python3
"""
Calculate the best scooter package given certain factors
"""

from collections.abc import Iterable
from sys import maxsize
from typing import NamedTuple


class Rides(NamedTuple):
    """Represent an amount of rides with equal length"""

    amount: int
    minutes: int


class Package:
    """Represent a scooter bundle pricing package"""

    def __init__(
        self,
        package_price: int,
        unlock_price: int,
        price_per_minute: int,
        max_rides: int = 0,
        max_ride_length: int = maxsize,
    ) -> None:
        self.package_price = package_price
        self.unlock_price = unlock_price
        self.price_per_minute = price_per_minute
        self.max_rides = max_rides
        self.max_ride_length = max_ride_length

    @staticmethod
    def _get_package_multiplier(amount_of_rides: int, max_rides: int) -> int:
        """
        Return the amount of times the package must be purchased
        to ride `amount_of_rides` times

        If max_rides is <= 0, allow infinite rides
        """
        if amount_of_rides <= 0:
            msg = "`amount_of_rides` must be greater than zero"
            raise ValueError(msg)

        if max_rides <= 0:
            return 1

        return max(1, -(-amount_of_rides // max_rides))

    def get_price(self, rides: Iterable[Rides] | Rides) -> int:
        """Return the price for a certain amount of `m` length rides"""
        total_rides, overtime_fee, total_per_minute = 0, 0, 0
        if isinstance(rides, Rides):
            rides = [rides]

        for ride in rides:
            total_rides += ride.amount
            overtime_fee += max(0, ride.minutes - self.max_ride_length)
            total_per_minute += (
                self.price_per_minute * ride.minutes * ride.amount
            )

        return (
            self.package_price
            * self._get_package_multiplier(total_rides, self.max_rides)
            + self.unlock_price * total_rides
            + total_per_minute
            + overtime_fee * total_rides
        )

    def __str__(self) -> str:
        return f"{self.package_price}".zfill(2)


def get_packages() -> list[Package]:
    """Return a list of Packages which represent available Dott Packages"""
    return [
        Package(16, 0, 1),
        Package(18, 0, 0, 2, 30),
        Package(19, 9, 0, max_ride_length=30),
        Package(45, 6, 0, max_ride_length=30),
        Package(79, 0, 0, 10, max_ride_length=30),
        Package(0, 6, 1),
    ]


def main() -> None:
    """Entry point for calculations"""
    dott = get_packages()

    rides = int(input("Amount of rides: "))
    ride_len = int(input("Minutes per ride: "))
    prices = {p: p.get_price(Rides(rides, ride_len)) for p in dott}
    print(min(prices.values()), end="\n----\n")  # noqa: T201
    for package, price in prices.items():
        print(package, price)  # noqa: T201


if __name__ == "__main__":
    main()
