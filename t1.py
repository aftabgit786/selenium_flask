from flask import Flask, render_template, request
from selenium import webdriver
from bs4 import BeautifulSoup
from utils import scroll_to_page_end, extract_comments_data

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    url = request.form['url']
    driver = webdriver.Chrome()
    driver.get(url)

    scroll_to_page_end(driver)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    comments_data = extract_comments_data(soup)

    driver.quit()

    video_title = soup.title.string

    return render_template('results.html', comments_data=comments_data, video_title=video_title)


if __name__ == '__main__':
    app.run(debug=True)
