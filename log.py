import os

REPOS = {
    "pyecharts": [
        "pyecharts",
        "echarts-themes-pypkg",
        "echarts-themes-js",
        "pyecharts-javascripthon",
        "pyecharts-javascripthon-api-service",
        "echarts-china-provinces-pypkg",
        "echarts-countries-pypkg",
        "pypkg-mobans",
        "jupyter-echarts-pypkg",
        "pyecharts-snapshot",
        "jupyter-echarts",
        "echarts-china-counties-pypkg",
        "assets",
        "echarts-china-misc-pypkg",
        "echarts-china-cities-pypkg",
        "echarts-united-kingdom-pypkg",
        "pyecharts-cli",
        "pyecharts-users-cases",
        "pyecharts-jupyter-installer",
        "pyecharts-app",
        "echarts-themes-pypkg",
        "echarts-cities-pypkg",
        "flask_demo",
        "echarts-cities-js",
        "echarts-themes-js",
        "pyecharts.js-app"
    ],
    "echarts-maps": [
        "echarts-china-provinces-js",
        "echarts-china-counties-js",
        "echarts-mapmaker",
        "echarts-js-mobans",
        "echarts-maps-project-info",
        "echarts-china-misc-js",
        "echarts-china-cities-js",
        "echarts-united-kingdom-js",
        "echarts-countries-js"
    ],
    "kinegratii": [
        "django-echarts"
    ]
}


for org, repos in REPOS.items():
    for repo in repos:
        if os.path.exists(repo):
            more = "cd {0} && git pull&& gource --output-custom-log ../{0}.log".format(repo)
            os.system(more)
        else:
            command = "git clone https://github.com/{0}/{1}".format(org, repo)
            more = "cd {0} && gource --output-custom-log ../{0}.log".format(repo)
            os.system(command)
            os.system(more)
