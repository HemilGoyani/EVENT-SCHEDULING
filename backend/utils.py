from django.contrib.gis.geoip2 import GeoIP2


def get_currency_by_country(country_code):
    # Define your mapping of country codes to currencies
    currency_map = {
        'US': 'USD',
        'GB': 'GBP',
        'DE': 'EUR',
        # Add more country codes and currencies as needed
    }

    # Get the currency for the given country code
    currency = currency_map.get(country_code)
    
    # If the country code is not found in the mapping, set a default currency
    if not currency:
        currency = 'USD'  # Set a default currency, such as USD

    return currency


def get_currency_by_location(ip_address):
    g = GeoIP2()
    location = g.city(ip_address)
    country_code = location['country_code']
    
    # Perform logic to map country_code to currency
    currency = get_currency_by_country(country_code)
    
    return currency