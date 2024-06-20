import argparse
from .ukpostcode import UKPostcode


def main():
    parser = argparse.ArgumentParser(description="Validate and format UK postcodes.")
    parser.add_argument('postcode', type=str, help="The postcode to validate and format.")
    args = parser.parse_args()

    try:
        postcode = UKPostcode(args.postcode)
        print(f"Postcode: {postcode.raw_postcode}")
        print(f"Formatted: {postcode}")
        print(f"Outward Code: {postcode.get_outward_code()}")
        print(f"Inward Code: {postcode.get_inward_code()}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
