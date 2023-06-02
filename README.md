# Weather-Info-Site

Welcome to the Weather-Info-Site repository! This repository contains a Django web application that allows users to input a city name and retrieve weather information for that city. Additionally, the website provides a dynamic background video that reflects the current weather conditions in the entered city.

## Features

- User-friendly interface: The website offers a simple and intuitive interface for users to enter their desired city and retrieve weather information.
- Weather data: The application fetches weather data from a reliable weather API, providing accurate and up-to-date information.
- Dynamic background videos: Depending on the weather conditions in the entered city, the website displays a background video that reflects the current weather, enhancing the user experience.
- Responsive design: The site is designed to be responsive, ensuring optimal user experience across various devices and screen sizes.
- Caching: To improve performance, the application implements caching mechanisms to store frequently accessed weather data.

## Prerequisites

Before running the Weather-Info-Site application, ensure that you have the following prerequisites installed:

- Python (version 3.7 or higher)
- Django (version 3.0 or higher)
- OpenWeatherMap API key: You will need a valid API key from a weather service provider. Refer to the next section for instructions on obtaining an API key.

## Getting Started

To get started with Weather-Info-Site, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/your-username/Weather-Info-Site.git
   ```

2. Navigate to the project directory:

   ```
   cd Weather-Info-Site
   ```

3. Install the project dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Obtain a OpenWeatherMap API key:

   - Visit a weather service provider's website and sign up for an API key https://openweathermap.org/appid
   - Copy the API key provided by the weather service provider.

5. Configure the API key:

   - Open the `views.py` file located in the `weather` directory.
   - Locate the `api_key` variable and replace `"enter api key from openweather"` with your actual weather API key.

6. Run database migrations:

   ```
   python manage.py migrate
   ```

7. Start the development server:

   ```
   python manage.py runserver
   ```

8. Access the Weather-Info-Site:

   Open your web browser and visit `http://localhost:8000` to access the application.


## License

The Weather-Info-Site repository is open-source software licensed under the [Apache-2.0 license](https://opensource.org/licenses/Apache-2.0-license). Feel free to modify and distribute the code as per the license terms.
