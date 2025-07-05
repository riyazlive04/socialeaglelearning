from playwright.async_api import async_playwright
import asyncio

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://www.bing.com/")

        # Handle "Stay signed out" span if present
        try:
            # Wait for it to appear, but don't fail if it doesn't exist
            await page.locator("text=Stay signed out").first.wait_for(timeout=5000)
            await page.locator("text=Stay signed out").first.click()
            print("Clicked 'Stay signed out' span.")
        except:
            print("No 'Stay signed out' span found.")

        # Wait for the search box
        await page.wait_for_selector('textarea[name="q"]', timeout=10000)

        # Fill the search box
        await page.fill('textarea[name="q"]', "India vs England score")
        await page.press('textarea[name="q"]', "Enter")

        """# Wait for results
        await page.wait_for_selector('h3', timeout=10000)

        # Click first search result
        first_result = await page.query_selector('h3')
        if first_result:
            parent_link = await first_result.evaluate_handle("node => node.closest('a')")
            if parent_link:
                await parent_link.click()
                print("Clicked first search result.")
            else:
                print("No link found for first result.")
        else:
            print("No search results found.")"""

        await page.wait_for_timeout(50000)
        #await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
