import argparse
import sys
from src.loader import load_stars, filter_stars_by_magnitude, sort_stars
from src.display import render_table

def main():
    parser = argparse.ArgumentParser(description="Stellar CLI: Visualize star data.")
    parser.add_argument("--file", required=True, help="Path to the JSON star catalog")
    parser.add_argument("--max-mag", type=float, help="Filter stars by maximum magnitude")
    parser.add_argument("--sort", choices=["mag", "name"], help="Sort stars by property")

    args = parser.parse_args()

    try:
        stars = load_stars(args.file)
        
        if args.max_mag is not None:
            stars = filter_stars_by_magnitude(stars, args.max_mag)

            if args.sort:
                stars = sort_stars(stars, key=args.sort)
            
        print(render_table(stars))
    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()