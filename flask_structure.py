"""from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Riyaz!"

if __name__ == '__main__':
    app.run(debug=True)"""

"""from flask import Flask, jsonify
import asyncio
from playwright.async_api import async_playwright

app = Flask(__name__)

async def show_score():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # Go to Google
        await page.goto("https://www.google.com")

        # Accept cookies or stay signed out if visible (optional)
        try:
            button = page.locator("text=Stay signed out")
            if await button.is_visible():
                await button.click()
                await page.wait_for_load_state("load")
        except:
            pass

        # Wait for the search box (correct selector!)
        await page.wait_for_selector('textarea[name="q"]', timeout=10000)

        # Type query and press Enter
        await page.fill('textarea[name="q"]', "India vs England score")
        await page.keyboard.press("Enter")

        # Wait for results to load
        await page.wait_for_selector("h3", timeout=10000)

        # Keep the browser open for you to view results
        await page.wait_for_timeout(30000)

        await browser.close()

@app.route('/show-score', methods=['GET'])
def trigger_show_score():
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(show_score())
        return jsonify({"status": "Browser launched and search performed."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)"""

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    try:
        # Get data from request (GET or POST)
        if request.method == 'POST':
            data = request.get_json()
        else:
            data = request.args

        num1 = float(data.get('num1'))
        num2 = float(data.get('num2'))
        operation = data.get('operation', '').lower()

        result = None

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return jsonify({'error': 'Division by zero not allowed'}), 400
            result = num1 / num2
        else:
            return jsonify({'error': 'Invalid operation'}), 400

        return jsonify({
            'num1': num1,
            'num2': num2,
            'operation': operation,
            'result': result
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

