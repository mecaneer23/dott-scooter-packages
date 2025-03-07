#!/usr/bin/env python3
"""
Calculate the best scooter package given certain factors
"""


class Package:
    """Represent a scooter bundle pricing package"""

    def __init__(
        self,
        package_price: int,
        unlock_price: int,
        price_per_minute: int,
    ) -> None:
        self.package_price = package_price
        self.unlock_price = unlock_price
        self.price_per_minute = price_per_minute

    def get_price(self, amount_of_rides: int, minutes_per_ride: int) -> int:
        """Return the price for a certain amount of `m` length rides"""
        return (
            self.package_price
            + self.unlock_price * amount_of_rides
            + self.price_per_minute * minutes_per_ride * amount_of_rides
        )

    def __str__(self) -> str:
        return f"{self.package_price}"


def main() -> None:
    """Entry point for calculations"""
    dott = [
        Package(16, 0, 1),
        Package(18, 0, 0),
        Package(19, 9, 0),
        Package(45, 6, 0),
        Package(79, 0, 0),
        Package(0, 6, 1),
    ]

    rides = int(input("Amount of rides: "))
    ride_len = int(input("Minutes per ride: "))
    # print(min(dott, key=lambda p: p.get_price(rides, ride_len)))  # noqa: T201
    for p in dott:
        print(p, p.get_price(rides, ride_len))


if __name__ == "__main__":
    main()
