from flask import Flask, render_template

from template_method import (
    School,
    University
)
from visitor import (
    TestVisitorSchool,
    TestVisitorUniversity
)

app = Flask(__name__)


def html(text: str) -> str:
    return text.replace("\n", "<br/>").replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;")


@app.route('/')
def index():
    return render_template(
        'index.html'
    )


@app.route('/template_method')
def template_method():
    school = School()
    school.runAll()
    print(school.runAll())

    university = University()
    university.runAll()
    print(university.runAll())

    return render_template(
        'template_method.html',
        template_method1=html(school.runAll()),
        template_method2=html(university.runAll())
    )


@app.route('/visitor')
def visitor():
    s = TestVisitorSchool()
    s.setProduct()
    visitor1 = f"Всего к оплате за покупки к школе: {s.GetCost()}"
    print(visitor1)

    u = TestVisitorUniversity()
    u.setProduct()
    visitor2 = f"Всего к оплате за покупки к институту: {u.GetCost()}"
    print(visitor2)

    return render_template(
        'visitor.html',
        visitor1=html(visitor1),
        visitor2=html(visitor2)
    )


if __name__ == "__main__":
    app.run('127.0.0.1', debug=True)