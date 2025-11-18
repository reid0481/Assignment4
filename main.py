import time

def main():
    hours = prompt_for_int("Input number of hours: ")
    minutes = prompt_for_int("Input number of minutes: ")
    seconds = prompt_for_int("Input number of seconds: ")

    total_seconds = hours * 3600 + minutes * 60 + seconds

    if total_seconds <= 0:
        print("Timer duration must be greater than zero seconds.")
        return

    run_timer(total_seconds)


def prompt_for_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a whole number.")


def run_timer(total_seconds):
    for remaining in range(total_seconds, -1, -1):
        render_progress(total_seconds, remaining)
        if remaining > 0:
            time.sleep(1)
    print("\nTimer complete!")


def render_progress(total_seconds, remaining):
    elapsed = total_seconds - remaining
    fraction = elapsed / total_seconds
    filled_length = int(30 * fraction)
    bar = "#" * filled_length + "-" * (30 - filled_length)
    formatted_remaining = format_time(remaining)
    percent = fraction * 100
    print(f"\r[{bar}] {percent:5.1f}% | Time left: {formatted_remaining}", end="")


def format_time(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


if __name__ == "__main__":
    main()