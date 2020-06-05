from flask import Flask

import folium

app = Flask(__name__)


@app.route('/')
def index():
    m = folium.Map(
    location=[45.372, -121.6972],
    zoom_start=12,
    tiles='Stamen Terrain'
    )

    tooltip = 'Click me!'

    folium.Marker([45.3288, -121.6625], popup='<i>Mt. Hood Meadows</i>', tooltip=tooltip).add_to(m)
    folium.Marker([45.3311, -121.7113], popup='<b>Timberline Lodge</b>', tooltip=tooltip).add_to(m)


    return m._repr_html_()


if __name__ == '__main__':
    app.run(debug=True)