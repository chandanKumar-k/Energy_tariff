"""Electricity meter management and tariff calculation system."""

import json
from datetime import datetime

# Global state
meters = {}
RATE_TIER_1 = 3.5
RATE_TIER_2 = 5.0
RATE_TIER_3 = 7.5
SPIKE_LIMIT = 500


def record_reading(meter_id, units, history=None):
    """Record electricity usage for a meter."""
    if history is None:
        history = []

    history.append((meter_id, units, str(datetime.now())))
    meters[meter_id] = meters.get(meter_id, 0) + units
    return history


def compute_bill(meter_id, tier_rates):
    """Calculate an electricity bill using tiered rates."""
    units = meters[meter_id]

    if units <= 100:
        return units * tier_rates[0]

    if units <= 300:
        return (
            100 * tier_rates[0]
            + (units - 100) * tier_rates[1]
        )

    return (
        100 * tier_rates[0]
        + 200 * tier_rates[1]
        + (units - 300) * tier_rates[2]
    )


def raise_rates(percent):
    """Increase all electricity tariff rates by a percentage."""
    global RATE_TIER_1, RATE_TIER_2, RATE_TIER_3

    multiplier = 1 + percent / 100
    RATE_TIER_1 *= multiplier
    RATE_TIER_2 *= multiplier
    RATE_TIER_3 *= multiplier


def flag_spikes():
    """Return meter IDs whose usage exceeds the spike limit."""
    return [
        meter_id
        for meter_id, units in meters.items()
        if units > SPIKE_LIMIT
    ]


def load_meter_data(file="meters.json"):
    """Load meter readings from a JSON file."""
    global meters

    try:
        with open(file, "r", encoding="utf-8") as meter_file:
            meters = json.load(meter_file)
    except (OSError, json.JSONDecodeError):
        meters = {}


def save_meter_data(file="meters.json"):
    """Save meter readings to a JSON file."""
    with open(file, "w", encoding="utf-8") as meter_file:
        json.dump(meters, meter_file)


def main():
    """Run the electricity meter and billing demonstration."""
    record_reading("M-01", 120)
    record_reading("M-02", 640)
    history = record_reading("M-03", -50)

    print("Readings stored so far:", len(history))

    raise_rates(10)
    rates = [RATE_TIER_1, RATE_TIER_2, RATE_TIER_3]

    print(f"Bill M-01: {compute_bill('M-01', rates):.2f}")
    print(f"Bill M-03: {compute_bill('M-03', rates):.2f}")
    print("Spikes:", flag_spikes())

    adjustment_text = input(
        "Extra units for M-01 (Enter for 0): "
    ).strip()

    try:
        adjustment = int(adjustment_text) if adjustment_text else 0

        if adjustment < 0:
            print("Invalid input. Please enter a non-negative integer.")
        else:
            record_reading("M-01", adjustment)

    except ValueError:
        print("Invalid input. Please enter a whole number.")

    save_meter_data()
    load_meter_data()

    print(
        f"Bill M-01 after reload: "
        f"{compute_bill('M-01', rates):.2f}"
    )


if __name__ == "__main__":
    main()
