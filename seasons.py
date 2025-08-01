from datetime import date
import sys
import inflect


def main():
    date_of_birth = get_dob(input("Enter your date of birth (YYYY-MM-DD): "))
    age_in_minutes = get_age_in_minutes(date_of_birth)
    age_in_words = get_minutes_in_words(age_in_minutes)
    print(f"{age_in_words} minutes")
    

def get_dob(dob):
    try:
        date_of_birth = date.fromisoformat(dob)
        return date_of_birth
    except ValueError:
        sys.exit("Invalid date format. Please use YYYY-MM-DD.")

def get_age_in_minutes(date_of_birth):
    # if today_date is None:
    today_date = date.today()
    days_diff = (today_date - date_of_birth).days
    minutes_past = days_diff * 24 * 60
    return minutes_past

def get_minutes_in_words(minutes_past):
    p = inflect.engine()
    return p.number_to_words(minutes_past, andword=" ", comma=False).capitalize()


if __name__ == "__main__":
    main()