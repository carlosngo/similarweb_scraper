def clean_data(data):
    top_countries = data["geography"]["topCountriesTraffics"]
    age_distribution = data["demographics"]["ageDistribution"]

    cleaned_data = remove_irrelevant_data(data)
    cleaned_data = flatten_top_countries(cleaned_data, top_countries)
    cleaned_data = flatten_age_distribution(cleaned_data, age_distribution)
    cleaned_data = normalize_data(cleaned_data)

    return cleaned_data


def remove_irrelevant_data(data):
    domain = data["domain"]
    rank_history = data["ranking"]["globalRankCompetitorsHistory"][domain]
    visits_history = data["traffic"]["visitsHistory"]

    return {
        "domain": domain,
        "global_rank": data["overview"]["globalRank"],
        "total_visits": data["overview"]["visitsTotalCount"],
        "bounce_rate": data["overview"]["bounceRateFormatted"],
        "pages_per_visit": data["overview"]["pagesPerVisit"],
        "avg_visit_duration": data["traffic"]["visitsAvgDurationFormatted"],
        "oct_rank": rank_history[0]["rank"],
        "nov_rank": rank_history[1]["rank"],
        "dec_rank": rank_history[2]["rank"],
        "oct_visits": visits_history.get("2022-10-01"),
        "nov_visits": visits_history.get("2022-11-01"),
        "dec_visits": visits_history.get("2022-12-01"),
        "visits_change": data["traffic"]["visitsTotalCountChange"],
    }


def flatten_top_countries(data, top_countries):
    flattened_data = data

    for idx, country_dict in enumerate(top_countries):
        flattened_data[f"top_country_{idx}_code"] = country_dict["countryAlpha2Code"]
        flattened_data[f"top_country_{idx}_share"] = country_dict["visitsShare"]
        flattened_data[f"top_country_{idx}_share_change"] = country_dict["visitsShareChange"]

    return flattened_data


def flatten_age_distribution(data, age_distribution):
    flattened_data = data

    for age_distribution_dict in age_distribution:
        min_age = age_distribution_dict["minAge"]
        max_age = age_distribution_dict.get("maxAge")
        distribution = age_distribution_dict["value"]
        key = f"age_{min_age}_{max_age}" if max_age is not None else f"age_{min_age}"
        flattened_data[key] = distribution

    return flattened_data


def normalize_data(data):
    normalized_data = data
    normalized_data["bounce_rate"] = normalize_percent(data["bounce_rate"])
    normalized_data["avg_visit_duration"] = normalize_duration(data["avg_visit_duration"])
    normalized_data["oct_visits"] = normalize_number_str(normalized_data["oct_visits"])
    normalized_data["nov_visits"] = normalize_number_str(normalized_data["nov_visits"])
    normalized_data["dec_visits"] = normalize_number_str(normalized_data["dec_visits"])
    return normalized_data


def normalize_percent(percent_str):
    if percent_str == "":
        return 0
    return float(percent_str[:-1]) / 100.0


def normalize_duration(duration_str):
    if duration_str == "":
        return 0
    hours, minutes, seconds = duration_str.split(":")
    return int(hours) * 3600 + int(minutes) * 60 + int(seconds)


def normalize_number_str(number_str):
    if number_str is None:
        return 0
    return int(number_str)
