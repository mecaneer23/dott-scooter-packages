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
        max_rides: int = 0,
    ) -> None:
        self.package_price = package_price
        self.unlock_price = unlock_price
        self.price_per_minute = price_per_minute
        self.max_rides = max_rides

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

    def get_price(self, amount_of_rides: int, minutes_per_ride: int) -> int:
        """Return the price for a certain amount of `m` length rides"""
        return (
            self.package_price
            * self._get_package_multiplier(amount_of_rides, self.max_rides)
            + self.unlock_price * amount_of_rides
            + self.price_per_minute * minutes_per_ride * amount_of_rides
        )

    def __str__(self) -> str:
        return f"{self.package_price}"


def get_packages() -> list[Package]:
    """Return a list of Packages which represent available Dott Packages"""
    return [
        Package(16, 0, 1),
        Package(18, 0, 0, 2),
        Package(19, 9, 0),
        Package(45, 6, 0),
        Package(79, 0, 0, 10),
        Package(0, 6, 1),
    ]


def main() -> None:
    """Entry point for calculations"""
    dott = get_packages()

    rides = int(input("Amount of rides: "))
    ride_len = int(input("Minutes per ride: "))
    print(min(dott, key=lambda p: p.get_price(rides, ride_len)), end="\n----\n")  # noqa: T201
    for p in dott:
        print(p, p.get_price(rides, ride_len))  # noqa: T201


if __name__ == "__main__":
    main()
