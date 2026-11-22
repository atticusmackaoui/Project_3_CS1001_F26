import build_data
import data


# Part 1
def population_total(counties: list[data.CountyDemographics]) -> int:
    """
    Calculate the total 2014 population for a list of CountyDemographics objects.
    """
    if not counties:
        return 0

    population_sum = 0
    for county in counties:
        population_sum += county.population['2014 Population']

    return population_sum


# Part 2
def filter_by_state(counties: list[data.CountyDemographics], state: str) -> list[data.CountyDemographics]:
    """
    Filter a list of CountyDemographics objects by state.
    """
    if not counties:
        return []

    if not state:
        return []

    filtered_counties = []
    for county in counties:
        if county.state == state:
            filtered_counties.append(county)

    return filtered_counties


# Part 3
def population_by_education(counties: list[data.CountyDemographics], key: str) -> float:
    """
    Calculate the total population for a list of CountyDemographics objects based on a specific education key.
    """
    if not counties:
        return 0

    if not key:
        return 0
    
    population_sum = 0
    for county in counties:
        if key in county.education:
            population_sum += county.education[key] * county.population['2014 Population'] / 100

    return population_sum


def population_by_ethnicity(counties: list[data.CountyDemographics], key: str) -> float:
    """
    Calculate the total population for a list of CountyDemographics objects based on a specific ethnicity key.
    """
    if not counties:
        return 0

    if not key:
        return 0
    
    population_sum = 0
    for county in counties:
        if key in county.ethnicities:
            population_sum += county.ethnicities[key] * county.population['2014 Population'] / 100

    return population_sum


def population_below_poverty_level(counties: list[data.CountyDemographics]) -> float:
    """
    Calculate the total population below the poverty level for a list of CountyDemographics objects.
    """
    if not counties:
        return 0

    population_sum = 0
    for county in counties:
        population_sum += county.income['Persons Below Poverty Level'] * county.population['2014 Population'] / 100

    return population_sum   


# Part 4
def percent_by_education(counties: list[data.CountyDemographics], key: str) -> float:
    """
    Calculate the percentage of the population for a list of CountyDemographics objects based on a specific education key.
    """
    if not counties:
        return 0

    if not key:
        return 0

    total_population = population_total(counties)
    sub_population = population_by_education(counties, key)

    if total_population == 0:
        return 0

    return (sub_population / total_population) * 100


def percent_by_ethnicity(counties: list[data.CountyDemographics], key: str) -> float:
    """
    Calculate the percentage of the population for a list of CountyDemographics objects based on a specific ethnicity key.
    """
    if not counties:
        return 0
    
    if not key:
        return 0

    total_population = population_total(counties)
    sub_population = population_by_ethnicity(counties, key)

    if total_population == 0:
        return 0
    
    return (sub_population / total_population) * 100


def percent_below_poverty_level(counties: list[data.CountyDemographics]) -> float:
    """
    Calculate the percentage of the population below the poverty level for a list of CountyDemographics objects.
    """
    if not counties:
        return 0

    total_population = population_total(counties)
    sub_population = population_below_poverty_level(counties)

    if total_population == 0:
        return 0

    return (sub_population / total_population) * 100


# Part 5
def education_greater_than(counties: list[data.CountyDemographics], key: str, threshold: float) -> list[data.CountyDemographics]:
    """
    Determine which counties have a percentage of the population with a specific education level greater than a given threshold.
    """
    if not counties:
        return []

    if not key:
        return []

    filtered_counties = []
    for county in counties:
        if county.education[key] > threshold:
            filtered_counties.append(county)
            
    return filtered_counties


def education_less_than(counties: list[data.CountyDemographics], key: str, threshold: float) -> list[data.CountyDemographics]:
    """
    Determine which counties have a percentage of the population with a specific education level less than a given threshold.
    """
    if not counties:
        return []

    if not key:
        return []

    filtered_counties = []
    for county in counties:
        if county.education[key] < threshold:
            filtered_counties.append(county)
            
    return filtered_counties


def ethnicity_greater_than(counties: list[data.CountyDemographics], key: str, threshold: float) -> list[data.CountyDemographics]:
    """
    Determine which counties have a percentage of the population with a specific ethnicity greater than a given threshold.
    """
    if not counties:
        return []

    if not key:
        return []

    filtered_counties = []
    for county in counties:
        if county.ethnicities[key] > threshold:
            filtered_counties.append(county)
            
    return filtered_counties


def ethnicity_less_than(counties: list[data.CountyDemographics], key: str, threshold: float) -> list[data.CountyDemographics]:
    """
    Determine which counties have a percentage of the population with a specific ethnicity less than a given threshold.
    """
    if not counties:
        return []

    if not key:
        return []

    filtered_counties = []
    for county in counties:
        if county.ethnicities[key] < threshold:
            filtered_counties.append(county)

    return filtered_counties


def below_poverty_level_greater_than(counties: list[data.CountyDemographics], threshold: float) -> list[data.CountyDemographics]:
    """
    Determine which counties have a percentage of the population below the poverty level greater than a given threshold.
    """
    if not counties:
        return []

    filtered_counties = []
    for county in counties:
        if county.income['Persons Below Poverty Level'] > threshold:
            filtered_counties.append(county)

    return filtered_counties

def below_poverty_level_less_than(counties: list[data.CountyDemographics], threshold: float) -> list[data.CountyDemographics]:
    """
    Determine which counties have a percentage of the population below the poverty level less than a given threshold.
    """
    if not counties:
        return []

    filtered_counties = []
    for county in counties:
        if county.income['Persons Below Poverty Level'] < threshold:
            filtered_counties.append(county)

    return filtered_counties