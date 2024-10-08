def loading_bar(progress_number: int) -> str:
    if progress_number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    loaded_percents_as_digits = progress_number // 10  # symbol %
    not_loaded_percents_as_digits = 10 - loaded_percents_as_digits  # symbol .
    return f"{progress_number}% [{loaded_percents_as_digits * '%'}{not_loaded_percents_as_digits * '.'}]\nStill loading..."


number = int(input())
print(loading_bar(number))
