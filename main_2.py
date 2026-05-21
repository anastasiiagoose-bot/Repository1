#import utils
from pywebio.input import input, input_group
from pywebio.output import put_text
from pywebio import start_server
from pywebio.session import run_js


def main():

    data = input_group(
        "Запит на поточну погоду",
        [
            input("City", name="city", required=True),
            input("Email", name="email", required=True),
            input("Name", name="name", required=True),
        ]
    )
    print(data)

    run_js("""
        setTimeout(() => {
            window.location.reload();
        }, 5000);
    """)
    # current_weather = utils.get_weather_info(city)
    # put_text(f"Температура у {city}: {current_weather['temperature']}")


start_server(
    main,
    host="0.0.0.0",
    port=8888,
    debug=True,
)