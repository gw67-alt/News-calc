def find_year_day_combinations(target_years):
    """Find combinations where Year + Day(1-31) = Target Year"""
    years = range(1, 2033)  # Available years
    days = range(1, 32)     # Days cycle from 1 to 31
    
    for target_year in target_years:
        print(f"\nTarget Year: {target_year}")
        solutions = []
        
        for year in years:
            # Check if target_year - year is a valid day between 1-31
            day = target_year - year
            if day in days:
                solutions.append((year, day))
        
        if solutions:
            print(f"Found {len(solutions)} solutions:")
            for year, day in sorted(solutions):
                print(f"  Year {year} + Day {day:2d} = {target_year}")
        else:
            print("No solutions found")

# Test target years in range
target_years = range(2000, 2033)
find_year_day_combinations(target_years)
